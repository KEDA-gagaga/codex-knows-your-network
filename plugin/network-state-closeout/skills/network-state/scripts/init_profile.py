#!/usr/bin/env python3
"""Initialize a private network-state profile outside the installed skill directory."""

from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path


def default_state_path() -> Path:
    configured = os.environ.get("NETWORK_STATE_HOME")
    if configured:
        return Path(configured).expanduser()
    return Path.home() / ".codex" / "network-state"


def is_within(child: Path, parent: Path) -> bool:
    try:
        child.relative_to(parent)
        return True
    except ValueError:
        return False


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a private network-state profile from the bundled empty templates."
    )
    parser.add_argument(
        "--path",
        type=Path,
        default=default_state_path(),
        help="Private profile directory (default: NETWORK_STATE_HOME or ~/.codex/network-state)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    skill_dir = Path(__file__).resolve().parent.parent
    template_dir = skill_dir / "assets" / "profile-template"
    target = args.path.expanduser().resolve()

    if is_within(target, skill_dir):
        print("Refusing to place private state inside the skill directory.", file=sys.stderr)
        return 2

    if not template_dir.is_dir():
        print(f"Template directory is missing: {template_dir}", file=sys.stderr)
        return 2

    if target.exists():
        if not target.is_dir():
            print(f"Target exists and is not a directory: {target}", file=sys.stderr)
            return 2
        if any(target.iterdir()):
            print(f"Target directory is not empty; nothing changed: {target}", file=sys.stderr)
            return 2
    else:
        target.mkdir(parents=True, mode=0o700)

    created: list[Path] = []
    try:
        for source in sorted(template_dir.iterdir()):
            if not source.is_file():
                continue
            destination = target / source.name
            shutil.copyfile(source, destination)
            os.chmod(destination, 0o600)
            created.append(destination)
        os.chmod(target, 0o700)
    except Exception:
        for path in created:
            path.unlink(missing_ok=True)
        raise

    print("Initialized private network-state profile.")
    print(f"path: {target}")
    print("next: edit profile.md and devices.md, then run validate_profile.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
