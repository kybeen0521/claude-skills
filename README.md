English | [한국어](README.ko.md)

# claude-skills

A collection of Claude Code skills by kybeen0521. Each skill is a separate plugin in one marketplace, so you can install only the ones you need.

| Plugin | What it does |
|---|---|
| [report-format](plugins/report-format) | Builds Korean A4 technical reports as Word (.docx) files in a fixed layout, with preview and automatic checks. |
| [english-writing](plugins/english-writing) | Rules and a review procedure for English written by Korean speakers: fewer translated passives and commas, one word for one thing, sentences readers understand at first reading, and no change to the content. |

## Installation

In the Claude Code chat prompt:

```
/plugin marketplace add kybeen0521/claude-skills
/plugin install report-format@claude-skills
/plugin install english-writing@claude-skills
```

From a shell (VS Code extension, or anywhere `/plugin` is unavailable):

```
claude plugin marketplace add kybeen0521/claude-skills
claude plugin install report-format@claude-skills
claude plugin install english-writing@claude-skills
```

Start a new Claude Code session after installing so the skills are picked up.

### Update and uninstall

```
claude plugin marketplace update claude-skills
claude plugin update <plugin>@claude-skills
claude plugin uninstall <plugin>@claude-skills
```

## Layout

```
.claude-plugin/marketplace.json        list of plugins
plugins/<plugin>/.claude-plugin/plugin.json
plugins/<plugin>/skills/<skill>/SKILL.md
```

To add a skill, create `plugins/<name>/` with the same layout and add one entry to `marketplace.json`.
