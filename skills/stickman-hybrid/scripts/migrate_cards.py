"""Rewrite an old SCENES.tsv so it has ZERO text and no standalone full-screen `card` rows.

    python <skill>/scripts/migrate_cards.py SCENES.tsv            # in place, keeps SCENES.tsv.bak
    python <skill>/scripts/migrate_cards.py SCENES.tsv -o NEW.tsv # leave the original alone
    python <skill>/scripts/migrate_cards.py SCENES.tsv --dry-run  # only report what would change

Rule: NO TEXT ANYWHERE IN THE VIDEO. The video is pure visual storytelling (illustrations + cut-out stickers).
- Any full-screen `card` row is removed (allowing the preceding scene picture to continue).
- Any `tag` or `count` overlay row is removed.
- Any text in the `text` column is cleared.
- Any `bars:` chart is removed.
- Stickers positioned for cards get `auto,<h>` so they sit in quiet spots on the scene picture.
"""
import argparse, csv, io, os, shutil, sys

TAG_POS = "auto,0.28"
MAX_STICKER_H = 0.3


def is_comment(line):
    s = line.strip()
    return not s or s.startswith("#") or s.split("\t")[0].strip() == "cue"


def migrate(lines):
    """lines: raw lines of a SCENES.tsv. Returns (new_lines, report, errors)."""
    out, report, errors = [], [], []
    prev_img = None            # the scene picture currently on screen
    on_card = False            # overlays that follow belong to a removed card
    for n, raw in enumerate(lines, 1):
        line = raw.rstrip("\r\n")
        if is_comment(line):
            out.append(line)
            continue
        cols = next(csv.reader([line], delimiter="\t"))
        cols += [""] * (5 - len(cols))
        cue, img, text, pos, extra = (c.strip() for c in cols[:5])

        # 1. Overlay rows (+cue)
        if cue.startswith("+"):
            if img.lower() in ("tag", "count"):
                report.append(f"line {n}: removed text overlay {cue} {img} ({text})")
                continue
            if on_card:
                if not pos or pos.startswith("auto"):
                    h = float(pos.split(",")[1]) if "," in pos else MAX_STICKER_H
                else:
                    h = float(pos.split(",")[2])
                new_pos = f"auto,{min(h, MAX_STICKER_H):g}"
                if new_pos != pos:
                    report.append(f"line {n}: {cue} sticker {pos or '(none)'} -> {new_pos}")
                    pos = new_pos
            if text:
                report.append(f"line {n}: cleared text label {text!r} from sticker {cue} {img}")
                text = ""
            if extra.startswith("bars:"):
                report.append(f"line {n}: removed chart from {cue}")
                extra = ""
            out.append("\t".join([cue, img, text, pos, extra]))
            continue

        # 2. Scene rows (cue)
        if img.lower() == "card":
            if prev_img is None:
                errors.append(f"line {n}: card at cue {cue} has no scene picture above it; replace it with a scene picture (e.g. img/s01.jpg)")
                continue
            on_card = True
            report.append(f"line {n}: removed card {cue} ({text or 'empty'}), {prev_img} continues")
            continue

        prev_img, on_card = img, False
        if text:
            report.append(f"line {n}: cleared on-screen text {text!r} from scene {cue} {img}")
            text = ""
        if extra.startswith("bars:"):
            report.append(f"line {n}: removed chart from scene {cue}")
            extra = ""
        out.append("\t".join([cue, img, text, pos, extra]))
    return out, report, errors


def main():
    for stream in (sys.stdout, sys.stderr):           # Hindi text in the report on a cp1252 console
        stream.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("scenes")
    ap.add_argument("-o", "--out", help="write here instead of changing the file in place")
    ap.add_argument("--dry-run", action="store_true", help="report only, write nothing")
    ap.add_argument("--no-backup", action="store_true", help="in-place: do not keep SCENES.tsv.bak")
    a = ap.parse_args()
    with open(a.scenes, encoding="utf-8-sig", newline="") as f:
        lines = f.read().splitlines()
    new, report, errors = migrate(lines)
    for r in report:
        print(r)
    for e in errors:
        print("ERROR " + e, file=sys.stderr)
    print(f"{len(report)} changes, {len(errors)} problems")
    if a.dry_run or errors:
        if errors:
            print("nothing written", file=sys.stderr)
        return 1 if errors else 0
    dest = a.out or a.scenes
    if not a.out and not a.no_backup:
        shutil.copyfile(a.scenes, a.scenes + ".bak")
    with open(dest, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(new) + "\n")
    print("wrote", os.path.abspath(dest))
    return 0


if __name__ == "__main__":
    sys.exit(main())
