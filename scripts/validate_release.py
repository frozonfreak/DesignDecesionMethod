"""Validate the Design Decision Method release tree."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from release_lib import validate_release, write_manifest


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate the skill release files.")
    parser.add_argument(
        "root",
        nargs="?",
        default=".",
        help="Repository root or an extracted design-decision-method directory",
    )
    parser.add_argument(
        "--write-manifest",
        action="store_true",
        help="Regenerate release-manifest.json from the current skill files",
    )
    args = parser.parse_args(argv)
    root = Path(args.root)
    if args.write_manifest:
        write_manifest(root)
    errors = validate_release(root)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("release validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
