# Developer Onboarding Agent

A governed engineering-onboarding prototype for helping a new developer move from an ambiguous request to a safe first contribution without bypassing normal engineering controls.

The project uses a small OpenCV-style Python wrapper as the stand-in codebase. **The image-processing functions are not the product; the onboarding workflow is.**

## Problem

New engineers often learn repository conventions through scattered documentation, Slack messages, senior engineers, old pull requests, and late review feedback. AI coding tools can make implementation faster, but without repository context and deterministic checks they can also make incorrect contributions faster.

I framed the success metric as **time to first safe PR**, not raw code-generation speed.

## Approach

The repository makes engineering expectations explicit across the delivery lifecycle:

```text
Ambiguous request
      |
      v
Acceptance criteria / assumptions
      |
      v
Engineering plan
      |
      v
Implementation + tests
      |
      v
QA / edge-case review
      |
      v
CI readiness
      |
      v
Pull request + human review
```

The workflow is designed for multiple roles rather than only the developer:

- **PM:** clarify requirements, assumptions, risks, and definition of done
- **Engineer:** plan before editing, follow repository conventions, implement and test
- **QA:** identify missing edge cases and regression risks
- **DevOps:** assess CI/deployment readiness and production gaps

## Engineering controls

AI guidance is not treated as enforcement. Hard controls remain deterministic:

- linting and formatting
- pytest test suite
- coverage threshold
- dependency policy
- pull-request review
- CI
- branch protection in a production repository

The original implementation reached **11 passing pytest cases** with Ruff checks passing. This public version is a generalized portfolio project and contains no interview prompt or private company material.

## Repository structure

```text
src/                  small image-processing wrapper
 tests/                deterministic behavior and validation tests
 docs/                 contribution, testing, role and CI guidance
 .github/workflows/    automated quality gates
```

## Why OpenCV?

OpenCV provides deterministic operations with obvious inputs, outputs, and edge cases. That keeps the demo focused on onboarding and governance rather than domain complexity. The repository does not reproduce OpenCV; it exposes a small internal wrapper around `opencv-python`.

## What I learned

The most useful pattern was **repo-centric context**: rules, docs, code patterns, tests, and CI together gave the AI assistant a much better chance of producing a compliant change. Just as importantly, generated changes still had to pass the same deterministic gates as human-written code.

## What I would add in production

- protected branches and required checks
- Jira / issue-tracker integration
- stale-document detection
- stronger dependency controls
- reusable role/task entry points
- onboarding analytics: time to first PR, review iterations, CI failure rate
- evaluation of assistant suggestions against historical accepted PRs

## Portfolio context

I built this to explore how AI coding tools can accelerate onboarding **without replacing engineering judgment or governance**. It demonstrates the level of hands-on coding fluency I use in customer-facing technical work: understanding a codebase, defining guardrails, debugging setup and import issues, validating changes, and reasoning about the path from local code to production.

— Anastasia Chueva
