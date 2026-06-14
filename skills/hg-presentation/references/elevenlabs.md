# ElevenLabs Notes

The scripts use the ElevenLabs Text to Speech REST API:

```text
POST https://api.elevenlabs.io/v1/text-to-speech/:voice_id?output_format=mp3_44100_128
```

Required environment values:

```dotenv
ELEVENLABS_API_KEY=replace_me
ELEVENLABS_VOICE_ID=replace_me
ELEVENLABS_MODEL_ID=eleven_multilingual_v2
ELEVENLABS_OUTPUT_FORMAT=mp3_44100_128
```

Defaults:

- `eleven_multilingual_v2` for stable long-form narration quality.
- `mp3_44100_128` for broad MP3 compatibility.

Do not print or commit the real API key. Keep it in the repository root `.env`.
