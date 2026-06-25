---
name: csv-budget-cli
description: Use for the CSV-based Python CLI budget app in this repository, especially when planning, implementing, or reviewing TDD-driven ledger features.
---

# CSV Budget CLI

Use this skill when working on the budgetApp repository.

## Core workflow

- Read `AGENTS.md` before changing code.
- Follow TDD: write the test first, then implement the smallest passing change.
- Keep functions small and typed.
- Prefer simple CSV-centric designs that are easy to test.

## Validation

- Run `pytest` after each meaningful change.
- Check complexity with `radon cc`.
- If a change is ready to commit, ask the `qa_engineer` sub-agent to review quality first.

## Good defaults

- Use plain data structures for transactions unless a stronger abstraction is clearly needed.
- Preserve compatibility with the sample CSV files in `data/`.
