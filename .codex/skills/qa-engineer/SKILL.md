---
name: qa-engineer
description: Use for pre-commit quality review of the CSV budget CLI app, focusing on tests, type hints, complexity, edge cases, and regressions.
---

# QA Engineer

Use this skill for final quality checks before commit.

## Review checklist

- Review only the changed files and directly related tests.
- Confirm tests exist for the new behavior.
- Check that type hints are present.
- Look for functions that are too long or too complex.
- Look for missing edge cases and regression risks.
- Verify the change matches the project rules in `AGENTS.md`.

## Output

- Return either explicit approval or concrete issues.
- Report concrete issues first.
- If nothing is wrong, say the change looks safe and note any residual risk.
