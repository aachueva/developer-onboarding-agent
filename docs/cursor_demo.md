# Cursor Demo Workflow

Open this repository in Cursor. The `.cursor/rules/governed-onboarding.mdc` rule is version-controlled with the project so the assistant receives the same contribution expectations as a new engineer.

## Demo 1 — Turn ambiguity into a plan

Ask Cursor:

> Add a `rotate_image` function to this wrapper. Before editing, inspect the repo and give me acceptance criteria, assumptions, affected files, and a minimal implementation plan.

What to look for:

- Does it inspect existing validation and test patterns?
- Does it avoid unnecessary dependencies?
- Does it identify source, exports, and tests that need to change?
- Does it wait for a reviewable plan rather than immediately editing everything?

## Demo 2 — Implement with tests

After reviewing the plan, ask Cursor to implement it and add tests consistent with the repository standards.

Then run:

```bash
ruff check src tests
ruff format --check src tests
pytest --cov=src --cov-report=term-missing --cov-fail-under=90
```

The point is not that Cursor can write `rotate_image`. The point is that repository context plus deterministic gates make an AI-assisted contribution easier to review and safer to merge.

## Demo 3 — QA review

Ask Cursor to review the diff as QA and identify missing invalid-input, boundary, and regression cases without changing code.

## Demo 4 — Production readiness

Ask Cursor to assess whether the local change is sufficient for production. A good answer should distinguish passing local tests from concerns such as CI, branch protection, dependency policy, performance, observability, and deployment controls.
