# V&V Records Workbook

## Purpose

Show why the public SWVNV implementation uses an Excel workbook as a human review/edit surface while keeping `records/*.yaml` as the canonical machine source for agents and scripts.

## Slide Usage

Used in: `../index.md`, slide `사람용 Workbook, Agent용 YAML`

## Prompt

Create a 16:9 hand-drawn whiteboard style workflow diagram for a regulatory software documentation presentation. Show a clean left-to-right loop:

1. "records/*.yaml" with blue structured file cards and a small tag "canonical machine source"
2. "Export Workbook" with an arrow to an Excel-like sheet
3. "Human Review / Edit" with a person and checklist
4. "Dry-run Import" with a cautious inspection icon
5. "Validation + Traceability" with checkmarks and linked Record Item IDs
6. "Records Update" returning to the YAML cards

Make the central Excel-like sheet labeled "workbooks/vnv-records.xlsx" and add a small tag "human review/edit surface". Use a circular or gently bent workflow so it fits comfortably in 16:9. Keep labels large and sparse.

Main message: Excel is the practical human interface, YAML remains the agent-readable canonical source, and validation/traceability gates protect the update.

## Negative Prompt

Do not show Excel as the canonical source. Do not show automatic approval, direct unreviewed update arrows, submission stamps, sci-fi dashboards, glowing UI, dense tables with tiny text, or brand logos.

## Style Constraints

- 16:9 aspect ratio
- Hand-drawn whiteboard style, clean and readable
- Muted blue for YAML records, subtle yellow for workbook, green for validation
- Minimal embedded text
- Professional regulatory software documentation tone

## Output

Primary asset: `cover.png`
