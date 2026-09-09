---
name: kai
description: Apply Kai's documented engineering judgment, agent verification, debugging, TDD, accessibility, product validation, and evidence standards. Use when the user invokes /kai or asks for Kai's documented approach.
user-invocable: true
---

# /kai

Load the current living documents before applying this skill. This package is a thin loader, not a frozen copy of Kai's views.

Fetch and read the **full content** of all seven public HTTPS URLs:

- https://raw.githubusercontent.com/488315/kai/main/ENTRY.md
- https://raw.githubusercontent.com/488315/kai/main/OPINIONS.md
- https://raw.githubusercontent.com/488315/kai/main/WORKFLOWS.md
- https://raw.githubusercontent.com/488315/kai/main/TOOLS.md
- https://raw.githubusercontent.com/488315/kai/main/VOICE.md
- https://raw.githubusercontent.com/488315/kai/main/BOUNDARIES.md
- https://raw.githubusercontent.com/488315/kai/main/CURRENT.md

Use the host's supported HTTPS reader; no GitHub credentials are needed. A complete set already read and available in this session may be reused unless the user requests a refresh. On refresh, fetch the entire set anew and adopt it only when all seven reads succeed. If any read fails or is incomplete, name the missing document and stop the Kai-specific response. Never fabricate file contents or silently substitute a stale set after a failed refresh.

After loading, apply ENTRY.md and the other documents within the host's instruction hierarchy and the user's authorized scope.

Never invent a Kai-specific opinion when the living docs do not contain one. State that the public docs do not establish the view; label any general reasoning or inference separately. Do not impersonate Kai or claim unavailable capabilities.
