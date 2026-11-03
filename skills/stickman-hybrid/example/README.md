# Approved test films (~2 min each)

| Folder | Topic | Look | Pictures | Scenes | Tags |
|---|---|---|---|---|---|
| `teeth/` | How Did Ancient Humans Clean Their Teeth? | bright | 38 | 51 | 13 |
| `cooking/` | Why Are Humans the Only Animals That Cook? | warm | 44 | 57 | 11 |
| `food/` | How Did Ancient Humans Stop Food From Rotting? (hybrid, Nano Banana 2, LaMa) | bright | 27 + 17 stickers | 37 | 28 overlays |
| `food_hi/` | the same film in Hindi (Aman; made at 1.15x before the 1.10x preset was approved), re-paced with `render.py --pacing`: 96 visual changes, 24 in the hook | bright | 10 new stickers | 41 | 62 overlays |
| `boat_hi/` | **The current target.** इंसानों ने पहली नाव कैसे बनाई? Food-style: full natural scenes; the line's named objects are stickers (scene = place + action), no repeats, maps with stickers, completely text-free (no on-screen text, no cards), soft paper sounds instead of pops, Aman one doc voice 1.10x | bright | 22 + 22 | 39 | 24 overlays |
| `time_hi/` | घड़ी से पहले इंसान समय कैसे जानते थे? Hindi voice (Aman, one doc voice, 1.10x), completely text-free (no on-screen text, no cards), layouts mixed per line (`space`/`flip`), 25 stickers | bright | 21 + 25 | 38 | 38 overlays |
| `teeth_hybrid/` | the teeth film in the hybrid look (§9): same pictures + 20 stickers | bright | 38 + 20 | 47 | 29 overlays |

Each folder has:
- LINES.tsv: the script, one sentence per row
- SHOTS.tsv: the picture prompts
- STYLE.txt: the look
- PICK.tsv: the pictures Flow swapped
- SCENES.tsv: the cuts on spoken words
- cues.tsv: the sound
- contact_sheet.jpg: every scene of the final film, in order

Read the contact sheets to see the target: a full-colour scene in every frame, the same cast
throughout, and completely text-free visuals (no on-screen text, no tags, no counters, no card scenes).

The `SCENES.tsv` files here have zero on-screen text: all cards, tags, and text columns were stripped
via `scripts/migrate_cards.py`. Visual beats come exclusively from cuts between scene illustrations
and cut-out stickers popping in on the spoken words (`render.py --pacing`: a beat about every 2 s,
every 1.2-1.5 s in the hook, no still over 3.5 s without a deliberate reason).

Feedback from the review that shaped them:
- The first `cooking` cut had white backgrounds, which read as empty. It was redone in the
  warm look.
- The warm look was then judged a bit too brown, so `teeth` was made in the bright look.
- Both films first had a tag on almost every shot. The tags were cut to numbers, names, map
  places and unseen terms only, and kept off faces.
