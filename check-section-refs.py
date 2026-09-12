#!/usr/bin/env python3
"""Resolve every "section N" reference in survey-flow/*.html to the heading it names.

A section number is a NAME that two documents share, and renumbering is renaming.
Nothing fails when a pointer goes stale: the reference still resolves to a real
section, just the wrong one. Run this after inserting, removing or reordering any
<h2> in any of these files.

    python3 check-section-refs.py

Exits non-zero if a reference points outside the target document's range. It
CANNOT tell you a reference points at the wrong section - only a human reading
the resolved heading can. That is why it prints every one rather than only errors.
"""
import re, sys, pathlib

DOCS = ["privacy.html", "terms.html", "user-guide.html", "pricing.html"]
here = pathlib.Path(__file__).parent / "survey-flow"

heads, texts = {}, {}
for d in DOCS:
    f = here / d
    if not f.exists():
        continue
    t = texts[d] = f.read_text(encoding="utf-8")
    heads[d] = [h[1] for h in re.findall(r'<h2 id="([\w-]+)"[^>]*>(?:<span[^>]*>\d+</span>)?([^<]*)</h2>', t)]

bad = 0
for d in DOCS:
    if d not in texts:
        continue
    print(f"\n{d}")
    for m in re.finditer(r'[Ss]ection (\d+)( of the (?:<a[^>]*>)?privacy policy)?', texts[d]):
        n = int(m.group(1))
        target = "privacy.html" if m.group(2) else d
        names = heads.get(target, [])
        if 1 <= n <= len(names):
            print(f"  section {n:>2} -> {target:<15} {names[n-1]}")
        else:
            print(f"  section {n:>2} -> {target:<15} ⚠️  OUT OF RANGE")
            bad += 1

print(f"\n{'FAIL' if bad else 'ok'}: {bad} out-of-range reference(s)."
      f" Read the headings above - a reference can resolve and still be wrong.")
sys.exit(1 if bad else 0)
