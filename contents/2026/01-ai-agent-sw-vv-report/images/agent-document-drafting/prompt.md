# Agent Document Drafting

## Purpose

Show how an AI Agent uses V&V Records and Context Materials differently when drafting regulatory document changes. This image should bridge the concept explanation page and the later workflow pages without introducing Records change candidates yet.

## Slide Usage

Used in: `../index.md`, slide `AI Agent의 문서 작성 방식`

## Prompt

A 16:9 hand-drawn whiteboard style workflow illustration, clean and readable. Show how V&V Records and Context Materials are used differently when an AI Agent creates a document draft. The key message is that the AI Agent does not rewrite Records; instead, the AI Agent operates a gear-shaped Script that mounts canonical Records data into the document draft.

Top-left input: "V&V Records". Draw it as structured data cards, a table, or a small repository box. Include compact examples such as requirements, tests, risk controls, and AI model metadata. Draw a clear arrow from V&V Records to a central gear-shaped node labeled "Script", then from Script to "Document Draft". Label the Records-to-Script arrow "canonical data" and label the Script-to-Document Draft arrow "그대로 탑재". The visual must communicate that Records data is mounted into the document without arbitrary modification.

Bottom-left input: "Context Materials". Draw it as concrete supporting material: document cards, review comments, meeting notes, regulatory guidance, and working notes. The arrow from Context Materials should be labeled "supporting material / 작성 근거" and should communicate that context supports explanation, rationale, review comment handling, and wording improvements.

Draw a friendly, simple node labeled "AI Agent" near the gear-shaped Script. Show the AI Agent operating or managing the gear with a small lever, hand, button, or dashed control line labeled "operates script". Do not draw a direct Records-to-AI-Agent arrow. Draw the Context Materials arrow into the AI Agent, then an arrow from AI Agent to "Document Draft" labeled "drafting support / 작성 보조". The draft should look like a marked-up regulatory document, not an approved final submission. From Document Draft, draw a final arrow to "Human Review", represented by a person, checklist, or review marker.

The image should emphasize that Script carries V&V Records into the draft as canonical data, while AI Agent uses Context Materials for writing support and operates the Script. Human review completes the document after the draft. Keep the flow simple and left-to-right. Use black pen lines, muted accent colors, blue for Records data flow, green or gray for Context Materials support, and neutral colors for Human Review. Do not add a bottom explanation box, legend paragraph, caption panel, or any long sentence block; the diagram should rely on labels and arrows only.

## Negative Prompt

Do not include "Candidate", "Records Change Candidate", "Context to Records", a Context-to-Records update arrow, a direct "Records -> AI Agent" arrow, automatic approval, final submission stamp, "Approved", "Final Document", or any visual suggesting that AI modifies Records or replaces human judgment. Do not use visible labels "SWVNV", "Source of Truth", "SoT YAML", "related_sot", or "sot/". Avoid sci-fi UI, glowing holograms, dense tiny text, long paragraphs, bottom explanatory text boxes, caption panels, brand logos, and complex multi-step workflow details.

## Style Constraints

- 16:9 aspect ratio
- Hand-drawn whiteboard style matching the other presentation images
- Simple left-to-right flow
- Show V&V Records and Context Materials as different input roles
- Show Script as a gear-shaped mechanism operated by AI Agent
- V&V Records must flow through Script before reaching the document
- Context Materials must flow through AI Agent before reaching the document
- Output must be `Document Draft` or `Document Change Proposal`, not final approved document
- Human Review must appear after the draft

## Output

Primary asset: `cover.png`
