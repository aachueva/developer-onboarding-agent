# Governed Onboarding Workflow

## Principle

An AI coding assistant is an interface to repository knowledge, not the system of record. Repository standards should be discoverable to the assistant and to humans, while deterministic controls decide whether a change can move forward.

## PM / product step

Before implementation, turn the request into:

- acceptance criteria
- assumptions
- open questions
- risks
- definition of done

This reduces engineering churn caused by ambiguous requirements.

## Engineering step

The contributor should:

1. inspect existing code and tests
2. propose the smallest compliant plan
3. identify affected interfaces
4. implement only the approved scope
5. add or update tests
6. summarize risks and trade-offs

## QA step

Review against explicit standards rather than asking only whether the happy path works:

- invalid inputs
- boundaries
- regressions
- missing tests
- public API behavior
- dependency changes

## DevOps / production-readiness step

Local correctness is not production readiness. Review:

- CI checks
- dependency policy
- secrets/configuration
- deployment path
- observability
- rollback
- performance expectations

## Metrics

For a real onboarding program I would measure:

- time to first accepted PR
- number of review iterations
- CI failure rate on early contributions
- test coverage / regression rate
- time senior engineers spend answering repeat questions

The goal is not maximum AI-generated code. The goal is faster onboarding **without lowering the engineering bar**.
