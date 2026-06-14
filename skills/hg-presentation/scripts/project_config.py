from __future__ import annotations

import json
import os
import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ENV_PATTERN = re.compile(r"\$\{([A-Za-z_][A-Za-z0-9_]*)\}")


@dataclass(frozen=True)
class Slide:
    index: int
    image: Path
    text: str


@dataclass(frozen=True)
class VoiceConfig:
    voice_id: str
    model_id: str
    output_format: str


@dataclass(frozen=True)
class VideoConfig:
    width: int
    height: int
    fps: int


@dataclass(frozen=True)
class Project:
    path: Path
    root: Path
    presentation_dir: Path
    output_dir: Path
    exports_dir: Path
    voice: VoiceConfig
    video: VideoConfig
    slides: list[Slide]


def find_repo_root(start: Path | None = None) -> Path:
    current = (start or Path.cwd()).resolve()
    for path in [current, *current.parents]:
        if (path / "pyproject.toml").exists() or (path / ".git").exists():
            return path
    return current


def load_root_env(root: Path) -> None:
    env_path = root / ".env"
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        name, value = stripped.split("=", 1)
        name = name.strip()
        value = value.strip().strip('"').strip("'")
        os.environ.setdefault(name, value)


def resolve_env_value(value: Any, *, required: bool = False) -> Any:
    if not isinstance(value, str):
        return value

    def replace(match: re.Match[str]) -> str:
        name = match.group(1)
        resolved = os.environ.get(name)
        if resolved is None:
            if required:
                raise ValueError(f"Environment variable {name} is required but not set")
            return ""
        return resolved

    return ENV_PATTERN.sub(replace, value)


def _positive_int(value: Any, field: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{field} must be a positive integer")
    return value


def _resolve_input(path_arg: str | Path, root: Path) -> tuple[Path, Path]:
    path = Path(path_arg).expanduser()
    if not path.is_absolute():
        path = root / path
    path = path.resolve()
    if path.is_dir():
        return path / "narration.json", path
    return path, path.parent


def _resolve_project_path(presentation_dir: Path, value: str) -> Path:
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = presentation_dir / path
    return path.resolve()


def relative_to_presentation(project: Project, path: Path) -> str:
    try:
        return path.resolve().relative_to(project.presentation_dir).as_posix()
    except ValueError:
        return os.path.relpath(path.resolve(), project.presentation_dir).replace(os.sep, "/")


def load_project(project_path: str | Path) -> Project:
    root = find_repo_root()
    load_root_env(root)

    path, presentation_dir = _resolve_input(project_path, root)
    if not path.exists():
        raise ValueError(f"narration file does not exist: {path}")

    with path.open("r", encoding="utf-8") as handle:
        raw = json.load(handle)

    if not isinstance(raw, dict):
        raise ValueError("narration JSON must be an object")

    output_dir_raw = resolve_env_value(raw.get("output_dir", "build/voiceover"))
    output_dir = _resolve_project_path(presentation_dir, str(output_dir_raw))
    exports_dir = _resolve_project_path(presentation_dir, str(raw.get("exports_dir", "exports")))

    voice_raw = raw.get("voice", {})
    if voice_raw is None:
        voice_raw = {}
    if not isinstance(voice_raw, dict):
        raise ValueError("voice must be an object when provided")

    voice_id = resolve_env_value(voice_raw.get("voice_id", "${ELEVENLABS_VOICE_ID}"))
    model_id = resolve_env_value(voice_raw.get("model_id", os.environ.get("ELEVENLABS_MODEL_ID", "eleven_multilingual_v2")))
    output_format = resolve_env_value(voice_raw.get("output_format", os.environ.get("ELEVENLABS_OUTPUT_FORMAT", "mp3_44100_128")))

    video_raw = raw.get("video", {})
    if video_raw is None:
        video_raw = {}
    if not isinstance(video_raw, dict):
        raise ValueError("video must be an object when provided")

    video = VideoConfig(
        width=_positive_int(video_raw.get("width", 1920), "video.width"),
        height=_positive_int(video_raw.get("height", 1080), "video.height"),
        fps=_positive_int(video_raw.get("fps", 30), "video.fps"),
    )

    slides_raw = raw.get("slides")
    if not isinstance(slides_raw, list) or not slides_raw:
        raise ValueError("slides must be a non-empty array")

    slides: list[Slide] = []
    for idx, item in enumerate(slides_raw, start=1):
        if not isinstance(item, dict):
            raise ValueError(f"slides[{idx}] must be an object")
        image_raw = resolve_env_value(item.get("image"))
        text = resolve_env_value(item.get("text"))
        if not isinstance(image_raw, str) or not image_raw.strip():
            raise ValueError(f"slides[{idx}].image is required")
        if not isinstance(text, str) or not text.strip():
            raise ValueError(f"slides[{idx}].text is required")
        slides.append(Slide(index=idx, image=_resolve_project_path(presentation_dir, image_raw), text=text.strip()))

    return Project(
        path=path.resolve(),
        root=root,
        presentation_dir=presentation_dir.resolve(),
        output_dir=output_dir,
        exports_dir=exports_dir,
        voice=VoiceConfig(voice_id=str(voice_id), model_id=str(model_id), output_format=str(output_format)),
        video=video,
        slides=slides,
    )


def require_tools(*names: str) -> list[str]:
    return [name for name in names if shutil.which(name) is None]


def audio_path(project: Project, slide: Slide) -> Path:
    return project.output_dir / "audio" / f"slide-{slide.index:03d}.mp3"


def timeline_path(project: Project) -> Path:
    return project.output_dir / "timeline.json"


def voiceover_video_path(project: Project) -> Path:
    return project.output_dir / "final.mp4"


def final_video_path(project: Project) -> Path:
    return project.exports_dir / "final.mp4"
