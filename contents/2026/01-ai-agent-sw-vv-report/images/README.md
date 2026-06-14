# Presentation Images

This directory contains image prompts and generated image assets for `../index.md`.

The goal is to keep presentation visuals consistent, inspectable, and reproducible. Each image should have a clear slide purpose, a saved generation prompt, and a stable output file name used by the presentation.

## Directory Convention

Each image has its own directory.

```text
images/<image-title>/
├── prompt.md
├── cover.png
└── variants/
```

Use kebab-case for `<image-title>`.

Examples:

- `scattered-documents`
- `why-existing-approach-is-hard`
- `source-of-truth-context`
- `agent-document-drafting`
- `ct-analysis-workstation`

## Prompt File

Each `prompt.md` should include:

- Purpose
- Slide usage
- Prompt
- Negative prompt
- Style constraints
- Output requirements

## Asset Naming

Use `cover.png` as the primary asset referenced from `index.md`.

Optional variants can be stored in `variants/` with short descriptive names.

```text
variants/
├── v1.png
├── v2.png
└── monochrome.png
```

## Shared Style

The presentation should feel professional, structured, and suitable for regulatory software engineering.

Prefer:

- clean editorial presentation visuals
- structured diagrams and document-system imagery
- subtle medical software context when relevant
- minimal or no embedded text
- 16:9 composition
- readable hierarchy

Avoid:

- stock-photo cliches
- fake readable UI text
- dramatic sci-fi styling
- excessive glow
- brand logos
- cartoonish medical devices
- cluttered dashboards

## Prompt Template

```md
# <Image Title>

## Purpose

Describe what message this image supports.

## Slide Usage

Used in: `../index.md`, slide `<slide title>`

## Prompt

...

## Negative Prompt

Avoid stock-photo cliches, unreadable text, fake UI labels, excessive glow, cartoonish medical devices, and dramatic sci-fi styling.

## Style Constraints

- Clean editorial presentation style
- Professional regulatory / software engineering tone
- Minimal text inside the image
- No brand logos
- 16:9 aspect ratio

## Output

Primary asset: `cover.png`
```
