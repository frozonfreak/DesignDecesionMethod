# Design Decision Method

## What is it?

Design Decision Method is a reusable workflow for people and AI agents to decide what information a screen needs, how to organize it, and which interactions and visual direction fit the project. It draws on established guidance. It does not create another UI library or visual standard.

## What does it solve?

It addresses repeated UI guesswork: starting from generic layouts, overlooking essential information, adding unnecessary complexity, and revisiting the same decisions across projects. It makes consequential choices explicit before building.

## Why do we need it?

For our work, it carries the same design philosophy across products and agents: simple to understand, informative enough to decide, and efficient to use. It reduces the need to explain that philosophy from scratch each time. Whether it actually saves time still needs measurement. It is useful as a shared procedure, and it is not mandatory for every small edit.

## How is it different from WebHIG?

| Design Decision Method | WebHIG |
|---|---|
| Decides how this particular experience should work | Defines applicable interface quality requirements |
| Chooses information hierarchy, layouts and flows | Governs accessibility, consistency, responsiveness, performance and motion |
| Records why a choice fits the audience and task | Provides requirements and checks for its implementation |

The two stay separate. This repository does not copy WebHIG requirements into a second standard. When a project has no interface guidelines, the method uses WCAG 2.2 AA for web, or the relevant native guidance, and records any other requirements that were not specified.

These four points are also published as a page from the `docs/` folder: https://frozonfreak.github.io/DesignDecesionMethod/

The agent procedure routes UI work across OOUX, GOV.UK, Carbon, Material 3, platform guidelines, and a project's own rules. When relationships shape structure, it requires a short object map and decision record before layout, and it ends with an honest validation status. It does not rank those sources, copy their branding, or claim research or compliance it has not done. This README is for people. The agent reads `SKILL.md`.

Current release: 2.2.4.

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
├── LICENSE                           MIT License
└── README.md
```

## Install

The skill follows the open Agent Skills format. Copy the whole folder, keeping the name `design-decision-method`, into your agent's skills directory. The `name` in `SKILL.md` must match that directory name. Paths below were checked on 2026-10-05 against the cited docs. They can change, so confirm them again before relying on them.

| Agent | Where to put `design-decision-method/` | Verification |
|---|---|---|
| Claude Code | `.claude/skills/` in the project, or `~/.claude/skills/` for yourself | Checked [Claude Code skills](https://code.claude.com/docs/en/skills.md) |
| Cursor | `.cursor/skills/` or `.agents/skills/` in the project, or the same two paths under your user home | Checked [Cursor skills](https://cursor.com/docs/skills) |
| Gemini CLI | `.gemini/skills/` or `.agents/skills/` in the project, or `~/.gemini/skills/` or `~/.agents/skills/` | Checked [Gemini CLI skills](https://geminicli.com/docs/cli/skills.md) |
| Codex | `.agents/skills/` in the repository, from the working directory up to the repo root | Project path checked on [Codex skills](https://developers.openai.com/codex/skills). Personal directory: not verified |
| Others | Confirm in that host's own docs | not verified |

**Claude.ai.** Not verified against Claude.ai documentation in this release. The `.skill` export is a zip of this same folder for hosts that import a skill archive.

**Agents without skill support.** Paste the body of `SKILL.md` into your rules or instructions file (for example `AGENTS.md`), and keep `references/` and `assets/` in the repository so the paths resolve. A short pointer in persistent memory can remind an agent to load the skill, but it cannot replace the files:

> Load the full Design Decision Method and its relevant references before UI/UX work. Establish audience, purpose, frequency, error consequences, and platform; apply the conditional object-map gate before layout; record consequential choices; apply project guidelines or disclose the fallback; validate purpose-specific outcomes and label tested versus untested results. Apply AI checks only to AI-enabled features.

## Release and integrity

`release-manifest.json` lists a SHA-256 for every file except itself, plus a canonical checksum over the sorted relative paths and exact file bytes (path, NUL byte, bytes, NUL byte). Matching hashes show that two copies have identical content. They do not show authenticity, freshness, or design quality. Different zip exports can contain the same files and still differ as archives.

- Copies installed in other hosts do not update when you change one copy, and no update service is configured.
- When delegating to another agent, give it the same release, the project brief, and the relevant evidence.
- Any content change needs a new version in `SKILL.md` metadata, the manifest, and the changelog.
- There is no automated freshness service. Re-check a source when you rely on it, and record what you actually opened.

## Check it

The Agent Skills specification documents this format check, for a folder named `design-decision-method`. It was not run for this release. A narrower host validator must not be used to reject portable fields such as `compatibility` and `metadata`.

```
skills-ref validate ./design-decision-method
```

`evals/evals.json` holds ten prompts. Give the performing agent only the `prompt` field. Do not include `expected_output` or `expectations`; those are grader-only. Run each prompt in a separate context. For a with-method and without-method comparison, use the same brief, model, and tools, and save the outputs. Case 10, "Design a logo for my bakery.", is an automatic-trigger test: do not mention this method in that prompt. This checks whether the method stays unused for a standalone logo. It does not measure usability or time saved.

These cases have not been run for 2.2.1, so nothing here is benchmarked. A package check cannot show whether an object map happened before layout, or whether a task is usable. Report proposed, heuristic, automated, manual, and user-research evidence separately.

From the repository root, after Python 3 is available:

```
python scripts/validate_release.py
python scripts/test_integrity.py
python scripts/package_release.py
```

`validate_release.py` checks YAML and JSON structure, version agreement, evaluation ids and fields, local references, manifest coverage, file hashes, and the canonical checksum. `test_integrity.py` repeats that check, then confirms a missing file and an altered file are rejected. `package_release.py` writes `dist/design-decision-method.zip` and `dist/design-decision-method.skill`, each with the enclosing `design-decision-method/` folder. The export contains the skill files listed above. Repository scripts, CI, and ignore rules stay in git and are not part of the skill package. On Windows, `py -3` works in place of `python`.

## Keeping it current

Design systems change. Re-check the snapshot in `references/visual-systems.md` against the exact source URL, and record the publication date, last-update date, access date, available version, reviewed scope, and verification status. Use "not stated" or "not verified" when that is the honest value. Update `metadata.updated` and regenerate the manifest. Do not treat a landing-page check as pattern verification.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
