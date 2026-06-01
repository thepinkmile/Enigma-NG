# SESSION_START

Bootstrap file for every new session on this repository.
Follow these steps in order before doing any other work.

---

## Step 1 — Load All Directives

1. Read `.copilot/directives/index.md`.
2. Read each directive file listed in the index (all files in `.copilot/directives/`).
3. Persist directive memories before any other work:
   - Upvote matching existing memories with `vote_memory` using exact fact text.
   - If exact-match fails (`no memory was found`), immediately create a new repository memory using
     `store_memory` with citations to the source directive file.
4. **Batch memory operations in multiple passes until complete.**
   - Do not stop after a single call if tool budget/rate limits are hit.
   - Use small batches (recommended: max 5 `vote_memory` calls per pass).
   - Repeat passes until every directive/rule below is confirmed persisted.
5. Do not proceed to Step 2 until Step 1 persistence is complete.

Minimum set to confirm loaded:

| Directive | Non-negotiable rule |
| :--- | :--- |
| PRIMARY | Never modify MPNs or supplier PNs; BOM content rules apply |
| SECONDARY | Never git commit / add / stage / unstage — ever |
| TERTIARY | `design/Design_Log/` is append-only; existing DEC files are read-only |
| QUATERNARY | Never delete files permanently; move to `.recycle-bin/` |
| SENARY | Never modify files without explicit implementation approval |
| SEPTENARY | Every sub-agent prompt must start with the mandatory preamble block |
| QUINARY | Review sub-agents are strictly read-only |
| OCTONARY | Seed session DB from `todos/todos.sql` + `todos/deps.sql` at session start |
| NONARY | KiCAD import completeness gate: all library formats must stay in sync |
| component-lookup | Local lookup order only (MD → PDF → ask user); no web search |
| document-rules | Only `Last Updated` may change; design docs contain current design only |
| character-usage | Non-ASCII requires explicit allowlist approval |
| repo-state | `.copilot/` tracking, checkpoint sequencing, and path sanitisation rules |

---

## Step 2 — Seed Session Database

Run both SQL files via the `sql` tool:

1. `.copilot/todos/todos.sql` — inserts all todos (`INSERT OR IGNORE`, idempotent)
2. `.copilot/todos/deps.sql` — inserts all dependencies (uses `PRAGMA foreign_keys = OFF/ON`)

Verify row counts match expectations before proceeding. Failure to seed is an OCTONARY violation.

---

## Step 3 — Read Current State

1. Read `.copilot/plan.md` — current workstream status, next steps, key design decisions.
2. Read `.copilot/handoff.md` (latest section first) — what was last worked on.
3. Read the latest relevant checkpoint(s) in `.copilot/checkpoints/` if additional context is needed.

---

## Checklist

- [ ] All directives loaded as standing memories
- [ ] Memory persistence completed across as many passes as required (no partial completion)
- [ ] Exact-match vote failures resolved via `store_memory` (no directive left unpersisted)
- [ ] Session DB seeded (row counts verified)
- [ ] `plan.md` read
- [ ] `handoff.md` read
