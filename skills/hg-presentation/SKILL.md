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

Use `draft.md` for long-form thinking, `slides.md` for the slide structure, and `narration.json` as the executable voiceover input. Narration uses `slides[].segments[]`; the legacy `slides[].text` shape is not valid.

## Workflow

Run scripts with `uv run python`.

1. Convert legacy paragraph narration when needed:

   ```sh
   uv run python skills/hg-presentation/scripts/segment_narration.py contents/YYYY/NN-title --dry-run
   uv run python skills/hg-presentation/scripts/segment_narration.py contents/YYYY/NN-title
   ```

2. Validate the project:

   ```sh
   uv run python skills/hg-presentation/scripts/validate_project.py contents/YYYY/NN-title --skip-api-key
   ```

3. Generate or reuse segment and slide audio:

   ```sh
   uv run python skills/hg-presentation/scripts/generate_audio.py contents/YYYY/NN-title
   ```

4. Build the timeline:

   ```sh
   uv run python skills/hg-presentation/scripts/build_timeline.py contents/YYYY/NN-title
   ```

5. Generate YouTube subtitles and transcript:

   ```sh
   uv run python skills/hg-presentation/scripts/generate_subtitles.py contents/YYYY/NN-title
   ```

6. Render the video:

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
- Use ElevenLabs v3 audio tags sparingly at the start of segment text, for example `[calm]` or `[thoughtful][slight emphasis]`.
- Segment audio is generated under `build/voiceover/audio/slide-001/segment-001.mp3` and concatenated into `build/voiceover/audio/slide-001.mp3`.
- Store real API keys only in the repository root `.env`.
- See `references/input-schema.md`, `references/elevenlabs.md`, and `references/ffmpeg.md` when changing script behavior.
