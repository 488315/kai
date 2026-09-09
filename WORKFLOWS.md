# Workflows

## Verify an AI coding agent

1. Establish the requested behavior and acceptance criteria.
2. Inspect the current branch, commit, working tree, applicable instructions, and relevant production interfaces.
3. Review the diff for scope, ownership, lifecycle, failure handling, and unrelated changes.
4. Run checks that exercise the changed behavior. Record the command, configuration, result, and limits.
5. Verify runtime or user-facing behavior when the claim depends on it.
6. Report each delivery stage separately. Identify remaining requirements instead of declaring blanket completion.

Preserve unrelated staged, unstaged, and untracked work. Do not force-push or rewrite unrelated history. A passing test suite is evidence to interpret, not permission to ignore a visible defect.

## Debug

Reproduce the observable failure. Capture fresh evidence, narrow the failing boundary, and form one testable hypothesis. Use the smallest diagnostic step that distinguishes competing explanations. Fix the cause through the existing owner, rerun the reproduction, and check nearby failure paths. If reproduction is unavailable, label the diagnosis as provisional.

## TDD

Start with a concrete observable behavior and a failing test for the right reason. Implement the smallest change that passes through the production interface, then refactor while preserving behavior. Include rejection and recovery where they matter. Avoid tests that merely assert internal call structure, duplicate the implementation, or weaken requirements to obtain green results.

## Accessibility

Define the user's task and the consequence of failure. Check relevant keyboard, focus, assistive-technology, visual, and error-recovery behavior. Use automated metrics to locate potential problems, then verify whether people can complete the task. Report the actual barrier and test conditions; do not equate a score with universal accessibility.

## Product validation

State who has the problem, what they do today, and what behavior would indicate demand. Choose a small test before substantial implementation. Set continue, adjust, and stop criteria in advance. Observe behavior such as repeated use or a concrete commitment, interpreted in context. Record contrary evidence as carefully as encouraging evidence. Compliments alone do not establish demand.

## Tool choice

Confirm the capability is actually available. Prefer a supported API or CLI when it fits; use UI interaction when the task requires it. Bound the operation, inspect its result, and retain an appropriate recovery route. If the needed capability fails or is absent, state the blocker rather than simulate success.
