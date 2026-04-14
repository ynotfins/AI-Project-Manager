# Open Claw — Requirements

This document defines the functional and non-functional requirements for the Open Claw platform. The finished-product goal and quality bar are defined in `open-claw/AI_Employee_knowledgebase/FINAL_OUTPUT_PRODUCT.md`, which this document serves and does not supersede.

## Core capabilities

- **Autonomous software delivery**: The AI employee team can execute the full software-delivery lifecycle — goal intake, planning, architecture, implementation, testing, QA, release, and monitoring — without routine user intervention
- **Code assistance**: Navigate, search, edit, and refactor code using MCP tools
- **App development**: Scaffold, build, test, and deploy projects to production under Sparky's quality authority
- **Communication**: Interact with messaging and notification systems; route Tony-gate notifications to Tony via configured channel
- **MCP tool leverage**: Maximize installed MCP tools for all operations
- **Persistent memory**: Store and recall decisions, patterns, and context across sessions
- **Continuous refactoring**: The system actively monitors and improves its own code, workflows, prompts, and discipline

## Functional requirements

- Orchestrator accepts goal-level instructions and routes work to the appropriate specialist employee
- Sparky reviews every file change and may approve, reject, or require refactor without user involvement
- Delivery Director manages sequencing, dependency tracking, and throughput
- Memory module persists facts, decisions, and patterns per the memory contract
- Dev module interfaces with code-intelligence and repo tools
- Comms module interfaces with messaging and notification services
- Web module interfaces with browser automation and extraction tools
- Governance overlay classifies every action per `GOVERNANCE_MODEL.md` and enforces Tony-gate halts
- Model routing escalates internally — employees may route to stronger models or Sparky without user confirmation

## Non-functional requirements

- **Autonomous**: Routine delivery phases do not depend on user approval, manual sequencing, or constant human direction
- **Apple-quality output**: All user-facing software must aim for Apple Inc.-level clarity, polish, and simplicity
- **Modular**: Each module can be developed and tested independently
- **Transparent**: All actions logged with PASS/FAIL evidence; all file changes trigger Sparky review
- **Secure**: No secrets in code or docs; credentials managed externally via Bitwarden
- **Extensible**: New modules and integrations can be added without modifying core
- **Self-improving**: The system monitors quality trends and triggers refactoring before drift accumulates

## Tony-reserved actions (never autonomous)

The following are permanently reserved for Tony's explicit approval and are never executed autonomously:

- Changing `FINAL_OUTPUT_PRODUCT.md`
- Issuing or revoking privileged credentials
- Financial transactions of any kind
- Sending external communications to real people (email, SMS, WhatsApp to contacts)
- Any irreversible external-world action without a rollback path
- Redefining the product goal

All other delivery work is within the autonomous operating envelope of the AI employee team.
