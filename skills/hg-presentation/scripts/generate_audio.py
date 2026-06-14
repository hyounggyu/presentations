from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

from project_config import audio_path, load_project


API_BASE = "https://api.elevenlabs.io/v1/text-to-speech"


def generate(project_file: str, *, overwrite: bool = False) -> int:
    project = load_project(project_file)
    api_key = os.environ.get("ELEVENLABS_API_KEY")
    if not api_key:
        print("ERROR: ELEVENLABS_API_KEY is required in .env or the process environment", file=sys.stderr)
        return 1
    if not project.voice.voice_id:
        print("ERROR: voice.voice_id or ELEVENLABS_VOICE_ID is required", file=sys.stderr)
        return 1

    audio_dir = project.output_dir / "audio"
    audio_dir.mkdir(parents=True, exist_ok=True)

    for slide in project.slides:
        target = audio_path(project, slide)
        if target.exists() and not overwrite:
            print(f"Skipping existing audio: {target}")
            continue

        query = urllib.parse.urlencode({"output_format": project.voice.output_format})
        url = f"{API_BASE}/{urllib.parse.quote(project.voice.voice_id)}?{query}"
        payload = {
            "text": slide.text,
            "model_id": project.voice.model_id,
        }
        request = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "xi-api-key": api_key,
            },
            method="POST",
        )

        try:
            with urllib.request.urlopen(request, timeout=120) as response:
                target.write_bytes(response.read())
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            print(f"ERROR: ElevenLabs request failed for slide {slide.index}: HTTP {exc.code} {detail}", file=sys.stderr)
            return 1
        except urllib.error.URLError as exc:
            print(f"ERROR: ElevenLabs request failed for slide {slide.index}: {exc}", file=sys.stderr)
            return 1

        print(f"Wrote {target}")

    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate per-slide ElevenLabs TTS audio.")
    parser.add_argument("project", help="Presentation directory or narration.json path")
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    raise SystemExit(generate(args.project, overwrite=args.overwrite))


if __name__ == "__main__":
    main()
