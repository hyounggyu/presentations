# 인허가 문서 작성 AI Agent 설계: V&V Records와 Context Materials 구조

부제: software verification and validation 문서 예제에서 인허가 문서 AI Assistant reference implementation으로

## 발표 목적

이 발표는 인허가 문서 작성을 단순한 문장 생성 문제가 아니라, 반복 관리 기록과 근거 자료를 함께 관리해야 하는 구조적 작업으로 정의한다.

AI를 인허가 문서 작성에 제대로 활용하려면 두 정보 층을 구분해야 한다.

- software lifecycle 산출물과 V&V evidence를 일관되게 생성, 확인, 추적하는 기준 기록인 V&V Records
- 문서 작성과 판단에 필요한 기존 문서, 가이드, 회의록, 리뷰, 메모 같은 Context Materials

이 프로젝트는 SoT라는 일반 개념을 의료기기 소프트웨어 verification/validation documentation 도메인에서는 V&V Records로 구체화해 실행해 보는 reference implementation이다. 현재 CT Analysis Workstation 문서 패키지는 전체 프로젝트의 목적이 아니라 첫 번째 포함 예제다.

## 핵심 메시지

인허가 문서 작성의 병목은 문장을 처음부터 쓰는 일이 아니라, 여러 문서에 반복되는 정보와 그 정보의 근거를 일관되게 유지하는 일이다.

AI Agent는 문서를 대신 승인하는 주체가 아니다. AI Agent는 V&V Records와 Context Materials를 구분해 읽고, 문서 작성, 검토, 누락 탐지, 불일치 확인, Records 변경 가능성 발견을 돕는 협업자다.

## 문제 정의

IEC 62304 기반 소프트웨어 lifecycle 산출물과 V&V evidence 문서에는 요구사항, 설계, 위험 통제, 테스트, AI model metadata, dataset, performance metric, traceability matrix가 반복적으로 등장한다.

요구사항 하나가 추가되면 관련 설계 항목, 위험 통제, 테스트 케이스, 보고서 요약, 추적성 표가 함께 바뀐다. 또한 실제 작성 과정에서는 기존 문서, 회의록, 리뷰 코멘트, 내부 작성 가이드, 규제 지침, 테스트 로그 같은 자료가 계속 참고된다.

문제는 이 자료들이 모두 같은 성격의 정보가 아니라는 점이다.

- 요구사항 ID, 테스트 케이스, 위험 통제 항목은 canonical data로 관리되어야 한다.
- 회의록, 리뷰 코멘트, 기존 문서 표현은 판단의 근거지만 바로 canonical data가 되지는 않는다.

둘이 섞이면 AI가 어떤 정보를 기준으로 문서를 수정해야 하는지 불분명해지고, 리뷰어가 생성된 문장의 근거를 추적하기 어렵다.

## 핵심 설계: V&V Records와 Context Materials

이 프로젝트는 인허가 문서 작성을 위한 기본 정보를 두 종류로 나눈다.

```text
records/
  software lifecycle 산출물과 V&V evidence를 일관되게 생성, 확인, 추적하는 기준 기록

contexts/registry.yaml
  문서 작성과 판단에 필요한 Context Materials 색인

optional findings / open questions
  사용자가 요청할 때만 남기는 파생 검토 산출물
```

V&V Records는 software lifecycle 산출물과 V&V evidence를 일관되게 생성, 확인, 추적하기 위해 여러 문서에서 반복 사용되는 기준 데이터다. 요구사항, 아키텍처, 상세 설계, 위험 통제, 테스트, AI model metadata, dataset, performance metric, document metadata 같은 Record Item을 포함한다.

Context Materials는 문서 작성과 판단에 필요한 근거다. 예를 들어 기존 문서, 가이드 문서, 법령/고시/지침, 회의록, 리뷰 코멘트, 제출 템플릿, 작업 메모가 여기에 속한다. Registry에는 `source_path`, `authority`, `related_records`, `summary`를 남긴다.

Finding이나 open question은 V&V Records, Context Materials와 같은 핵심 정보 분류가 아니다. AI Agent가 Context Materials를 읽고 Records 변경 가능성을 발견했을 때 먼저 남기는 검토 대기 산출물이며, 사람이 승인하기 전까지 canonical Records는 변경되지 않는다.

## AI Agent의 문서 작성 방식

AI Agent는 V&V Records와 Context Materials를 구분해 읽고 문서 수정안을 만든다. V&V Records는 여러 문서에 반복 사용되는 기준 데이터이므로 AI Agent가 작동시키는 스크립트를 통해 문서에 그대로 탑재한다. AI Agent는 Records를 임의로 재작성하지 않고, 문서 생성/수정 스크립트와 context 기반 작성 보조를 관리한다. Context Materials는 문서 작성과 판단을 돕는 근거 자료로, 설명 보완, 배경과 rationale 작성, 리뷰 코멘트 반영, 표현 개선에 사용된다. 모든 문서 수정안은 사람이 검토한 뒤 완성된다.

## AI Agent를 사용하면 무엇이 달라지는가

예전에도 사람은 기준 기록과 근거 자료를 가지고 있었다. V&V Records에 해당하는 정보는 Excel, 표, 기존 문서 안의 반복 문장으로 관리됐고, Context Materials는 책자, PDF, 회의록, 리뷰 파일, 작업 메모로 존재했다. 달라진 점은 이 자료를 AI Agent가 읽고, 찾고, 검증하고, 문서에 반영할 수 있는 형식으로 입력한다는 것이다.

이 변화의 핵심은 AI가 판단을 대체하는 것이 아니다. 사람이 이미 갖고 있던 기준 정보와 근거 자료를 agent-readable한 구조로 바꿔, AI Agent가 관련 자료를 찾고, 문서 초안을 만들고, 불일치와 누락을 검토할 수 있게 하는 것이다.

## 현재 구현의 핵심 구조

현재 공개 구현은 V&V Records를 YAML로 만들고, Context Materials를 registry로 관리하며, Typst와 script로 문서 생성과 검증을 자동화한다.

```text
records/              YAML V&V Records
contexts/registry.yaml Context Materials metadata and related records
documents/            Typst document entrypoints
shared/               reusable Typst renderers and templates
scripts/              validation, traceability, document build automation
.agents/skills/       AI agent operating rules
workbooks/            human review/edit surface
```

V&V Records YAML에는 requirements, architecture, detailed design, tests, risk controls, AI models, datasets, performance metrics, documents가 들어간다. Context registry에는 기존 문서, 가이드, 리뷰 노트, working note 같은 자료의 `id`, `type`, `source_path`, `authority`, `related_records`, `summary`가 들어간다.

Script는 `validate`, `trace`, `build`를 수행한다. 즉, Records와 context metadata가 깨지지 않았는지 확인하고, traceability를 점검하고, Typst 문서를 PDF로 빌드한다.

## 사람용 Workbook, Agent용 YAML

YAML은 AI Agent와 script가 읽기 좋은 canonical source지만, 모든 실무자가 YAML을 직접 편집하기 편한 것은 아니다. 그래서 공개 구현에는 V&V Records Workbook workflow가 들어간다.

`records/*.yaml`에서 `workbooks/vnv-records.xlsx`를 export하고, 사람이 Excel에서 검토하거나 편집한 뒤, 먼저 dry-run import로 변경 가능성을 확인한다. 그 다음 validation과 traceability check를 통과한 변경만 canonical `records/*.yaml`에 반영한다.

이 구조는 Git-native source와 사람 친화적인 review surface를 함께 제공한다. Excel은 검토와 편집 표면이고, YAML은 AI Agent와 자동화 script가 읽는 기준 데이터다.

## 문서 작성은 Typst로 한다

이 구현은 문서 작성 형식으로 Typst를 사용한다. Typst는 Markdown처럼 텍스트 기반으로 읽기 쉽지만, PDF 조판, 표, 반복 섹션, 함수와 템플릿 구성에 강하다. 특히 YAML 데이터를 직접 읽어 문서에 렌더링할 수 있어 V&V Records를 문서에 복사해 붙이는 대신 기준 데이터를 문서에 재현 가능하게 탑재할 수 있다.

예를 들어 `document-data.typ`는 다음처럼 V&V Records YAML을 읽는다.

```typst
#let requirement-data = yaml("records/requirements.yaml")
#let requirements() = requirement-data.requirements
```

그리고 SRS 문서는 다음처럼 renderer를 호출한다.

```typst
#requirements-table(requirements())
#requirement-traceability(requirements())
```

이 구조에서는 문서 안에 흩어진 문장이 기준 데이터의 원본이 아니다. 기준 데이터의 원본은 `records/*.yaml`이고, Typst 문서는 그 데이터를 읽어 문서 표와 traceability section으로 렌더링한다.

## Agent Skills

AI Agent가 V&V Records와 Context Materials의 경계를 지키며 작업하도록 이 repository에는 agent skill을 둔다.

- Guide / Context skills는 시작점 안내, context add/retrieval, Context Materials에서 Records 변경 가능성을 찾는 findings workflow를 담당한다.
- Records / Workbook skills는 V&V Records validation, traceability check, Excel workbook export/import workflow를 담당한다.
- Document / Dev skills는 drafting, consistency review, Typst/Python/Git 운영 규칙을 담당한다.

Skill의 역할은 AI에게 "무엇을 할 수 있는지"만 알려주는 것이 아니라 "무엇을 하면 안 되는지"도 고정하는 것이다. AI Agent는 Context Materials에서 V&V Records 변경 가능성을 발견할 수 있지만, 이를 자동으로 Records에 반영하지 않는다. 먼저 finding 또는 open question으로 보고하고, 사람이 승인한 뒤 별도 Records 변경으로 반영한다.

## CT Analysis Workstation 예제

기본 예제는 CT DICOM import, image viewing, ROI/HU measurement, assistive AI segmentation overlay, measurement report export를 다루는 가상 독립형 소프트웨어다. AI segmentation output은 보조 기능이며 자동 진단이 아니다.

이 예제는 다음 8개의 software lifecycle and V&V evidence 문서를 생성한다.

- Software Development Plan
- Software Requirements Specification
- Software Architecture Design
- Software Detailed Design
- Unit Test
- Integration Test
- System Test
- Software Verification and Validation Report

## 책임 경계

AI Agent가 도울 수 있는 일은 관련 V&V Records 항목 찾기, 관련 Context Materials 찾기, 문서 초안 작성, traceability gap 후보 탐지, review comment 반영 여부 점검, context 기반 Records 변경 가능성 발견과 질문 정리, 변경 영향 요약이다.

사람이 직접 판단해야 하는 일은 요구사항이 실제 제품 의도와 맞는지, 위험 통제가 충분한지, verification 방법이 적절한지, validation과 intended use 판단이 타당한지, 테스트 결과가 승인 가능한지, context 기반 변경 가능성을 V&V Records 변경으로 승인할지, 문서가 제출 가능한 품질인지다.

## 결론

AI를 인허가 문서 작성에 제대로 활용하려면, 사람이 이미 가진 자료를 AI Agent가 읽을 수 있는 구조로 바꿔야 한다.

V&V Records는 반복 정보의 기준을 제공하고, Context Materials는 작성과 판단의 근거를 제공한다. Typst와 script는 기준 데이터를 문서에 재현 가능하게 탑재한다. Agent Skills와 Workbook workflow는 AI가 경계를 지키고 사람이 검토 가능한 방식으로 작업하도록 만든다.

이 프로젝트는 이 원칙을 작은 예제, 검증 가능한 데이터, 재현 가능한 문서 빌드, 명시적인 AGENTS.md와 skills로 보여주는 reference implementation이다.
