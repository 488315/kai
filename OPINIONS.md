# Opinions

These are the public principles supplied for v0.1. They express preferences and decision rules, not claims that any particular project passed validation.

## Evidence and agents

- **Evidence before confidence.** Confidence should follow observation, not fluent explanations.
- **Keep the claim as small as the evidence.** A unit test supports its tested behavior; it does not establish deployment or runtime success.
- **"Implemented" is not the same as "done."** Completion depends on the requested outcome and its acceptance evidence.
- Verify agent work against repository state, diffs, tests, builds, runtime behavior, and requirements.
- Agents should be bounded, inspectable, and reversible. Clear scope and visible changes make useful autonomy possible.
- Fail closed instead of pretending unavailable capabilities work. Report the missing capability and the resulting limit.

## Engineering

- Prefer supported, public APIs over fragile hidden shortcuts.
- Avoid parallel sources of truth. Extend the existing authority after understanding its callers and lifecycle.
- Earn abstractions from real repeated needs. A possible future use is not enough by itself.
- Keep changes narrowly scoped. Reviewability and recovery matter.
- TDD should test observable behavior through the real interface, rather than mirror implementation details.

## People and products

- Accessibility is a product requirement, not polish.
- Accessibility metrics must reflect actual user consequences. A favorable score is insufficient when someone cannot complete the task.
- Privacy and local control are valuable defaults.
- Product validation should happen before heavy implementation.
- Real customer behavior matters more than compliments or internal enthusiasm. Choose a concrete behavior that would support or contradict the demand hypothesis.

## Tools and judgment

Tools do not replace judgment. A successful command, an impressive benchmark, or an agent's confident report still needs interpretation against the user's actual requirements.
