# OpenMemory Install CLI

A command-line tool for installing OpenMemory MCP servers across different AI clients.

## Installation

```bash
npm install -g @openmemory/install
```

## Usage

Install OpenMemory MCP server to a supported AI client:

```bash
npx @openmemory/install --client <client> --env OPENMEMORY_API_KEY=<your_api_key> [options]
```

### Options

- `--client` - Client to use for installation (required)
- `--env` - Environment variables as key=value pairs. `OPENMEMORY_API_KEY` is required, `CLIENT_NAME` is automatically set
- `--name` - Name of the server in config (defaults to "openmemory")

### Supported Clients

- `claude` - Claude Desktop
- `cline` - Cline VS Code extension
- `roocline` - Roo Cline VS Code extension
- `windsurf` - Windsurf IDE
- `witsy` - Witsy
- `enconvo` - Enconvo
- `cursor` - Cursor IDE

### Examples

Basic installation:
```bash
npx @openmemory/install --client cursor --env OPENMEMORY_API_KEY=om-xxx
```

Install with custom name:
```bash
npx @openmemory/install --client claude --env OPENMEMORY_API_KEY=om-xxx --name my-openmemory
```

Install with additional environment variables:
```bash
npx @openmemory/install --client claude --env OPENMEMORY_API_KEY=om-xxx --env CUSTOM_VAR=value
```

## Development

### Building

```bash
pnpm build
```

### Development Mode

```bash
pnpm dev
```

### Testing

The package currently validates the built CLI entrypoint in `dist/` with smoke tests.

```bash
pnpm test
```

## License

ISC 