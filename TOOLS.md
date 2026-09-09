# Tools

This file records tool-selection principles, not an inventory of Kai's private setup or a claim that a particular integration is connected.

| Need | Useful evidence or capability | Limit to check |
| --- | --- | --- |
| Repository review | Git state, history, and diffs | Local state may differ from the remote. |
| GitHub delivery | GitHub CLI and public APIs | Verify visibility, branch, commit, and remote files after publication. |
| Behavior checks | Focused tests through production interfaces | A passing test proves only the behavior it covers. |
| Build checks | The project's supported build tools | Compilation does not establish runtime correctness. |
| Runtime diagnosis | Reproduction, logs, and direct observation | Synthetic fixtures may not reproduce the real environment. |
| Accessibility review | Automated checks plus task-level interaction | Scores can miss barriers and user consequences. |
| Agent assistance | Bounded tasks and reviewable outputs | An agent's report is not independent verification. |

Prefer supported/public interfaces, inspectable outputs, privacy, and local control. Avoid fragile hidden shortcuts and duplicated durable state. Choose tools for the task rather than treating a favorite tool as a requirement.

The Skills CLI install command is documented in README. It installs a loader; the host must supply public HTTPS reading and any other capabilities needed for the user's task. Never claim access to files, browsers, repositories, or services merely because a tool is named here.
