[English](README.md) | 한국어

# claude-skills

kybeen0521 의 Claude Code 스킬 모음이다. 스킬마다 별도 플러그인으로 한 마켓플레이스에 들어 있어, 필요한 것만 골라 설치한다.

| 플러그인 | 하는 일 |
|---|---|
| [report-format](plugins/report-format) | A4 한글 기술 보고서를 일정한 형식의 Word(.docx)로 만들고 미리보기와 자동 점검을 한다. |
| [english-writing](plugins/english-writing) | 한국어 화자가 쓰는 영문의 작성·윤문 규칙과 검토 절차. 직역 수동태·쉼표 남발을 줄이고, 같은 것은 같은 말로, 한 번에 이해되는 문장으로 쓰며 내용은 바꾸지 않는다. |

## 설치

Claude Code 대화창에서:

```
/plugin marketplace add kybeen0521/claude-skills
/plugin install report-format@claude-skills
/plugin install english-writing@claude-skills
```

셸에서(VS Code 확장 등 `/plugin` 을 쓸 수 없는 환경):

```
claude plugin marketplace add kybeen0521/claude-skills
claude plugin install report-format@claude-skills
claude plugin install english-writing@claude-skills
```

설치 후 Claude Code 세션을 새로 열면 스킬이 잡힌다.

### 갱신·삭제

```
claude plugin marketplace update claude-skills
claude plugin update <플러그인>@claude-skills
claude plugin uninstall <플러그인>@claude-skills
```

## 구성

```
.claude-plugin/marketplace.json        플러그인 목록
plugins/<플러그인>/.claude-plugin/plugin.json
plugins/<플러그인>/skills/<스킬>/SKILL.md
```

스킬을 더하려면 같은 구성으로 `plugins/<이름>/` 을 만들고 `marketplace.json` 에 한 항목을 넣는다.
