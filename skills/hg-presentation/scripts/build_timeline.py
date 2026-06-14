from __future__ import annotations

import argparse
import json
import subprocess
import sys

from project_config import audio_path, load_project, relative_to_presentation, timeline_path


def probe_duration(path) -> float:
    result = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(path),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return float(result.stdout.strip())


def build(project_file: str) -> int:
    project = load_project(project_file)
    entries = []

    for slide in project.slides:
        audio = audio_path(project, slide)
        if not audio.exists():
            print(f"ERROR: Missing audio for slide {slide.index}: {audio}", file=sys.stderr)
            return 1
        try:
            duration = probe_duration(audio)
        except Exception as exc:
            print(f"ERROR: Could not read duration for {audio}: {exc}", file=sys.stderr)
            return 1
        entries.append(
            {
                "index": slide.index,
                "image": relative_to_presentation(project, slide.image),
                "audio": relative_to_presentation(project, audio),
                "duration": round(duration, 3),
            }
        )

    timeline = {
        "video": {
            "width": project.video.width,
            "height": project.video.height,
            "fps": project.video.fps,
        },
        "slides": entries,
    }
    path = timeline_path(project)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(timeline, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {path}")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a slide/audio timeline JSON.")
    parser.add_argument("project", help="Presentation directory or narration.json path")
    args = parser.parse_args()

    raise SystemExit(build(args.project))


if __name__ == "__main__":
    main()
