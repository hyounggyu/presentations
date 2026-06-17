# V&V Records and Context Materials

## Purpose

Explain the two core information classes used by the presentation: `Context Materials` and `V&V Records`. The image should help an audience unfamiliar with both terms understand that Context Materials are concrete supporting material, while V&V Records are reusable canonical data used across multiple SW V&V documents.

## Slide Usage

Used in: `../index.md`, slide `핵심 설계`

## Prompt

A 16:9 hand-drawn whiteboard style concept illustration, halfway between a rough workshop sketch and a clean explanatory diagram. Create a side-by-side comparison with two large areas separated by a subtle neutral vertical boundary line, not a workflow arrow. The boundary should only help distinguish the two conceptual areas; it should not feel like a warning, conflict, or conversion step.

Left area label: "Context Materials". Add a smaller subtitle: "supporting material / 근거 자료". Show concrete supporting materials gathered loosely: existing documents, regulatory guidance, submission templates, meeting notes, review comments, and working notes. Represent them as document cards, sticky notes, comment bubbles, checklists, and guide pages. The left side should feel like useful evidence and reference material for writing and judgment, but not canonical data.

Right area label: "V&V Records". Add a small note: "reusable canonical data". Show a structured, tidy source of reusable canonical data using organized cards, table rows, or a central data store. Include compact example cards or rows for requirements, architecture, detailed design, risk controls, tests, AI models, datasets, performance metrics, and documents.

Make the key V&V Records idea visually obvious: one Record Item card labeled "SR-004" should branch out with clean lines to several regulatory document outputs labeled "SRS", "Architecture Design", "Test Documents", and "SW V&V Report". This should communicate that one source is reused in many places.

The image should emphasize the two meanings without dramatizing their relationship: Context Materials are supporting material for interpretation; V&V Records are the stable reusable reference used to generate or maintain documents. Keep text minimal, large, and readable. Use black pen lines with muted accent colors; blue accents for reusable Records connections. Use a light gray or very soft neutral divider between the two areas. Professional regulatory software documentation tone.

## Negative Prompt

Do not show a workflow from Context Materials to Review to V&V Records. Do not include "Review / Interpretation", "Candidate", "Human approval", or a third major box. Do not include a not-equal sign, conflict symbol, warning symbol, red divider, red center mark, or any symbol implying opposition between Context Materials and V&V Records. Do not use visible labels "SWVNV", "Source of Truth", "SoT YAML", "related_sot", or "sot/". Avoid long paragraphs, fake UI screens, sci-fi interfaces, glowing holograms, polished stock infographic style, brand logos, dense tiny text, and abstract context clouds with no concrete documents.

## Style Constraints

- 16:9 aspect ratio
- Hand-drawn whiteboard style, but clean and readable
- Side-by-side concept comparison, not a process flow
- Subtle neutral boundary line only; no not-equal sign
- Minimal embedded text
- Use `V&V Records` as the main right-side label
- `Context Materials` may include the subtitle `supporting material / 근거 자료`
- Candidate must not appear as a main information class

## Output

Primary asset: `cover.png`
