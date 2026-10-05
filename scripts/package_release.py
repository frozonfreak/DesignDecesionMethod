"""Build the .zip and .skill exports."""

from __future__ import annotations

import argparse
import io
import sys
import zipfile
from pathlib import Path

from release_lib import SKILL_DIR, package_members, validate_release


def archive_bytes(root: Path) -> bytes:
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as archive:
        for name, data in package_members(root):
            info = zipfile.ZipInfo(name, date_time=(2026, 10, 5, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.flag_bits |= 0x800
            info.external_attr = (0o40755 if name.endswith("/") else 0o100644) << 16
            archive.writestr(info, data)
    return buffer.getvalue()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Package the skill as .zip and .skill archives.")
    parser.add_argument("--root", default=".", help="Repository root")
    parser.add_argument("--output", default="dist", help="Directory for the generated archives")
    args = parser.parse_args(argv)
    root = Path(args.root)
    errors = validate_release(root)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    payload = archive_bytes(root)
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    zip_path = output / f"{SKILL_DIR}.zip"
    skill_path = output / f"{SKILL_DIR}.skill"
    zip_path.write_bytes(payload)
    skill_path.write_bytes(payload)
    print(zip_path.as_posix())
    print(skill_path.as_posix())
    return 0


if __name__ == "__main__":
    sys.exit(main())
