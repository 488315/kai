<h1 align="center">/kai</h1>

<p align="center">
  <a href="https://agentskills.io"><img alt="Agent Skills package" src="https://img.shields.io/badge/Agent%20Skills-package-blue?style=flat-square" /></a>
  <a href="https://github.com/488315"><img alt="GitHub profile: 488315" src="https://img.shields.io/badge/GitHub-488315-181717?style=flat-square" /></a>
  <a href="https://github.com/488315/kai"><img alt="Public distillation v0.1" src="https://img.shields.io/badge/distillation-v0.1-26734D?style=flat-square" /></a>
</p>

<p align="center"><a href="https://github.com/488315">GitHub profile</a> · <a href="https://github.com/488315/kai">Repository</a> · <a href="SOURCES.md">Public sources</a></p>

<h3 align="center">Think carefully. Build narrowly. Verify the result.</h3>

<p align="center">
  <a href="https://github.com/488315"><img src="https://avatars.githubusercontent.com/u/19639817?v=4" alt="Kai's GitHub profile image" width="280" /></a>
</p>

Hi, I'm [Kai](https://github.com/488315). I care about what a system actually does, what the evidence supports, and whether the result helps the person using it.

`/kai` is a living distillation of how I make engineering decisions, verify AI coding agents, debug, use TDD, approach accessibility, evaluate products, work with tools, and communicate uncertainty. Its central rule is simple: **keep the claim as small as the evidence.**

This is a public knowledge base and an installable agent skill. It gives an agent a documented way to reason through a problem; it is not a trained model, a complete copy of me, or permission to speak on my behalf. Private context stays outside this repository.

## Quick Start

Install with the Skills CLI:

```sh
npx skills add 488315/kai -g
```

Then use it in an agent that supports skills:

```text
/kai Review this agent's changes. What is verified, and what is still unproven?
/kai Help me reproduce this bug and write a test for the observable failure.
/kai Does this accessibility metric capture an actual barrier for users?
/kai What is the smallest useful demand test before I build this product?
/kai Challenge this abstraction. Do we have repeated needs that justify it?
```

Invocation support depends on the host agent. The install command makes the skill available; it does not grant new tools or permissions.

## How It Works

The [skill](skills/kai/SKILL.md) is a thin loader. It reads the seven current living documents from public HTTPS URLs on `main`, then uses them to answer the request.

```text
Reviewed public evidence                  /kai request
          |                                    |
          v                                    v
+-------------------------+       +-------------------------+
| Review and edit the docs|       | Load seven living docs  |
| Check privacy and evals |       | from public main URLs   |
+------------+------------+       +------------+------------+
             |                                |
             v                                v
     Commit living docs              Apply ENTRY + boundaries
             |                                |
             +--------------------------------+
                              |
                              v
                  Answer with evidence limits
```

### What the skill loads

| Document | Purpose |
| --- | --- |
| [ENTRY.md](ENTRY.md) | Route the request and separate documented views from inference. |
| [OPINIONS.md](OPINIONS.md) | Durable principles and the tradeoffs behind them. |
| [WORKFLOWS.md](WORKFLOWS.md) | Engineering review, debugging, TDD, accessibility, and product validation. |
| [TOOLS.md](TOOLS.md) | Choose tools by capability, support, inspectability, and control. |
| [VOICE.md](VOICE.md) | Answer directly and make uncertainty explicit. |
| [BOUNDARIES.md](BOUNDARIES.md) | Protect privacy, respect authority, and avoid invented attribution. |
| [CURRENT.md](CURRENT.md) | State the current public scope and its limitations. |

These are living docs: editable, versioned statements of judgment. The installed loader does not freeze them inside the skill package. Public document reads need no GitHub authentication. A fully read set can be reused within a session; ask to refresh for new commits.

If any required document is unavailable or incomplete, the skill reports that limitation and stops the Kai-specific answer. If the docs contain no Kai-specific opinion, it says so. General reasoning must be labeled as such.

### How the living docs stay fresh

Updates currently happen through maintainer review and commits. There is **no scheduled refresh automation configured in this repository**. [AUTOMATION.md](AUTOMATION.md) describes the update procedure and requirements for any future automation.

New public evidence should revise the relevant existing statement, include provenance in [SOURCES.md](SOURCES.md), and pass privacy review and the behavioral cases in [evals/CASES.md](evals/CASES.md). A recent commit is evidence of an edit, not proof that every viewpoint is current.

### Public sources

- [Kai's GitHub profile](https://github.com/488315)
- [Source scope and provenance](SOURCES.md)
- Inspiration: [Kun's /kun](https://github.com/kunchenguid/kun) and [I distilled myself, and you should too](https://blog.kunchenguid.com/p/i-distilled-myself-and-you-should)

The architecture and presentation are inspired by Kun's project. Kai's principles and wording are independent; the inspiration is not evidence of Kai holding Kun's views.

## Contribution

Issues and focused pull requests for broken links, unclear instructions, and evaluation gaps are welcome. Changes to personal viewpoints require Kai's review. Please use public examples and do not include private conversations, repository contents, or sensitive information.
