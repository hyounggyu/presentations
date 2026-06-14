---
name: hg-presentation
description: Use when creating, validating, migrating, narrating, captioning, or rendering presentations in the hg-presentations repository, especially projects under contents/YYYY/NN-title with slides.md, narration.json, images, build artifacts, and YouTube subtitles.
---

# hg-presentation

Use this skill for presentation projects in this repository.

## Project Shape

Each presentation lives under `contents/YYYY/NN-title/` and keeps source material and artifacts together:

```text
presentation.yaml
draft.md
slides.md
narration.json
transcript.md
youtube.srt
images/
build/voiceover/
exports/
```

Use `draft.md` for long-form thinking, `slides.md` for the slide structure, and `narration.json` as the executable voiceover input.

## Workflow

Run scripts with `uv run python`.

1. Validate the project:

   ```sh
   uv run python skills/hg-presentation/scripts/validate_project.py contents/YYYY/NN-title --skip-api-key
   ```

2. Generate or reuse slide audio:

   ```sh
   uv run python skills/hg-presentation/scripts/generate_audio.py contents/YYYY/NN-title
   ```

3. Build the timeline:

   ```sh
   uv run python skills/hg-presentation/scripts/build_timeline.py contents/YYYY/NN-title
   ```

4. Generate YouTube subtitles and transcript:

   ```sh
   uv run python skills/hg-presentation/scripts/generate_subtitles.py contents/YYYY/NN-title
   ```

5. Render the video:

   ```sh
   uv run python skills/hg-presentation/scripts/render_video.py contents/YYYY/NN-title --overwrite
   ```

For a no-API planning check:

```sh
uv run python skills/hg-presentation/scripts/run_pipeline.py contents/YYYY/NN-title --dry-run
```

## Notes

- Keep `timeline.json` paths relative to the presentation directory.
- Keep generated YouTube captions in `youtube.srt`.
- Keep the readable script in `transcript.md`.
- Store real API keys only in the repository root `.env`.
- See `references/input-schema.md`, `references/elevenlabs.md`, and `references/ffmpeg.md` when changing script behavior.
