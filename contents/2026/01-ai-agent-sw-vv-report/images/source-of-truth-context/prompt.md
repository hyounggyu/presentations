# Source of Truth and Context

## Purpose

Explain the two core information classes used by the presentation: `Context` and `Source of Truth (SoT)`. The image should help an audience unfamiliar with both terms understand that Context is concrete supporting material, while Source of Truth is reusable canonical data used across multiple regulatory documents.

## Slide Usage

Used in: `../index.md`, slide `핵심 설계`

## Prompt

A 16:9 hand-drawn whiteboard style concept illustration, halfway between a rough workshop sketch and a clean explanatory diagram. Create a side-by-side comparison with two large areas separated by a subtle neutral vertical boundary line, not a workflow arrow. The boundary should only help distinguish the two conceptual areas; it should not feel like a warning, conflict, or conversion step.

Left area label: "Context". Add a smaller subtitle: "supporting material / 맥락 자료". Show concrete supporting materials gathered loosely: existing documents, regulatory guidance, submission templates, meeting notes, review comments, and working notes. Represent them as document cards, sticky notes, comment bubbles, checklists, and guide pages. The left side should feel like useful evidence and reference material for writing and judgment, but not canonical data.

Right area label: "Source of Truth (SoT)". Keep the English term exactly. Show a structured, tidy source of reusable canonical data using organized cards, table rows, or a central data store. Include compact example cards or rows for requirements, architecture, detailed design, risk controls, tests, AI models, datasets, performance metrics, and documents.

Make the key SoT idea visually obvious: one SoT item card labeled "SR-004" should branch out with clean lines to several regulatory document outputs labeled "SRS", "Architecture Design", "Test Documents", and "SW V&V Report". This should communicate that one source is reused in many places.

The image should emphasize the two meanings without dramatizing their relationship: Context is supporting material for interpretation; Source of Truth is the stable reusable reference used to generate or maintain documents. Keep text minimal, large, and readable. Use black pen lines with muted accent colors; blue accents for reusable SoT connections. Use a light gray or very soft neutral divider between the two areas. Professional regulatory software documentation tone.

## Negative Prompt

Do not show a workflow from Context to Review to SoT. Do not include "Review / Interpretation", "Candidate", "Human approval", or a third major box. Do not include a not-equal sign, conflict symbol, warning symbol, red divider, red center mark, or any symbol implying opposition between Context and SoT. Avoid long paragraphs, fake UI screens, sci-fi interfaces, glowing holograms, polished stock infographic style, brand logos, dense tiny text, and abstract context clouds with no concrete documents.

## Style Constraints

- 16:9 aspect ratio
- Hand-drawn whiteboard style, but clean and readable
- Side-by-side concept comparison, not a process flow
- Subtle neutral boundary line only; no not-equal sign
- Minimal embedded text
- `Source of Truth (SoT)` must stay in English
- `Context` may include the subtitle `supporting material / 맥락 자료`
- Candidate must not appear as a main information class

## Output

Primary asset: `cover.png`
