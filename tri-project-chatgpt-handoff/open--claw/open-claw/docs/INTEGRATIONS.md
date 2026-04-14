# Open Claw — Target Integrations

## Overview

These are the intended integration targets for Open Claw. This document lists
what we plan to connect to, not how. No setup steps, credentials, or configuration
are included here.

## Integration targets

| Integration   | Module  | Purpose                                        |
|---------------|---------|------------------------------------------------|
| GitHub        | dev     | Repository operations, issues, pull requests   |
| Playwright    | web     | Browser automation and UI verification         |
| Context7      | dev     | Library documentation lookup                   |
| Firecrawl     | web     | Structured web extraction and scraping         |
| Google Sheets | comms   | Spreadsheet data read/write                    |
| Firestore     | memory  | Persistent document storage                    |
| Mem0          | memory  | Cross-session memory and pattern recall        |

## Notes

- All integrations are accessed via MCP tools installed in the IDE environment.
- No integration credentials are stored in this repo.
- Integration availability is checked at runtime; failures are reported per the MCP failure policy in `.cursor/rules/05-global-mcp-usage.md`.
- New integrations can be added by creating a new MCP tool configuration outside the repo and updating this document.
