# 발표 Transcription

## 1. 왜 기존 방식이 힘든가

먼저, 왜 기존 방식이 힘든지부터 보겠습니다. 인허가 문서 작성은 단순히 문장을 잘 쓰는 문제가 아닙니다. 요구사항, 설계, 위험 통제, 테스트, 보고서 요약처럼 같은 정보가 여러 문서에 반복해서 등장합니다. 여기에 규제 가이드, 회의록, 리뷰 코멘트, 테스트 로그 같은 참고 자료도 계속 들어옵니다. 문제는 기준 데이터와 참고 근거가 섞이면 사람도 AI도 무엇을 기준으로 문서를 고쳐야 하는지 판단하기 어려워진다는 점입니다.

## 2. 핵심 설계

그래서 이 발표에서는 정보를 두 가지로 나눕니다. Source of Truth, 즉 SoT는 여러 문서에 반복 사용되는 기준 데이터입니다. 요구사항, 아키텍처, 상세 설계, 위험 통제, 테스트, AI 모델, 데이터셋 같은 항목이 여기에 들어갑니다. Context는 문서 작성과 판단에 필요한 근거입니다. 기존 문서, 규제 지침, 제출 템플릿, 회의록, 리뷰 코멘트가 여기에 속합니다. Context는 중요하지만 곧바로 canonical truth가 되지는 않습니다.

## 3. AI Agent의 문서 작성 방식

AI Agent의 역할은 SoT를 직접 재작성하는 것이 아닙니다. 기준 데이터는 스크립트를 통해 문서에 그대로 탑재되고, AI Agent는 그 스크립트를 작동시키면서 Context를 활용해 문서 초안과 수정안을 만듭니다. 예를 들어 설명을 보완하거나, 리뷰 코멘트를 반영했는지 확인하거나, 문장의 흐름을 다듬는 일을 도울 수 있습니다. 최종 판단과 승인은 여전히 사람이 합니다.

## 4. AI Agent를 사용하면 무엇이 달라지는가

여기서 핵심은 SoT와 Context라는 개념이 완전히 새로 생긴 것이 아니라는 점입니다. 예전에도 사람은 SoT를 엑셀, 표, 기존 문서 안의 반복 문장으로 관리했고, Context는 책자, PDF, 회의록, 리뷰 파일, 작업 메모로 가지고 있었습니다. 달라진 점은 이 자료를 AI Agent가 읽고 추적할 수 있는 형식으로 입력한다는 것입니다. AI가 판단을 대체하는 것이 아니라, 사람이 가진 자료 구조를 agent-readable하게 만드는 것입니다.

## 5. 현재 구현의 핵심 구조

현재 구현은 이 아이디어를 작은 파일 기반 reference implementation으로 보여줍니다. SoT는 YAML로 관리합니다. requirements, architecture, tests, risk controls, AI models 같은 기준 데이터가 여기에 들어갑니다. Context는 registry로 관리합니다. MFDS 가이드, 기존 문서, 리뷰 노트, 작업 메모 같은 자료는 source path, authority, related SoT, summary와 함께 색인화됩니다. Typst는 YAML SoT를 문서로 렌더링하고, script는 validate, trace, build를 담당합니다.

## 6. 문서 작성은 Typst로 한다

문서 작성에는 Typst를 사용합니다. Typst는 Markdown처럼 텍스트 기반으로 읽기 쉽지만, PDF 조판, 표, 반복 섹션, 템플릿 구성에 강합니다. 특히 YAML 데이터를 읽어 문서에 렌더링할 수 있습니다. 그래서 Word 문서에 정보를 반복해서 복사해 넣는 방식보다, 기준 데이터를 재사용하고 일관성을 유지하기 쉽습니다.

## 7. Typst에서 SoT를 렌더링한다

구체적으로 보면 Typst는 requirements.yaml 같은 SoT 파일을 읽고, 그 데이터를 요구사항 표와 traceability section으로 렌더링합니다. 문서 안의 표는 사람이 손으로 복사해 붙인 결과가 아니라, SoT YAML에서 생성된 표현입니다. 이 구조에서는 기준 데이터의 원본이 문서가 아니라 YAML에 남고, 문서는 그 기준 데이터를 반복 가능하게 보여주는 산출물이 됩니다.

## 8. Agent Skills

AI Agent가 이 구조를 안정적으로 사용하려면 작업 방식도 고정해야 합니다. 그래서 repository에는 SWVNV 전용 agent skill을 둡니다. Context retrieval은 SoT 항목과 관련된 근거 자료를 찾습니다. Document drafting은 SoT를 기준으로, Context를 근거로 초안과 수정안을 만듭니다. Consistency review는 SoT, Context, draft 문서 사이의 불일치와 누락을 찾습니다. PDF reader는 MFDS PDF context에서 필요한 페이지만 찾아 확인합니다.

## 9. CT Analysis Workstation 예제

기본 예제는 CT Analysis Workstation입니다. CT DICOM import, image viewing, ROI와 HU measurement, AI segmentation overlay, measurement report export를 다루는 가상의 독립형 소프트웨어입니다. 여기서 AI segmentation은 보조 기능이며 자동 진단이 아닙니다. 이 예제는 Software Plan, SRS, Architecture, Detailed Design, 여러 테스트 문서, 그리고 SW V and V Report를 포함한 문서 패키지를 생성합니다.

## 10. Findings And Open Questions

Context에서 SoT 변경 가능성이 발견될 수는 있습니다. 예를 들어 규제 가이드나 리뷰 코멘트에서 현재 SoT에 없는 요구사항 가능성이 보일 수 있습니다. 하지만 AI Agent는 이를 자동으로 SoT에 반영하지 않습니다. 먼저 finding 또는 open question으로 보고하고, 사용자가 명시적으로 요청할 때만 별도 후보 기록을 만들며, 사람이 승인한 뒤에만 SoT 변경으로 반영합니다.

## 11. 책임 경계

책임 경계도 중요합니다. AI Agent는 관련 SoT와 Context를 찾고, 문서 수정안을 만들고, traceability gap과 open question을 정리할 수 있습니다. 하지만 제품 의도, 위험 통제의 충분성, 검증 방법의 타당성, SoT 변경 승인, 제출 가능한 품질에 대한 최종 판단은 사람이 해야 합니다. 이 경계가 분명해야 AI를 실무에 안전하게 넣을 수 있습니다.

## 12. 제품화 가능성 탐색

제품화 가능성을 보면, 현재 구현은 reference implementation이지만 몇 가지 제품 단위로 분리할 수 있습니다. Repository template, SoT와 Context authoring tool, 규제 context ingestion, Typst 기반 문서 생성 서비스, AI review assistant가 그 예입니다. 즉 이 프로젝트는 하나의 완성된 제품이라기보다, 어떤 기능 단위가 제품화될 수 있는지 탐색하는 구조입니다.

## 13. 포지션

SWVNV의 포지션은 ALM, eQMS, RIM을 정면으로 대체하는 것이 아닙니다. 오히려 이 시스템들과 연결될 수 있는 reasoning and document authoring layer에 가깝습니다. SoT와 Context를 agent-readable하게 구성하고, 문서 초안과 review finding을 만들어, 기존 시스템 사이에서 인허가 문서 작성과 검토를 돕는 역할을 목표로 합니다.

## 14. 결론

정리하면, AI를 인허가 문서 작성에 제대로 활용하려면 사람이 이미 가진 자료를 AI Agent가 읽을 수 있는 구조로 바꿔야 합니다. SoT는 반복 정보의 기준을 제공하고, Context는 작성과 판단의 근거를 제공합니다. Typst와 script는 기준 데이터를 문서에 재현 가능하게 탑재하고, Agent Skills는 AI가 이 경계를 지키며 작업하도록 만듭니다. SWVNV는 이 원칙을 작은 예제로 실험하는 reference implementation입니다.
