import argparse
import json
import os
import shutil
import sys

BASE_PATH = os.path.join(os.path.dirname(__file__), "resources")
REQUIRED_RESOURCE_DIRS = [
    "upload",
    "midi",
    "sheet",
    "mp3",
    "simple_sheet",
    "harder_sheet",
]


def _ensure_resource_dirs() -> None:
    for folder in REQUIRED_RESOURCE_DIRS:
        os.makedirs(os.path.join(BASE_PATH, folder), exist_ok=True)


def _output_paths(name: str) -> dict:
    return {
        "midi": os.path.join(BASE_PATH, "midi", f"{name}.mid"),
        "sheet": os.path.join(BASE_PATH, "sheet", f"{name}.pdf"),
        "mp3": os.path.join(BASE_PATH, "mp3", f"{name}.mp3"),
        "simple_midi": os.path.join(BASE_PATH, "simple_sheet", f"{name}_simple.mid"),
        "simple_sheet": os.path.join(BASE_PATH, "simple_sheet", f"{name}_simple.pdf"),
        "simple_mp3": os.path.join(BASE_PATH, "simple_sheet", f"{name}_simple.mp3"),
    }


def _status(name: str) -> dict:
    output_paths = _output_paths(name)
    exists = {key: os.path.exists(path) for key, path in output_paths.items()}
    core_complete = all(exists[key] for key in ["midi", "sheet", "mp3"])
    simple_complete = all(exists[key] for key in ["simple_midi", "simple_sheet", "simple_mp3"])

    if core_complete and simple_complete:
        overall = "done"
    elif any(exists.values()):
        overall = "processing"
    else:
        overall = "not_found"

    return {"name": name, "status": overall, "outputs": exists, "paths": output_paths}


def _list_demos() -> list:
    _ensure_resource_dirs()
    demos = []
    midi_dir = os.path.join(BASE_PATH, "midi")
    for filename in sorted(os.listdir(midi_dir)):
        if not filename.endswith(".mid"):
            continue

        base_name = filename.rsplit(".", 1)[0]
        sheet_path = os.path.join(BASE_PATH, "sheet", f"{base_name}.pdf")
        mp3_path = os.path.join(BASE_PATH, "mp3", f"{base_name}.mp3")
        if not (os.path.exists(sheet_path) and os.path.exists(mp3_path)):
            continue

        parts = base_name.split("-", 1)
        if len(parts) == 2:
            artist, title = parts[0].strip(), parts[1].strip()
        else:
            artist, title = "", base_name.strip()
        demos.append({"filename": base_name, "title": title, "artist": artist})

    return demos


def _process(input_path: str, name: str | None = None) -> dict:
    try:
        from .Tune2key import TUNE2KEY
    except ImportError:
        from Tune2key import TUNE2KEY

    _ensure_resource_dirs()

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    input_path = os.path.abspath(input_path)
    ext = os.path.splitext(input_path)[1].lower()
    if ext not in {".mp3", ".opus", ".mid", ".pdf"}:
        raise ValueError("Only .mp3, .opus, .mid, and .pdf are supported")

    output_name = name or os.path.splitext(os.path.basename(input_path))[0]
    upload_dir = os.path.join(BASE_PATH, "upload")
    os.makedirs(upload_dir, exist_ok=True)
    staged_path = os.path.join(upload_dir, f"{output_name}{ext}")
    shutil.copy2(input_path, staged_path)

    processor = TUNE2KEY()
    processor.upload_file(staged_path)

    return {
        "ok": True,
        "input": input_path,
        "name": output_name,
        "status": _status(output_name),
    }


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Tune2Key CLI: process MP3/MIDI files and inspect generated outputs."
    )
    subparsers = parser.add_subparsers(dest="command")

    process_parser = subparsers.add_parser("process", help="Process one input file")
    process_parser.add_argument("input", help="Path to input file (.mp3, .mid, .pdf)")
    process_parser.add_argument(
        "--name",
        help="Override output base name. Default uses input file name.",
    )

    status_parser = subparsers.add_parser("status", help="Check generated file status")
    status_parser.add_argument("name", help="Output base name")

    subparsers.add_parser("demos", help="List demo tracks with available sheet + mp3")
    return parser


def _print_json(data: dict | list) -> None:
    print(json.dumps(data, ensure_ascii=False, indent=2))


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    try:
        if args.command == "process":
            _print_json(_process(args.input, args.name))
            return 0
        if args.command == "status":
            _print_json(_status(args.name))
            return 0
        if args.command == "demos":
            _print_json(_list_demos())
            return 0
    except Exception as exc:
        _print_json({"ok": False, "error": str(exc)})
        return 1

    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())