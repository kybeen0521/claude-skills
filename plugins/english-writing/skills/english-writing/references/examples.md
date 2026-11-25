# 예문

실제 기술 발표 자료(영문 슬라이드)를 윤문하며 나온 사례를, 문장 틀은 그대로 두고 수치·설비 정보를 일반화한 것이다. 분야가 달라도 틀은 같다.

## 규칙 1. 수동태

| 원문 (직역) | 고친 문장 | 세운 주어 |
|---|---|---|
| Step 1: each curve is read at the target pressure, which gives the training points. | Step 1: Reading each curve at the target pressure gives the training points. | 동명사 |
| Step 2: the flow and the power are each modeled over the input space by Gaussian process regression. | Step 2: Gaussian process regression models the flow and the power separately over the input space. | 방법 |
| One test point is removed, its curve is re-read ..., and the model is rebuilt .... The prediction is compared with the measurement, for all 30 points. | Each iteration removes one test point and re-reads its curve .... It then rebuilds the model and compares the prediction at that point with the measurement. | 회차 |
| The outlet pressure is set by the process. | The process sets the outlet pressure. | 물리 원인 |
| Along this line the same flow is delivered by a lower speed ... | Along this line the pump delivers the same flow either at a lower speed ... | 장치 |

수동태로 둔 것(능동이 더 어색함):
- "the flow was varied with the outlet valve and 5 to 8 points were measured" (밸브를 행위자로 세우면 어색)
- "The acceptance test was run at the rated pressure" ("took place at a pressure" 는 연어 오류)
- "so that the operating points can be compared" ("allows a comparison of" 는 명사화로 더 딱딱)
- "The efficiency is computed from the predicted flow and power rather than modeled separately." (대비가 수동에서 더 자연스러움)

## 규칙 2. 직역 틀

| 원문 | 고친 문장 |
|---|---|
| The speed and the vane angle are what the control manipulates. | The process sets the outlet pressure, and the controller adjusts the speed and the vane angle. |
| The objective is a procedure for constructing ... | The objective is to establish a procedure for constructing ... |
| The scope is the construction of the map. ... is outside it. | This study covers only the construction of the map. ... is outside its scope. |
| ... requires a set of curves over both inputs, that is, a performance map. | ... requires a performance map, a set of curves over both inputs. |
| The map is defined on this plane for this reason. | This is why the map is defined on this plane. |
| Those of flow occur on the low-speed curves. | The maximum flow errors occur on the low-speed curves. |

## 규칙 3. 같은 것은 같은 말로

| 문제 | 정리 |
|---|---|
| "index" 가 성능 지표(performance index)와 오차 지표 두 뜻 | 오차 쪽을 "error metric" |
| "target" 이 목표 압력과 모델 출력(Target (model)) 두 뜻 | 모델 쪽을 "Output (model)" |
| "test" 가 설비 시험과 검증점(test points) 두 뜻 | 검증점을 "validation points" |
| 같은 압력 수준을 mapped pressures / target pressure / test levels 로 | "target pressure" 하나로 |
| "uncertainty", "the model's own estimate", "predictive standard deviation" 혼용 | 하나로 정하고 기호와 함께 |
| "tested combinations" 와 "combinations covered by the test" | "tested combinations" |

## 규칙 4. 이해

| 원문 | 문제 | 고친 문장 |
|---|---|---|
| ..., it rises with the speed on all three planes, where the flow also rises. | where 가 planes 를 받음 | ..., both the efficiency and the flow rise with speed on all three planes. |
| Without its end point the curve no longer reaches the pressure of that plane, so the combination has no training point on that plane. | its 가 두 곡선 중 무엇인지, that plane 중복 | Each end point is the only point of its curve that reaches the plane's pressure. When it is left out, that combination has no training point on that plane. |
| They do not directly give the values over the two inputs. | the values 막연 | They do not directly give Q and W over the two inputs. |
| GPR 이 풀네임보다 먼저 나옴 | 처음 나오는 곳에서 정의되지 않음 | 처음 나오는 곳에서 "Gaussian process regression (GPR)". 그림 속 기호(η, σ)도 본문에서 먼저 정의 |

## 규칙 5. 쉼표

| 원문 | 고친 문장 |
|---|---|
| ... follows the demand, so it mostly runs at part load, where it uses more power per unit of air. | ... follows demand. It therefore runs mostly at part load and uses more power per unit of air. |
| ... drops because the speed, and hence the work input, stays fixed. | ... drops because a fixed speed also fixes the work input. |
| The single largest value, 12.5 %, is at the low-speed, high-angle corner ..., where there is no training point. | The largest value (12.5 %) is at the low-speed, high-angle corner ..., where there is no training point. |
| On each plane, two independent models ... / Without data, the band is wide. | On each plane two independent models ... / Without data the band is wide. |

쉼표를 줄이다 생긴 실수(되돌릴 것):
- "..., on the 8 bar plane, which has no training point" → which 가 plane 을 받아 틀린 뜻이 됨. "..., where there is no training point" 로.
- "At the tested combinations leave-one-out cross-validation over 30 points gives ..." → 머리 구가 길면 쉼표를 남긴다.

## 규칙 7. 내용 불변 (수정안에서 실제로 걸러 낸 것)

| 수정안 | 문제 |
|---|---|
| GPR requires only a small number of training points | "only" 로 주장이 커짐 → "GPR handles a small number of training points" |
| On a conventional flow-pressure map | "conventional" 주장 추가 → 원문 구조 유지 |
| σ, which comes from the model itself | 다른 곳에서 구어라고 고친 "comes from" 을 새로 씀(자기 모순) |
| The procedure offers a method for ... | 절차가 방법을 제공하는 순환 표현 → 원래 문장으로 |
| The acceptance test ... took place at the rated pressure | 연어 오류 → 원래 문장으로 |

## 규칙 8. 형식

| 원문 | 고친 문장 |
|---|---|
| Step 1: reading ... / Step 2: Gaussian ... / Step 3: the ... | Step 1: Reading ... / Step 2: Gaussian ... / Step 3: The ... (쌍점 뒤 완전한 문장은 대문자, 같은 틀끼리 맞춤) |
| 0.94 % 가 줄 끝에서 "0.94" / "%" 로 갈라짐 | 숫자와 단위 사이 U+00A0 |
