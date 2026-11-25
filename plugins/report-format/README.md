English | [한국어](README.ko.md)

# report-format

A Claude Code skill that produces Korean A4 technical reports as Word (.docx) files in a fixed layout. If you need a PDF, open the .docx in Word and use "Save as PDF".

The skill writes the report in Korean and follows a fixed structure: a key-results box first, then data, method, results, and validation. It also enforces content rules: captions are a single title line, there are no callout boxes, and the body covers only what you asked for and the evidence behind it.

## Installation

### Option 1. In the Claude Code terminal (chat prompt)

```
/plugin marketplace add kybeen0521/claude-skills
/plugin install report-format@claude-skills
```

### Option 2. From a shell (VS Code extension, or anywhere `/plugin` is unavailable)

In the VS Code extension chat, `/plugin` fails with "isn't available in this environment". Run these in any terminal instead:

```
claude plugin marketplace add kybeen0521/claude-skills
claude plugin install report-format@claude-skills
```

Start a new Claude Code session (including VS Code windows) after installing so the skill is picked up.

### Update and uninstall

```
claude plugin marketplace update claude-skills
claude plugin update report-format@claude-skills
claude plugin uninstall report-format@claude-skills
```

### First run: environment setup

Installs python-docx, plus the approximate-preview tools (typst and a Korean font) for PCs without Word. Ask Claude to "set up the report environment", or run:

```
python3 <install dir>/skills/report-format/scripts/report_kit.py setup
python3 <install dir>/skills/report-format/scripts/report_kit.py doctor --build
```

## Usage

Ask something like "write this up as a report" (or in Korean, "이 결과를 보고서로 정리해줘"). The skill loads, writes a markdown manuscript, builds the `.docx`, and checks the result against page previews.

## Requirements

- Python 3
- pip package `python-docx` (installed by setup)
- Optional: `matplotlib` (figure scripts), `Pillow` (figure margin trimming, previews), `PyMuPDF` (previews), `typst` (approximate preview)
- Word preview: Microsoft Word (Windows, or Windows Word from WSL) or LibreOffice. Without either, a typst approximation is used

## Layout

```
(repository root) .claude-plugin/marketplace.json   marketplace definition
.claude-plugin/plugin.json        plugin definition
skills/report-format/
  SKILL.md                        procedure, content-scope rules, review checklist
  references/rules.md             format (part F) and writing (part W) rules
  scripts/report_kit.py           builder (markdown to docx, preview, checks)
  examples/                       example manuscript and figure script
```
