# Input Schema

Use one `narration.json` file per presentation directory.

```json
{
  "output_dir": "build/voiceover",
  "exports_dir": "exports",
  "video": {
    "width": 1920,
    "height": 1080,
    "fps": 30
  },
  "voice": {
    "voice_id": "${ELEVENLABS_VOICE_ID}",
    "model_id": "${ELEVENLABS_MODEL_ID}",
    "output_format": "${ELEVENLABS_OUTPUT_FORMAT}"
  },
  "slides": [
    {
      "image": "images/example/cover.png",
      "text": "Welcome. Today we will walk through the project."
    }
  ]
}
```

Paths are resolved relative to the presentation directory.

`generate_subtitles.py` reads `build/voiceover/timeline.json` and writes:

- `youtube.srt`
- `transcript.md`
