# Handoff Template: Data Specialist

## Objective

Request data model, schema migration, or data exposure review for a change that affects database structure, data access patterns, or data retention.

## Routing Reason

Sparky has identified a data surface in this work item that requires specialist evaluation. Data model changes, schema migrations, and data exposure modifications require independent data specialist review before the review gate can be satisfied.

## Current State

<!-- Fill in:
- Work item ID and title
- Risk classification: medium | high | critical
- Data surface affected: schema | migration | query | ORM | data-access-policy | data-exposure | retention | other
- Current trust level
-->

## Evidence Attached

<!-- List all attached artifacts:
- Code diff (commit hash and PR link)
- Schema migration scripts
- Affected table/collection names
- Data volume estimates (if migration affects large datasets)
- Rollback script (if migration is reversible)
-->

## Specific Data Questions

<!-- Be specific:
- Is the migration reversible? If not, what is the recovery path?
- Does the schema change break backward compatibility with any existing consumers?
- Does the change affect any PII, financial, or health data?
- Are there performance implications (index changes, query plan changes) for production data volumes?
- Does the change expose new data to actors who should not have access?
-->

## Known Risk Signals

<!-- List what Sparky observed:
- Schema changes (added/removed/modified columns, tables, collections)
- Migration scripts
- Changes to ORM models or data access layers
- Queries that now access new data
- Changes to data retention or deletion logic
-->

## What Data Specialist Must Return

1. **Migration safety assessment:** is the migration safe to run on production data? reversible?
2. **Backward compatibility:** does this break any existing consumer?
3. **Data exposure evaluation:** does this change expose data it should not?
4. **Performance impact:** any known risk at production data volumes?
5. **Rollback plan:** is a data-level rollback possible? What does it look like?
6. **Decision:** ALLOW | BLOCK | ESCALATE with full rationale

## Return Condition to Sparky

Return when all six items are produced.
Sparky will use this as T6/T7 evidence for the review and merge gate evaluation.
