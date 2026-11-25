---
name: english-writing
description: 영문 작성·영작·영문 윤문 규칙 스킬(모든 프로젝트 공통). 발표 자료(pptx), 논문 영문 Abstract·영문 제목·캡션, 보고서 영문, 이메일 등 영어 글을 새로 쓰거나 고치거나 검토할 때 반드시 먼저 로드한다. 트리거 - "영작", "영어로 써줘", "영문으로", "영어 표현 검토", "영문 윤문", "영어 어색한 것", "translate to English", "English polish", "proofread English", 슬라이드·Abstract 의 영어 문장 작성. 국문 직역에서 생기는 수동태·번역투·쉼표 남용을 막고, 같은 것은 같은 말로, 청중이 한 번에 이해하는 문장으로 쓰며, 내용(사실·수치·결정 사항)은 바꾸지 않는다.
metadata:
  version: "1.0"
  author: kybeen0521
  created: "2026-11-25"
---

# 영문 작성 규칙 (english-writing)

사용자는 한국어로 생각하고 쓴 내용을 영어로 옮긴다. 그래서 문제의 대부분은 문법 오류가 아니라 **국문 구조를 그대로 옮긴 흔적**이다. 목표는 원어민 수준의 화려한 문장이 아니라, **사용자와 청중(독자)이 한 번에 이해하는 자연스러운 기술 영어**다.

규칙의 근거와 예문(실제 기술 발표 자료 윤문에서 나온 사례를 일반화한 것)은 `references/examples.md` 에 있다. 처음 쓰는 글이거나 검토 범위가 넓으면 함께 읽는다.

## 우선순위

1. 이해 (한 번에 읽히는가) > 2. 자연스러움 (직역 티가 없는가) > 3. 문체 (구어·딱딱함). 2·3번에 걸려도 이해에 지장이 없으면 "낮음"으로 둔다.
2. 어떤 규칙도 **내용을 바꾸지 않는다** (규칙 7) 보다 앞서지 않는다.

## 규칙

### 1. 수동태: 직역에서 생긴 것만 능동으로
- 국문은 주어를 생략한다("각 곡선을 읽는다"). 직역하면 목적어가 주어 자리로 올라가 수동태가 된다("each curve is read"). 이런 문장은 **실제로 그 일을 하는 것을 주어로** 세운다: 방법·모델(GPR models, the map reproduces), 물리적 원인·장치(the process sets, intercooling brings, the compressor delivers), 절차의 회차(each iteration removes), 동명사(reading each curve gives).
- 기술 영어에서 수동태 자체는 정상이다. 방법 서술의 수동태가 **한 문장에 하나**이고 행위자가 중요하지 않으면 둔다("5 to 8 points were measured"). 한 문장에 수동태가 둘 이상 몰리거나 덱·문단 전체에 깔리면 고친다.
- **we 는 쓰지 않거나 최소**(결론 한 곳 정도). 대신 "This study ..." 를 한두 번까지.
- 능동이 더 어색해지면 수동으로 둔다: 무생물을 억지 행위자로 세우기(the valve varied the flow), 압력에 take place 같은 잘못된 연어, 명사화(allows a comparison of).

### 2. 국문 직역 틀을 풀어 쓴다
| 직역 틀 | 대신 |
|---|---|
| ~하여 ~를 얻는다 → ", which gives ..." 반복 | 주어를 바꿔 한 문장으로(Linear interpolation of each curve gives ...) |
| ~하는 것은 ~이다 → "X are what Y manipulates" | Y adjusts X |
| 목적은 ~이다 → "The objective is a procedure" | The objective is to establish a procedure |
| 범위는 ~이다 → "The scope is X. ... is outside it." | This study covers only X. ... is outside its scope. |
| 즉 → ", that is, X" | 동격으로(requires X, a set of ...) |
| 문장 끝에 붙인 구 → "..., for all 35 points", "... for this reason" | 문장을 나누거나 앞으로(This is why ...) |
| 하나의 → "one demand point" | a demand point (one 은 many 와 대비할 때만) |
| ~의 것 → "Those of flow" | The maximum flow errors |

### 3. 같은 것은 같은 말로
- 한 대상은 처음부터 끝까지 **한 낱말**로 부른다. 동의어로 바꿔 쓰는 "우아한 변주"는 기술 글에서 다른 대상으로 읽힌다(tested combinations / combinations covered by the shop test → 하나로).
- 한 낱말을 **두 뜻**으로 쓰지 않는다(performance index 와 error index, target pressure 와 Target (GPR), shop test 와 test points).
- 정의를 한 번 하고 나면 그 말만 쓴다. 기존 결정 용어(프로젝트 메모·결정 파일)가 있으면 그것을 따른다.
- 글을 고칠 때 새로 넣은 낱말이 이미 정한 용어 규칙을 어기지 않는지 확인한다.

### 4. 한 번에 이해되는 문장
- **한 문장에 한 가지.** 절이 셋 이상 이어지면 나눈다.
- **가리키는 말을 분명히.** its, that, those, which, it 가 둘 이상을 가리킬 수 있으면 대상을 직접 쓴다(its (N, α) → that point / the removed point's).
- **막연한 명사 금지.** the values, the combination, the same model, the control 처럼 "무엇인지" 빠진 말은 실제 대상으로(Q and W, the combination of speed and vane angle, the controller).
- **쉬운 낱말.** 같은 뜻이면 짧고 흔한 낱말.

### 5. 쉼표를 남발하지 않는다
- 짧은 머리 구(서너 단어) 뒤 쉼표는 뺀다: On each plane two GPRs ..., Along this line the compressor ..., At the tested combinations the map ...
- 끼워 넣은 구(", and hence X,", ", computed from Y,", ", set by Z,")는 문장을 다시 짜서 없앤다.
- 쉼표로 이은 절의 사슬(..., so ..., where ...)은 문장을 나눈다.
- **남기는 쉼표**: 목록(Q, W and η), 좌표·기호 묶음((x, y, Q, W)), 조합 표기(3,000 rpm, IGV 30°), 독립된 두 절 사이의 ", and / , so / , but", 빼면 잘못 읽히는 곳(In this example, speed ...), 긴 머리 구 뒤.

### 6. 문체: 구어도, 지나친 딱딱함도 피한다
- 구어 → 기술 영어: needs → requires, works with → handles, comes from → is given by / is predicted by, weak → less reliable, need a separate test → require additional tests.
- 지나친 명사화·장황함도 피한다: allows a comparison of the combinations → so that the combinations can be compared.
- 관사·수 일치·전치사: the first-order propagation → first-order error propagation, the speed and the work input stays → stay, differ between (셋 이상) → differ among, which is better (셋 이상) → best.

### 7. 내용은 바꾸지 않는다 (모든 수정안마다 확인)
- 원문에 없던 **주장을 더하지 않는다**(requires only, conventional, first, unique 등).
- 사실·수치는 원자료와 **대조**한다. 개수·범위를 다시 쓰면 검산한다.
- 이미 정한 문구·용어·범위(프로젝트의 결정 파일·작업 메모)는 건드리지 않는다. 바꿔야 할 것 같으면 제안만 한다.
- 수정안끼리 **서로 모순되지 않게** 한다(한 곳에서 구어라고 고친 말을 다른 곳에 새로 쓰지 않는다).

### 8. 형식
- 미국식 철자(-ize, -or, modeled, toward).
- em dash(—)·en dash(–) 금지, 일반 하이픈(-)만. 범위는 "to" 또는 "~"(국문 자료). 수식 편집기 안의 빼기 부호만 예외.
- 숫자와 단위 사이는 한 칸(12.5 %, 8 kgf/cm²). **슬라이드·조판물**은 줄바꿈 없는 공백(U+00A0)으로 넣어 줄 끝에서 갈라지지 않게 한다.
- 쌍점(:) 뒤가 완전한 문장이면 대문자로 시작한다(예: "Step 1: Reading each curve ..."). 목록이나 기호 대응이면 소문자 그대로. 같은 틀의 줄들은 대소문자를 맞춘다.
- 참고문헌 제목, 인용 그림의 원래 글, 고정된 제목은 고치지 않는다.

## 절차

1. **범위 확인**: 대상 파일과 글(슬라이드는 표·캡션·수식 글 상자 포함) 전부 뽑는다. 고정 대상(참고문헌, 인용 그림, 결정 문구)을 먼저 표시한다.
2. **결정 사항 읽기**: 프로젝트에 결정 파일·작업 메모·용어 규칙이 있으면 먼저 읽는다.
3. **목록 작성 (고치기 전에)**: 쪽(또는 문단)별 표로 `위치 | 현재 | 수정안 | 이유(규칙 번호) | 중요도` 를 낸다. 중요도: 높음 = 읽는 사람이 걸리거나 잘못 읽음, 중간 = 직역·비원어민 티가 분명하거나 뜻이 흐림, 낮음 = 맞는 문장을 다듬는 수준. "반영 권장"과 "선택(지금도 맞음)"을 나눈다.
4. **자기 수정안 재점검**: 수정안을 원문과 나란히 놓고 규칙 3·4·7 위반(새 용어 충돌, 새 모호함, 주장 추가, 서로 모순)과 "원문보다 나빠진 것"을 찾아 고치거나 뺀다.
5. **독립 검토 (범위가 넓거나 사용자가 "확실해?"라고 할 때)**: 내 결론을 주지 않은 검토자 한 명에게 현재 글만 주고 (a) 수동태가 자연스러운지 (b) 원어민 편집자가 짚을 문장을 심각도와 함께 묻는다. 고정 용어·철자·수치는 조건으로 알려 준다. 돌아온 지적은 그대로 옮기지 않고 사실·결정과 대조해 거른다.
6. **반영은 사용자가 고른 범위만**: 사용자가 "반영"·"전부"·번호로 정한 것만 넣는다. 수정 전 판을 백업한다.
7. **확인**: 슬라이드·조판물은 렌더해서 넘침·겹침·숫자-단위 갈라짐을 본다. 넘치면 뜻을 두고 줄 수만 맞추며 바꾼 문장을 보고한다. 산출물에서 –·— 를 grep 으로 0건 확인한다.
8. **보고**: 반영한 것, 계획과 다르게 넣은 것(이유), 넣지 않은 것을 나눠 짧게 보고한다.

## 하지 않는 것
- 원어민 수준이라고 단정하지 않는다. "규칙과 검토자 기준으로 점검했다"고 범위를 밝힌다.
- 취향 차이만 있는 표현을 목록에 올리지 않는다.
- 국문 글(대본·원고)은 이 스킬의 대상이 아니다(국문 윤문은 humanize-korean 등 별도 스킬).
