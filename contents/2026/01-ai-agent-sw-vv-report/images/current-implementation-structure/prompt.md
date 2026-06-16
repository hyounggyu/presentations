# Current Implementation Structure

## Purpose

Summarize the current public SWVNV implementation as one slide: records YAML, Context Materials registry, Typst documents, shared renderers, scripts, agent skills, and workbook review surface.

## Prompt

Create a 16:9 hand-drawn whiteboard style architecture diagram for a presentation. Use a clean hub-and-flow layout with seven labeled blocks.

Blocks:
- "records/" with small file cards: requirements, architecture, tests, risk controls, AI models; add a small tag "canonical machine source"
- "contexts/registry.yaml" with metadata tags: source_path, authority, related_records, summary
- "documents/" with document/page icons
- "shared/" with reusable renderer/template cards
- "scripts/" with a gear icon and labels: validate, trace, build
- ".agents/skills/" with small tool cards: guide, context, records, document, workbook, dev
- "workbooks/" with an Excel-like sheet icon and label: human review/edit surface

Show records flowing into Typst documents through shared renderers. Show Context Materials registry flowing into Agent Skills. Show Scripts connected to records and documents as validation/build automation. Show workbooks connected bidirectionally with records as export/import review surface. Keep the layout readable and explain the structure without long paragraphs.

Style: hand-drawn whiteboard, black marker, muted blue for records, green for Context Materials, gray/orange for scripts, light purple or neutral for Agent Skills, subtle yellow for workbook.

## Negative Prompt

Do not include complex repository trees beyond the seven named blocks, tiny code, sci-fi dashboards, glowing UI, automatic approval, "Candidate", or "Final Document". Avoid long captions and dense labels.

## Output

Primary asset: `cover.png`
