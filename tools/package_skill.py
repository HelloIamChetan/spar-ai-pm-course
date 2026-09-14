#!/usr/bin/env python3
"""Package the skill folder into a distributable .skill bundle (a zip, by another name).

    python3 tools/package_skill.py            # -> dist/<name>-<version>.skill

The version comes from the top "## x.y.z" heading in CHANGELOG.md, so the bundle and the
changelog cannot drift apart. Stdlib only.
"""

import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "skill"
DIST = ROOT / "dist"

# Never ship these, whatever a local working copy has accumulated.
EXCLUDE_NAMES = {"__pycache__", ".DS_Store", ".git", ".pytest_cache"}
EXCLUDE_SUFFIX = {".pyc", ".pyo"}


def version():
    m = re.search(r"^##\s*(\d+\.\d+\.\d+)", (ROOT / "CHANGELOG.md").read_text(encoding="utf-8"), re.M)
    if not m:
        sys.exit("no '## x.y.z' heading found in CHANGELOG.md — cannot determine a version")
    return m.group(1)


def main():
    skills = [p for p in SKILL_DIR.iterdir() if p.is_dir()]
    if len(skills) != 1:
        sys.exit(f"expected exactly one skill folder under {SKILL_DIR}, found {len(skills)}")
    src = skills[0]
    if not (src / "SKILL.md").exists():
        sys.exit(f"{src} has no SKILL.md — that file is what makes it a skill")

    DIST.mkdir(exist_ok=True)
    out = DIST / f"{src.name}-{version()}.skill"

    files, total = [], 0
    for p in sorted(src.rglob("*")):
        if not p.is_file() or p.suffix in EXCLUDE_SUFFIX:
            continue
        if EXCLUDE_NAMES & set(p.relative_to(src).parts):
            continue
        files.append(p)
        total += p.stat().st_size

    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for p in files:
            z.write(p, Path(src.name) / p.relative_to(src))

    print(f"wrote {out.relative_to(ROOT)}  ({out.stat().st_size / 1024:.0f} KB packed, "
          f"{total / 1024:.0f} KB of {len(files)} files)")
    with zipfile.ZipFile(out) as z:
        bad = z.testzip()
        if bad:
            sys.exit(f"bundle is corrupt at {bad}")
        names = z.namelist()
    assert f"{src.name}/SKILL.md" in names, "SKILL.md missing from the bundle"
    print(f"verified: {len(names)} entries, SKILL.md present")


if __name__ == "__main__":
    main()
