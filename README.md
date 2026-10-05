# Design Decision Method

An agent skill that makes design decisions explicit before a screen is drawn or coded. It routes UI work across OOUX, GOV.UK, Carbon, Material 3, platform guidelines, and a project's own rules. When relationships shape structure, it requires a short object map and decision record before layout, and it ends with an honest validation status.

It does not invent a visual system, rank the sources, copy their branding, or claim research or compliance it has not done. This README is for people. The agent reads `SKILL.md`.

## Contents

```
design-decision-method/
├── SKILL.md                          core procedure
├── references/
│   ├── modern-design.md              purpose-based presentation, specialist extension
│   ├── routing.md                    which guidance for which problem
│   ├── visual-systems.md             currency snapshot and adoption checks
│   ├── accessibility.md              WCAG 2.2 AA baseline and checks
│   ├── ai-interfaces.md              only for AI-enabled features
│   ├── acceptance-and-validation.md  criteria format and evidence levels
│   └── sources.md                    lookup routes and verification
├── assets/design-record-template.md  object map and decision record
├── evals/evals.json                  test prompts
├── agents/openai.yaml                optional metadata for hosts that read it
├── release-manifest.json             file hashes
├── CHANGELOG.md
└── README.md
```

## Install

The skill follows the open Agent Skills format. Copy the whole folder, keeping the name `design-decision-method`, into your agent's skills directory.

| Agent | Project directory | Personal directory |
|---|---|---|
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |
| Codex | `.agents/skills/` | `~/.agents/skills/` |
| Gemini CLI | `.gemini/skills/` (also reads `.agents/skills/`) | `~/.gemini/skills/` |
| Cursor | `.cursor/skills/` | `~/.cursor/skills/` |
| Others | Often `.agents/skills/` | |

These paths come from third-party documentation and change between releases, so confirm them against your agent's own docs.

**Claude.ai.** Upload the `.skill` file, which is this same folder as a zip.

**Agents without skill support.** Paste the body of `SKILL.md` into your rules or instructions file (for example `AGENTS.md`), and keep `references/` and `assets/` in the repository so the paths resolve. A short pointer in persistent memory can remind an agent to load the skill, but it cannot replace the files:

> Load the full Design Decision Method and its relevant references before UI/UX work. Establish audience, purpose, frequency, error consequences, and platform; apply the conditional object-map gate before layout; record consequential choices; apply project guidelines or disclose the fallback; validate purpose-specific outcomes and label tested versus untested results. Apply AI checks only to AI-enabled features.

## Release and integrity

`release-manifest.json` lists a SHA-256 for every file except itself, plus a canonical checksum over the sorted relative paths and exact file bytes (path, NUL byte, bytes, NUL byte). Matching hashes show that two copies have identical content. They do not show authenticity, freshness, or design quality. Different zip exports can contain the same files and still differ as archives.

- Copies installed in other hosts do not update when you change one copy, and no update service is configured.
- When delegating to another agent, give it the same release, the project brief, and the relevant evidence.
- Any content change needs a new version in `SKILL.md` metadata, the manifest, and the changelog.

## Check it

Validate the format with the reference validator from the Agent Skills project:

```
skills-ref validate ./design-decision-method
```

`evals/evals.json` holds ten prompts, one of which is a negative-trigger case (a logo request should not use the skill). Run each prompt in a separate context with and without the skill, using the same brief and model, then check the expectations and note failures. This measures process, not usability. The prompts have not been run, so nothing here is benchmarked.

## Keeping it current

Design systems change. Re-check the snapshot in `references/visual-systems.md` against the sources in `references/sources.md`, update `metadata.updated`, and regenerate the manifest.
