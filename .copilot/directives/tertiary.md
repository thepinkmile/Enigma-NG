# TERTIARY DIRECTIVE — Design Log Integrity

> ⚠️ **CRITICAL INTEGRITY VIOLATION** — Modifying an audit log entry is equivalent to falsifying a
> record. In a professional engineering context this could constitute a criminal offence.
> Commit `889cb5c` modified DEC-028 in-place. This must never recur.

The Design Log is `design/Design_Log/` — a directory of per-DEC files.

⛔ **NEVER modify any existing `design/Design_Log/DEC-NNN_*.md` file.** They are read-only once written.

> 🔔 **Exception check required:** if a DEC was written earlier in the *current, still-open* task
> and has not yet been reviewed/approved ("sealed") by the user, ask the user first whether it is
> already approved/sealed or still open for in-place correction — do not assume either way, and do
> not create an amending DEC to fix it without asking. One clarifying question up front avoids a
> cascade of unnecessary amending-DEC churn for what may just be an in-progress draft.

## Structure

- `design/Design_Log/index.md` — index table (ID, title, date, status, summary)
- `design/Design_Log/DEC-NNN_{kebab-case-title}.md` — one file per decision

## Rules

- New decisions → create new `DEC-NNN_{kebab-title}.md` **and** add a row to `index.md`.
- Changes to a prior decision → new DEC entry with `Amends: DEC-NNN` or `Supersedes: DEC-NNN`.
- Changes to a decision written earlier in the same still-open task → ask the user first (see
  exception check above) before choosing between an in-place fix and a new amending DEC.
- **Next entry: DEC-108** → file `design/Design_Log/DEC-108_{kebab-title}.md`.
- This rule applies to all agents and orchestrating sessions equally.
