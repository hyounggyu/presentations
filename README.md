# hg-presentations

Personal presentation archive and authoring toolkit.

The repository is intentionally simple:

```text
contents/
  YYYY/
    NN-title/
      presentation.yaml
      draft.md
      slides.md
      narration.json
      transcript.md
      youtube.srt
      images/
      build/
      exports/
skills/
  hg-presentation/
```

## First Content

The first imported presentation is:

```text
contents/2026/01-ai-agent-sw-vv-report/
```

It was migrated from the sibling `hg-swvnv-private` repository.

## Common Commands

Validate a presentation without requiring API credentials:

```sh
uv run python skills/hg-presentation/scripts/validate_project.py contents/2026/01-ai-agent-sw-vv-report --skip-api-key
```

Regenerate the timeline from existing audio:

```sh
uv run python skills/hg-presentation/scripts/build_timeline.py contents/2026/01-ai-agent-sw-vv-report
```

Generate YouTube subtitles and transcript:

```sh
uv run python skills/hg-presentation/scripts/generate_subtitles.py contents/2026/01-ai-agent-sw-vv-report
```

Render the final MP4 from existing slide images and audio:

```sh
uv run python skills/hg-presentation/scripts/render_video.py contents/2026/01-ai-agent-sw-vv-report --overwrite
```
