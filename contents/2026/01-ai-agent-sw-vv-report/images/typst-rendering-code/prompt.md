# Typst Rendering Code

## Purpose

Show a concrete Typst code example that reads YAML V&V Records and renders document tables and traceability sections.

## Prompt

Create a 16:9 hand-drawn whiteboard style slide image. Show a close-up of a Typst code snippet in the center, with two small side panels.

Left panel: "V&V Records YAML" with a small file labeled "requirements.yaml" and rows "SR-001", "SR-004", "risk", "test".
Center panel: "Typst code" with readable pseudo-code:
`yaml("records/requirements.yaml")`
`requirements-table(...)`
`requirement-traceability(...)`
Right panel: "Rendered section" showing a requirements table and traceability table.

Add a short arrow label: "read once -> render many sections". Keep the image focused on the idea that the document renders V&V Records instead of copy-pasting them.

## Negative Prompt

Do not include dense unreadable code, fake IDE chrome, Microsoft Word, automatic approval, sci-fi UI, or final submission stamps.

## Output

Primary asset: `cover.png`
