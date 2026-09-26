"""Verify curriculum chapters against CURRICULUM_SPEC.

Usage: python verify_curriculum.py [--blocks OUT.json]
Checks each NN-*.md for: em dashes, unquoted Mermaid labels, unbalanced display
math, the four level headings, the six closing sections, diagram and question
counts, and line count. Numbering-aware, so "## 30.7 Practice" matches.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).parent
LEVELS = ["Level 1", "Level 2", "Level 3", "Level 4"]
CLOSERS = ["Subtopic checklist", "Common misconceptions", "Practice",
           "How this is tested", "Summary", "Further reading"]


def heading_present(text, name):
    """True if a level-2 heading ends with `name`, with or without a number."""
    pat = r"^## (?:\d+\.\d+ )?.*%s\s*$" % re.escape(name)
    return re.search(pat, text, flags=re.M | re.I) is not None


def mermaid_problems(text):
    out = []
    for i, b in enumerate(re.findall(r"```mermaid\n(.*?)```", text, flags=re.S), 1):
        body = b.strip()
        if not body:
            out.append("diagram %d empty" % i)
            continue
        if body.splitlines()[0].startswith("quadrantChart"):
            # point rows need bracketed coordinates, `Name: [x, y]`; bare
            # `Name: x, y` fails to parse. A quoted name is tolerated.
            for line in body.splitlines()[1:]:
                ln = line.strip()
                if not ln or ln.startswith(("title", "x-axis", "y-axis", "quadrant-", "%%")):
                    continue
                if ":" in ln and "[" not in ln:
                    out.append("diagram %d quadrant point needs bracketed coords, `Name: [x, y]`: %s" % (i, ln[:44]))
                    break
            continue
        if not body.splitlines()[0].startswith(("flowchart", "graph", "stateDiagram")):
            continue
        for line in body.splitlines():
            s = line.strip()
            if s.startswith(("%%", "end")) or "[*]" in s:
                continue
            s = re.sub(r"^subgraph\s+", "", s)
            s = re.sub(r'"[^"]*"', '""', s)  # blank quoted labels so their contents cannot trip the scan
            hit = False
            for m in re.finditer(r"[A-Za-z0-9_]+\s*([\[\{\(]{1,2})([^\"\]\}\)])", s):
                if '"' not in s[m.end(1):m.end(1) + 2]:
                    out.append("diagram %d unquoted label: %s" % (i, line.strip()[:50]))
                    hit = True
                    break
            if hit:
                break
    return out


def check(path):
    t = path.read_text(encoding="utf-8")
    p = []
    if "—" in t:
        p.append("%d em dash(es)" % t.count("—"))
    if t.count("$$") % 2:
        p.append("odd $$ count")
    fences = [l for l in t.splitlines() if re.match(r"^ {0,3}```", l)]
    if len(fences) % 2:
        p.append("unbalanced code fences")
    if "<invoke" in t:
        p.append("stray invoke tag")
    for lv in LEVELS:
        if lv not in t:
            p.append("missing %s" % lv)
    for c in CLOSERS:
        if not heading_present(t, c):
            p.append("missing section: %s" % c)
    p += mermaid_problems(t)
    dia = len(re.findall(r"```mermaid", t))
    qa = len(re.findall(r"<details>", t))
    lines = t.count("\n") + 1
    if dia < 3:
        p.append("only %d diagrams" % dia)
    if qa < 1:
        p.append("no question blocks")
    if lines < 400:
        p.append("only %d lines" % lines)
    return lines, dia, qa, p, re.findall(r"```mermaid\n(.*?)```", t, flags=re.S)


def main():
    out_blocks = None
    if "--blocks" in sys.argv:
        out_blocks = pathlib.Path(sys.argv[sys.argv.index("--blocks") + 1])
    files = sorted(f for f in HERE.glob("[0-9][0-9]-*.md"))
    allb, tot, bad = [], 0, 0
    for f in files:
        lines, dia, qa, probs, blocks = check(f)
        tot += lines
        allb += [{"file": f.name, "i": i + 1, "code": b} for i, b in enumerate(blocks)]
        if probs:
            bad += 1
        print("%s %-58s %5d ln %2d dia %2d Q" % ("FIX" if probs else "OK ", f.name, lines, dia, qa))
        for x in probs:
            print("      - %s" % x)
    print("\n%d chapters, %d lines, %d diagrams, %d with problems" % (len(files), tot, len(allb), bad))
    missing = [n for n in range(1, 37) if not list(HERE.glob("%02d-*.md" % n))]
    if missing:
        print("missing chapters:", missing)
    if out_blocks:
        out_blocks.write_text(json.dumps(allb), encoding="utf-8")
        print("wrote", out_blocks)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
