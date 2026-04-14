#!/usr/bin/env python3
import json
import os
import re
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path


SERVER_NAME = "openmemory"
SERVER_VERSION = "local-1.0.1"
PROTOCOL_VERSION = "2025-11-25"
SUPPORTED_PROTOCOL_VERSIONS = {
    "2024-11-05",
    "2025-03-26",
    "2025-06-18",
    "2025-11-25",
}
CLIENT_NAME = os.environ.get("CLIENT_NAME", "cursor")
DEBUG_LOG = os.environ.get("OPENMEMORY_DEBUG_LOG") == "1"
TRACE_FILE = os.environ.get("OPENMEMORY_TRACE_FILE")
STORE_PATH = Path(
    os.environ.get(
        "OPENMEMORY_STORE_PATH",
        str(Path.home() / ".openclaw" / "data" / "openmemory-cursor.sqlite3"),
    )
)
MAX_LIST_RESULTS = 100
MAX_SEARCH_CANDIDATES = 500
MAX_SEARCH_RESULTS = 20
TRANSPORT_MODE = "content-length"


def log(message: str) -> None:
    if DEBUG_LOG:
        print(message, file=sys.stderr, flush=True)


def trace(message: str) -> None:
    if not TRACE_FILE:
        return
    trace_path = Path(TRACE_FILE)
    trace_path.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).isoformat()
    with trace_path.open("a", encoding="utf-8") as handle:
        handle.write(f"{timestamp} {message}\n")


def normalize_text(value: str) -> str:
    return " ".join(value.lower().split())


def tokenize_query(query: str) -> list[str]:
    return [token for token in re.findall(r"[A-Za-z0-9_-]+", query.lower()) if token]


class MemoryStore:
    def __init__(self, db_path: Path, client_name: str) -> None:
        self.db_path = db_path
        self.client_name = client_name
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(str(self.db_path))
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("PRAGMA journal_mode=WAL;")
        self.conn.execute("PRAGMA synchronous=NORMAL;")
        self._init_schema()

    def _init_schema(self) -> None:
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS memories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                client_name TEXT NOT NULL,
                content TEXT NOT NULL,
                normalized_content TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )
        self.conn.execute(
            """
            CREATE UNIQUE INDEX IF NOT EXISTS idx_memories_client_normalized
            ON memories (client_name, normalized_content)
            """
        )
        self.conn.commit()

    def add_memory(self, content: str) -> tuple[int, bool]:
        normalized = normalize_text(content)
        now = datetime.now(timezone.utc).isoformat()
        cur = self.conn.execute(
            """
            INSERT OR IGNORE INTO memories (client_name, content, normalized_content, created_at)
            VALUES (?, ?, ?, ?)
            """,
            (self.client_name, content, normalized, now),
        )
        self.conn.commit()
        if cur.rowcount:
            memory_id = cur.lastrowid
            return int(memory_id), True

        row = self.conn.execute(
            """
            SELECT id FROM memories
            WHERE client_name = ? AND normalized_content = ?
            """,
            (self.client_name, normalized),
        ).fetchone()
        return int(row["id"]), False

    def list_memories(self) -> list[sqlite3.Row]:
        return self.conn.execute(
            """
            SELECT id, content, created_at
            FROM memories
            WHERE client_name = ?
            ORDER BY id DESC
            LIMIT ?
            """,
            (self.client_name, MAX_LIST_RESULTS),
        ).fetchall()

    def search_memories(self, query: str) -> list[dict]:
        tokens = tokenize_query(query)
        normalized_query = normalize_text(query)
        rows = self.conn.execute(
            """
            SELECT id, content, created_at
            FROM memories
            WHERE client_name = ?
            ORDER BY id DESC
            LIMIT ?
            """,
            (self.client_name, MAX_SEARCH_CANDIDATES),
        ).fetchall()

        results = []
        for row in rows:
            content = row["content"]
            normalized_content = normalize_text(content)
            score = 0.0

            if normalized_query and normalized_query in normalized_content:
                score += 5.0

            token_hits = 0
            for token in tokens:
                if token in normalized_content:
                    token_hits += 1
                    score += 1.0

            if tokens and token_hits == len(tokens):
                score += 2.0

            if score <= 0:
                continue

            score += min(row["id"] / 1_000_000.0, 0.25)
            results.append(
                {
                    "id": row["id"],
                    "memory": content,
                    "created_at": row["created_at"],
                    "score": round(score, 3),
                }
            )

        results.sort(key=lambda item: (item["score"], item["id"]), reverse=True)
        return results[:MAX_SEARCH_RESULTS]

    def delete_all_memories(self) -> int:
        cur = self.conn.execute(
            "DELETE FROM memories WHERE client_name = ?",
            (self.client_name,),
        )
        self.conn.commit()
        return int(cur.rowcount or 0)


STORE = MemoryStore(STORE_PATH, CLIENT_NAME)


TOOLS = [
    {
        "name": "add-memory",
        "title": "Add Memory",
        "description": "Add a new memory to the durable local store.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "content": {
                    "type": "string",
                    "description": "The content to store in memory.",
                }
            },
            "required": ["content"],
            "additionalProperties": False,
        },
    },
    {
        "name": "search-memories",
        "title": "Search Memories",
        "description": "Search through locally stored memories.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query.",
                }
            },
            "required": ["query"],
            "additionalProperties": False,
        },
    },
    {
        "name": "list-memories",
        "title": "List Memories",
        "description": "List all memories in the current local memory store.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": [],
            "additionalProperties": False,
        },
    },
    {
        "name": "delete-all-memories",
        "title": "Delete All Memories",
        "description": "Delete all memories in the current local memory store.",
        "inputSchema": {
            "type": "object",
            "properties": {},
            "required": [],
            "additionalProperties": False,
        },
    },
]


def make_text_result(text: str, is_error: bool = False) -> dict:
    return {
        "content": [{"type": "text", "text": text}],
        "isError": is_error,
    }


def send_message(payload: dict) -> None:
    global TRANSPORT_MODE
    data = json.dumps(payload, ensure_ascii=True).encode("utf-8")
    trace(
        f"OUT {payload.get('method', 'response')} "
        f"id={payload.get('id')} bytes={len(data)} transport={TRANSPORT_MODE}"
    )
    if TRANSPORT_MODE == "line-delimited":
        sys.stdout.buffer.write(data + b"\n")
    else:
        sys.stdout.buffer.write(f"Content-Length: {len(data)}\r\n\r\n".encode("ascii"))
        sys.stdout.buffer.write(data)
    sys.stdout.buffer.flush()


def send_response(request_id, result: dict) -> None:
    send_message({"jsonrpc": "2.0", "id": request_id, "result": result})


def send_error(request_id, code: int, message: str) -> None:
    send_message(
        {
            "jsonrpc": "2.0",
            "id": request_id,
            "error": {"code": code, "message": message},
        }
    )


def read_message() -> dict | None:
    global TRANSPORT_MODE
    headers = {}
    while True:
        line = sys.stdin.buffer.readline()
        if not line:
            return None
        stripped = line.strip()
        if stripped.startswith(b"{"):
            try:
                message = json.loads(stripped.decode("utf-8"))
            except json.JSONDecodeError as exc:
                trace(f"line-delimited parse error: {exc}")
                return None
            TRANSPORT_MODE = "line-delimited"
            return message
        if line in (b"\r\n", b"\n"):
            break
        name, _, value = line.decode("utf-8").partition(":")
        headers[name.strip().lower()] = value.strip()

    content_length = int(headers.get("content-length", "0"))
    if content_length <= 0:
        trace(f"MCP request missing content-length headers={headers}")
        return None
    body = sys.stdin.buffer.read(content_length)
    if not body:
        trace(f"MCP request body missing after headers content_length={content_length}")
        return None
    TRANSPORT_MODE = "content-length"
    return json.loads(body.decode("utf-8"))


def handle_initialize(request_id, params: dict) -> None:
    client_protocol_version = params.get("protocolVersion")
    negotiated_protocol_version = (
        client_protocol_version
        if client_protocol_version in SUPPORTED_PROTOCOL_VERSIONS
        else PROTOCOL_VERSION
    )
    trace(
        "initialize "
        f"client_protocol={client_protocol_version!r} "
        f"negotiated_protocol={negotiated_protocol_version!r}"
    )
    send_response(
        request_id,
        {
            "protocolVersion": negotiated_protocol_version,
            "capabilities": {"tools": {"listChanged": False}},
            "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION},
        },
    )


def handle_tools_call(request_id, params: dict) -> None:
    name = params.get("name")
    arguments = params.get("arguments") or {}

    try:
        if name == "add-memory":
            content = (arguments.get("content") or "").strip()
            if not content:
                send_response(request_id, make_text_result("Error: content is required", True))
                return
            memory_id, created = STORE.add_memory(content)
            if created:
                text = f"Memory added successfully (id={memory_id}, store={STORE_PATH})"
            else:
                text = f"Memory already exists (id={memory_id}, store={STORE_PATH})"
            send_response(request_id, make_text_result(text))
            return

        if name == "search-memories":
            query = (arguments.get("query") or "").strip()
            if not query:
                send_response(request_id, make_text_result("No memories found"))
                return
            results = STORE.search_memories(query)
            if not results:
                send_response(request_id, make_text_result("No memories found"))
                return
            lines = []
            for result in results:
                lines.append(
                    f"Memory: {result['memory']}\n"
                    f"Relevance: {result['score']}\n"
                    f"ID: {result['id']}\n"
                    f"Created: {result['created_at']}\n---"
                )
            send_response(request_id, make_text_result("\n".join(lines)))
            return

        if name == "list-memories":
            results = STORE.list_memories()
            if not results:
                send_response(request_id, make_text_result("No memories found"))
                return
            lines = []
            for index, result in enumerate(results, start=1):
                lines.append(
                    f"{index}. Memory: {result['content']}\n"
                    f"ID: {result['id']}\n"
                    f"Created: {result['created_at']}\n---"
                )
            send_response(request_id, make_text_result("\n".join(lines)))
            return

        if name == "delete-all-memories":
            deleted = STORE.delete_all_memories()
            send_response(
                request_id,
                make_text_result(f"Deleted {deleted} memories from {STORE_PATH}"),
            )
            return

        send_response(request_id, make_text_result(f"Unknown tool: {name}", True))
    except Exception as exc:  # pragma: no cover - defensive server boundary
        send_response(request_id, make_text_result(f"Error: {exc}", True))


def main() -> None:
    trace(
        f"startup server={SERVER_NAME} version={SERVER_VERSION} "
        f"client={CLIENT_NAME} store={STORE_PATH}"
    )
    log(
        f"OpenMemory Cursor MCP Server initialized successfully "
        f"(client={CLIENT_NAME}, store={STORE_PATH})"
    )
    while True:
        message = read_message()
        if message is None:
            trace("IN <eof>")
            break

        request_id = message.get("id")
        method = message.get("method")
        params = message.get("params") or {}
        trace(f"IN {method} id={request_id}")

        if method == "initialize" and request_id is not None:
            handle_initialize(request_id, params)
        elif method in ("notifications/initialized", "notifications/cancelled", "$/cancelRequest"):
            continue
        elif method == "tools/list" and request_id is not None:
            send_response(request_id, {"tools": TOOLS})
        elif method == "resources/list" and request_id is not None:
            send_response(request_id, {"resources": []})
        elif method == "resources/templates/list" and request_id is not None:
            send_response(request_id, {"resourceTemplates": []})
        elif method == "prompts/list" and request_id is not None:
            send_response(request_id, {"prompts": []})
        elif method == "tools/call" and request_id is not None:
            handle_tools_call(request_id, params)
        elif method == "ping" and request_id is not None:
            send_response(request_id, {})
        elif method == "shutdown" and request_id is not None:
            send_response(request_id, {})
        elif method == "exit":
            break
        elif request_id is not None:
            send_error(request_id, -32601, f"Method not found: {method}")


if __name__ == "__main__":
    main()
