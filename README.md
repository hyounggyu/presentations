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
.agents/
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

Draft segment-based narration from a legacy `slides[].text` file:

```sh
uv run python .agents/skills/hg-presentation/scripts/segment_narration.py contents/2026/01-ai-agent-sw-vv-report --dry-run
uv run python .agents/skills/hg-presentation/scripts/segment_narration.py contents/2026/01-ai-agent-sw-vv-report
```

Validate a presentation without requiring API credentials:

```sh
uv run python .agents/skills/hg-presentation/scripts/validate_project.py contents/2026/01-ai-agent-sw-vv-report --skip-api-key
```

Regenerate the timeline from existing audio:

```sh
uv run python .agents/skills/hg-presentation/scripts/build_timeline.py contents/2026/01-ai-agent-sw-vv-report
```

Generate YouTube subtitles and transcript:

```sh
uv run python .agents/skills/hg-presentation/scripts/generate_subtitles.py contents/2026/01-ai-agent-sw-vv-report
```

Check the full plan without calling ElevenLabs:

```sh
uv run python .agents/skills/hg-presentation/scripts/run_pipeline.py contents/2026/01-ai-agent-sw-vv-report --dry-run
```

Render the final MP4 from existing slide images and audio:

```sh
uv run python .agents/skills/hg-presentation/scripts/render_video.py contents/2026/01-ai-agent-sw-vv-report --overwrite
```

`narration.json` uses ElevenLabs v3 and `slides[].segments[]`. Each segment may include inline audio tags such as `[calm]`, `[thoughtful]`, or `[slight emphasis]`, plus `pause_after_ms` for presentation breathing room. Generated segment audio stays under ignored `build/voiceover/audio/`; the reusable source is `narration.json`.
