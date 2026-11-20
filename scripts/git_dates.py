"""Write each page's git creation/revision dates into its front matter.

Zensical does not run the git-revision-date-localized plugin yet, but the
theme shows `git_revision_date_localized` / `git_creation_date_localized`
from front matter. Run this in CI right before `zensical build`; it edits
the working tree, so don't commit the result.
"""
import pathlib
import subprocess
import sys
from datetime import date


def dates(path):
    # author dates in each commit's own timezone, newest first
    out = subprocess.run(
        ["git", "log", "--follow", "--format=%ad", "--date=format:%Y-%m-%d", "--", str(path)],
        capture_output=True, text=True, check=True,
    ).stdout.split()
    if not out:
        today = date.today().isoformat()
        return today, today
    return out[-1], out[0]


def localize(iso):
    y, m, d = (int(x) for x in iso.split("-"))
    return f"{y}年{m}月{d}日"


def main(docs):
    for path in sorted(pathlib.Path(docs).rglob("*.md")):
        created, revised = (localize(x) for x in dates(path))
        meta = f"git_creation_date_localized: {created}\ngit_revision_date_localized: {revised}\n"
        text = path.read_text()
        if text.startswith("---\n"):
            text = "---\n" + meta + text[4:]
        else:
            text = "---\n" + meta + "---\n\n" + text
        path.write_text(text)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "docs")
