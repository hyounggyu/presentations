---
title: "인허가 문서 작성 AI Agent 설계: V&V Records와 Context Materials 구조를 통한 사업화 가능성 탐색"
subtitle: SW V&V 예제에서 인허가 문서 AI Assistant reference implementation으로
date: 2026-05-31
---

# 인허가 문서 작성 AI Agent 설계: V&V Records와 Context Materials 구조를 통한 사업화 가능성 탐색

## 왜 기존 방식이 힘든가

반복 정보가 여러 문서에 흩어지고, 근거와 리뷰가 여러 채널에서 들어온다.

![Why existing approach is hard](images/why-existing-approach-is-hard/cover.png)

### 변경은 한 곳에서 끝나지 않는다

요구사항 하나가 추가되면 관련 항목이 함께 흔들린다.

- 설계
- 위험 통제
- 테스트
- 보고서 요약
- 추적성 표

### 실제 작성 환경

작성자는 문서만 보는 것이 아니다.

- 기존 문서
- 규제 가이드
- 회의록
- 리뷰 코멘트
- 내부 작성 가이드
- 테스트 로그
- 작업 메모

### 섞이면 어려워지는 것

반복 정보와 참고 근거가 섞이면 AI도 사람도 판단하기 어렵다.

- 무엇이 canonical data인가?
- 무엇이 참고 context인가?
- 어떤 변경 제안을 검토 대기 산출물로 남겨야 하는가?
- 생성 문장의 근거를 어떻게 추적할 것인가?

---

## 핵심 설계

인허가 문서 작성을 위한 정보를 두 가지로 나눈다.

![V&V Records and Context Materials](images/source-of-truth-context/cover.png)

### V&V Records

SoT 개념을 SW V&V 도메인에서는 V&V Records로 구체화한다.

- requirements
- architecture
- detailed design
- risk controls
- tests
- AI models
- datasets
- performance metrics
- documents

### Context Materials

Context Materials는 문서 작성과 판단에 필요한 근거다.

- 기존 문서
- 규제 지침
- 제출 템플릿
- 회의록
- 리뷰 코멘트
- 작업 메모

`source_path`, `authority`, `related_records`, `summary`로 색인화한다.

---

## AI Agent의 문서 작성 방식

AI Agent는 V&V Records를 직접 재작성하지 않고, 스크립트와 Context Materials를 사용해 문서 수정안을 만든다.

![AI Agent document drafting](images/agent-document-drafting/cover.png)

- V&V Records -> Script -> Document
  기준 데이터는 AI Agent가 작동시키는 스크립트를 통해 문서에 그대로 탑재한다.

- Context Materials -> AI Agent -> Document
  근거, 설명, 리뷰 반영, 표현 개선에 사용한다.

- Human Review
  모든 문서 수정안은 사람이 검토한 뒤 완성된다.

---

## AI Agent를 사용하면 무엇이 달라지는가

예전에도 사람은 기준 기록과 근거 자료를 가지고 있었다.

![Agent readable change](images/agent-readable-change/cover.png)

- Before
  Excel, 책자, PDF, 회의록, 리뷰 파일, 작업 메모가 사람 머릿속에서 연결됐다.

- After
  V&V Records와 Context Materials를 AI Agent가 읽고 추적할 수 있는 형식으로 입력한다.

- 핵심 변화
  AI가 판단을 대체하는 것이 아니라, 사람이 가진 자료 구조를 agent-readable하게 만든다.

---

## 현재 구현의 핵심 구조

V&V Records는 YAML로 만들고, Context Materials는 registry로 관리한다.

![Current implementation structure](images/current-implementation-structure/cover.png)

- `records/`
  canonical machine source: requirements, architecture, tests, risk controls, AI models

- `contexts/registry.yaml`
  source_path, authority, related_records, summary

- `documents/`, `shared/`, `scripts/`, `.agents/skills/`, `workbooks/`
  render, validate, trace, build, review workflow를 담당한다.

---

## 사람용 Workbook, Agent용 YAML

YAML만으로는 실무자 접근성이 낮다. Excel workbook round-trip이 제품화 포인트가 된다.

![V&V Records Workbook](images/vnv-records-workbook/cover.png)

```text
records/*.yaml -> export workbook -> human review/edit
-> dry-run import -> validation/traceability -> records update
```

- `workbooks/vnv-records.xlsx`
  사람이 검토하고 편집하는 표면

- `records/*.yaml`
  AI Agent와 script가 읽는 canonical source

---

## 문서 작성은 Typst로 한다

Typst는 Markdown처럼 읽기 쉽지만, 조판과 데이터 렌더링에 강하다.

![Typst YAML rendering](images/typst-yaml-rendering/cover.png)

- Markdown과 비슷한 텍스트 기반 문법
- PDF 조판, 표, 반복 섹션 구성에 적합
- YAML V&V Records를 문서에 탑재

---

## Typst에서 V&V Records를 렌더링한다

V&V Records를 복사해 붙이는 대신 Typst가 YAML을 읽어 문서 표와 traceability 섹션을 만든다.

![Typst rendering code](images/typst-rendering-code/cover.png)

```typst
#let requirement-data = yaml("records/requirements.yaml")
#let requirements() = requirement-data.requirements

#requirements-table(requirements())
#requirement-traceability(requirements())
```

기준 데이터의 원본은 문서가 아니라 `records/*.yaml`에 있다.

---

## Agent Skills

AI Agent가 V&V Records와 Context Materials의 경계를 지키며 작업하도록 skill을 둔다.

![Agent skills](images/agent-skills/cover.png)

- Guide / Context
  시작점 안내, context add/retrieval, records findings를 담당한다.

- Records / Workbook
  validation, traceability, Excel workbook round-trip을 담당한다.

- Document / Dev
  drafting, consistency review, Typst/Python/Git 운영 규칙을 담당한다.

Skill은 기능 목록이 아니라 AI가 경계를 넘지 않게 하는 운영 규칙이다.

---

## CT Analysis Workstation 예제

가상의 독립형 CT 분석 소프트웨어를 대상으로 8개의 SW V&V 문서를 생성한다.

![CT Analysis Workstation](images/ct-analysis-workstation/cover.png)

- CT DICOM import, image viewing, ROI/HU measurement
- AI segmentation overlay는 보조 기능이며 자동 진단이 아니다.
- Software Plan, SRS, Architecture, Detailed Design, Test, SW V&V Report를 생성한다.

---

## Findings And Open Questions

Context Materials에서 V&V Records 변경 가능성이 발견되면 자동 반영하지 않는다.

![Findings and open questions](images/findings-open-questions/cover.png)

- AI Agent는 finding 또는 open question으로 보고한다.
- 사용자가 명시적으로 요청할 때만 별도 후보 기록을 만든다.
- 사람이 승인한 뒤 별도 V&V Records 변경으로 반영한다.

---

## 책임 경계

AI Agent는 자료를 찾고, 초안을 만들고, 불일치와 누락을 발견한다.

![Responsibility boundary](images/responsibility-boundary/cover.png)

- AI가 돕는 일
  records/context retrieval, drafting, traceability gap review, open question 정리

- 사람이 판단하는 일
  제품 의도, 위험 통제 충분성, 검증 타당성, records 변경 승인, 제출 가능 품질

---

## 제품화 가능성 탐색

현재 구현은 reference implementation이지만, 제품화 가능한 단위가 보인다.

![Productization path](images/productization-path/cover.png)

- Repository template
- V&V Records / Context Materials authoring tool
- Controlled V&V Records Workbook
- Records validation / traceability service
- Regulatory context ingestion
- Typst document generation service
- AI review assistant

---

## 포지션

이 프로젝트는 ALM, eQMS, RIM을 정면으로 대체하지 않는다.

![Positioning layer](images/positioning-layer/cover.png)

핵심 포지션은 V&V Records와 Context Materials를 agent-readable하게 구성하는
Git-native, transparent, lightweight regulatory documentation layer다.

ALM, eQMS, RIM, structured authoring, AI-assisted regulatory writing과 연결된다.

---

## 결론

AI를 인허가 문서 작성에 제대로 활용하려면, 사람이 이미 가진 자료를 AI Agent가 읽을 수 있는 구조로 바꿔야 한다.

![Project conclusion](images/project-conclusion/cover.png)

V&V Records는 반복 정보의 기준을 제공하고, Context Materials는 작성과 판단의 근거를 제공한다.
Typst와 script는 기준 데이터를 문서에 재현 가능하게 탑재한다.
Agent Skills와 Workbook workflow는 사람이 검토 가능한 운영 표면을 만든다.
