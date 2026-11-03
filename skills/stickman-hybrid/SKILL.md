---
name: stickman-hybrid
description: Make a complete stickman documentary explainer in the HYBRID look, end to end: clean full-colour scene pictures (Google Flow, Nano Banana 2) with cut-out stickers that pop in on the spoken words, paper collage beats, in the style of the viral "ancient humans" explainer channels. Completely text-free visuals (no on-screen text, no tags, no counters, no labels, no cards). Covers setup, topic ideas, the expressive TTS script (text2speech tags for Gemini 3.8 TTS / Google Cloud TTS Playground / ElevenLabs), user audio merge (VO.wav) or automated VO (Kokoro for English, Indic Parler on Kaggle for Hindi/Indian languages), consistent stickman cast, LaMa watermark removal, word-timed cuts, sound design and the final MP4. Use when the user says "stickman hybrid", "hybrid stickman", "stickman sticker video", "stickman hybrid start", "stickman hybrid continue", or opens the stickman-animation zip.
---

# Stickman documentary, hybrid look, end to end

You make the whole video for the user. They choose the topic, language and length; you do
the rest and show them only three checkpoints: the script, the voice and the finished video.

**Talk to the user in their own language** (often Hinglish), simply. Commands, file names and
file contents stay in English. Always give full absolute paths. Give a `https://` link only
when you are certain it is right (one written in these files, or one a tool printed); never
guess a URL. If unsure, give the menu path or let the tool say it.

`<skill>` means this skill's folder: `~/.gemini/config/skills/stickman-hybrid/` (Windows:
`C:\Users\<me>\.gemini\config\skills\stickman-hybrid\`) or fallback `~/.claude/skills/stickman-hybrid/`.
The companion skill **vox-doc-sound** (`~/.gemini/config/skills/vox-doc-sound/`) makes the voice and the sound;
read its SKILL.md at those stages. The companion skill **text2speech** (`~/.gemini/config/skills/text2speech/`)
formats scripts with natural expressive tags.

**Before planning any video, read `<skill>/PLAYBOOK.md` fully and `<skill>/looks/README.md`.**
The Part 1 rules are what made the test films work; follow them without exception.
`<skill>/example/` holds the approved films. **`boat_hi` is the current target** (follow it first). `food` (English) and `food_hi` (Hindi, the same
pictures re-voiced) and `teeth_hybrid` are the target: their SCENES (with `+` sticker rows),
ELEMENTS, PICK/ELPICK, cues and contact sheets show it. `teeth` and `cooking` are the plain-stills
ancestors.

**This pack makes the HYBRID look by default** (PLAYBOOK §9): every film has scene pictures plus
ELEMENTS.tsv stickers and paper collage beats. Make plain stills only if the user
asks for them.

## Every time this skill starts ("start", "continue", a topic, anything)

1. **Setup check.** Read `<skill>/SETUP_STATUS.md`. If it is missing or any required row is
   not ✅, run or resume `<skill>/SETUP.md` from the first unfinished step, then come back.
   Prerequisite: Flow Connector, set up by the user from the extension's own setup prompt.
   At setup only check `flow-auto --version`. "Extension not connected" is NOT a setup
   failure; Flow is connected at the picture stage.
2. **Find the project.** Projects live in `~/StickmanHybrid/<topic-slug>/`.
   - "continue" with no topic: open the most recently modified `PROGRESS.md` under
     `~/StickmanHybrid/`; tell the user which project and stage you are resuming.
   - New topic: create `~/StickmanHybrid/<slug>/` (short, lowercase, no spaces) with `PROGRESS.md`.
   - No topic yet: ask in ONE short message, with no defaults:
     - **Topic**: their own, or "Want me to suggest 10 topics?" (PLAYBOOK §1). For Hindi
       audiences give bilingual titles.
     - **Language** of the narration: Hindi, English, Hinglish, **or any other**. Say honestly
       which have a free voice (vox-doc-sound SKILL.md, step 2).
     - **Length**: their choice (for example 2, 5, 8 or 10 minutes, or any number). Do not
       pre-select one.
3. Work only inside the project folder; run every script from there.
4. After each stage update `PROGRESS.md`: stage, ✅, decisions (look, cast, voice, language,
   length), what the user approved. Then "continue" in any new chat resumes correctly.

## Stages

| # | Stage | Do | Checkpoint |
|---|---|---|---|
| 1 | Script | `SCRIPT.md` + `LINES.tsv` (PLAYBOOK §1). Format the script using companion skill **text2speech** with natural inline expression tags (`<short pause>`, `<breath>`, `<sigh>`, `<whispers>`) and deliver it inside a copyable code block with voice recommendations, or standard script. Hindi narration runs ~25% longer than English: write ~15% fewer words for the chosen length. Check facts on the web; word debated points as such | **Wait for the user's OK** |
| 2 | Look, cast, pictures: START IMMEDIATELY after the OK, in parallel with stage 3 | Choose the look by topic (`looks/`), write `STYLE.txt`, decide the cast. Also write `ELEMENTS.tsv` (PLAYBOOK §9) and run `pictures.py elements 1 <a pose>` as the sticker test, then the rest. Connect Flow: `flow-auto bridge start` in the background, then `flow-auto doctor --site flow` (relay its words if a line fails; never write your own Flow URL). Make the character sheet, then `pictures.py refs`. Write `SHOTS.tsv` from the script (PLAYBOOK §3). `pictures.py submit` 2 test shots, look at them, then submit the rest, and start `delama.py --watch` in the background (LaMa cleans each picture as it arrives) | One line: "look X, N pictures generating while the voice is made" |
| 3 | Voice: same turn as stage 2 | vox-doc-sound. Two supported paths: **Path A (Expressive TTS / User VO):** User takes the tagged script from Stage 1, generates audio in Gemini 3.8 TTS, Google Cloud TTS Playground, ElevenLabs, or mic recording, and saves as `VO.wav`. Run `align.py --vo VO.wav --lines LINES.tsv --out WORDS.tsv --lang <code>`. **Path B (Automated):** Hindi/Indian languages → **Indic Parler-TTS** on Kaggle (`kaggle/make_parler_job.py`, speaker Aman); English/other → Kokoro (`--speed 1.0`). Then `vo_join.py` + `align.py`. | Path A: `WORDS.tsv` word count confirmed. Path B: Play 2 lines; user approves Aman or chooses another speaker. |
| 4 | Scenes | `SCENES.tsv` on the words (PLAYBOOK §5, §9), then `render.py --pacing` and fix every long hold with a beat the line names (cut or sticker pop-in). Completely text-free visuals: NO text, tags, counters, or cards inside the video. Enforce Frame Count Invariant: total frames/beats must ALWAYS be greater than total expected seconds / 3 ($N > T / 3$, expected ~2s per frame) | A short table: line → what is on screen (no approval wait) |
| 5 | Collect pictures | When the queue is empty: re-submit refused ids once. `pictures.py review` → look → `PICK.tsv` for swaps → regenerate wrong ones → `pictures.py pick` → `delama.py` (copies the LaMa-cleaned pictures; instant) | One line: "N pictures in, fixed X" |
| 6 | Sound | vox-doc-sound: `cues.tsv` on words (PLAYBOOK §7), then `mix.py ... --out mix.wav` | Loudness numbers |
| 7 | Render + QC | `render.py`, then `pictures.py qc` and read `qc.jpg` YOURSELF: wrong picture, sticker positioning, sheet line-ups, leftover sparkle. Fix, re-render. Do not show the contact sheet to the user | Open the video for the user and give its full path. **They judge the final video** |

**Never run the voice first and the pictures later.** The pictures depend only on the
script's words; start them in the same turn the script is approved (users noticed and
objected when this was done in sequence).

## Rules that are easy to forget

- **Voice:** Hindi, Hinglish and every Indian language are voiced with Indic Parler-TTS (Kaggle), never Kokoro, whose Hindi is flat. Hindi and Hinglish start with speaker **Aman**; offer Kabir, Bhanu, Dinesh or Aakash only if the user wants a change (Rohit sounds robotic). English and other languages use Kokoro (`--speed 1.0`). Parler uses make_parler_job.py's defaults (`natural` description, seed 11) and is NEVER sped up: no `--tempo`, ever (1.10x made Hindi robotic). vo_join adds the approved pauses itself (Indian +0.3 s, others +0.35 s); a line it flags `RE-MAKE` is voiced again with another seed.
- **Never swap in another voice engine on your own** (Edge/Azure voices such as Madhur,
  Google TTS, Piper, MMS, gTTS), not even "temporarily". The user did not choose it, the film
  would need re-timing, and those licences are not cleared for this pack.
- **Where Parler runs is the user's decision.**
  - SETUP Step 0 records the machine as strong (an NVIDIA GPU with ≥ 8 GB VRAM, or ≥ 16 GB
    RAM) or weak. Kaggle is the default either way.
  - If the Kaggle job is QUEUED, or the user would rather run it locally, follow PLAYBOOK §4
    "Kaggle queue": stop and ASK, with the options and their honest cost on THIS machine.
  - Do what the user picks. Never decide alone.
- **ABSOLUTELY NO TEXT AT ALL INSIDE THE VIDEO:** The film is 100% pure visual storytelling.
  No on-screen text, no titles, no tags, no captions, no sticker labels, no animated counters,
  no numbers or dates, no bar charts, and no standalone `card` scenes (`img = "card"`). The spoken
  narration carries all verbal information; the screen carries only clean scene illustrations
  and cut-out stickers.
  - The scene picture (`img/sNN.jpg`) stays continuous throughout the scene.
  - Never switch to a blank screen, paper texture, or standalone card.
  - `render.py` stops with an error if any text, tag, counter, chart, or card row is present in `SCENES.tsv`.
  - To clean an old `SCENES.tsv` automatically: `python <skill>/scripts/migrate_cards.py SCENES.tsv`.
- Scene pictures are full, natural scenes (leave SHOTS `space` empty). Stickers go to the picture's quiet
  spots (`auto`); never spoil a scene for a sticker.
  Hindi emphasis comes from short punch lines ending in "!" with ONE doc voice for all lines; per-line
  styles made the voice robotic (vox-doc-sound 2b).
- Scene pictures stay still. Motion comes only from stickers popping on the spoken
  words (PLAYBOOK §9). No zooms, no AI video.
- **Dynamic pacing, never a fixed 3-second hold:** Shots and visual beats adapt dynamically to the scene:
  e.g. 1 second for fast cuts and punchy moments, ~2 seconds on average for smooth visual flow and
  proper blend, and up to ~3 seconds for emotional beats or complex scenes needing breathing room.
  In the first 30 s (the hook), visual beats come faster (every 1.2-1.5 s). No unchanged still longer
  than 3.5 s without a deliberate storytelling reason. Never cut merely to hit an arbitrary number:
  every beat must connect to a word the voiceover speaks.
- **Frame Count Invariant ($N > T / 3$):** Total frames / visual beats (scene cuts + sticker pop-ins) must ALWAYS be strictly greater than total expected video seconds / 3 ($N > T / 3$), never less. Since each frame averages ~2 seconds expected ($N \approx T / 2$):
  - 1-minute video (60s): $> 20$ frames minimum (expected ~30 frames).
  - 2-minute video (120s): $> 40$ frames minimum (expected ~60 frames).
  - 5-minute video (300s): $> 100$ frames minimum (expected ~150 frames).
  - 8-minute video (480s): $> 160$ frames minimum (expected ~240 frames).
- Pictures and stickers use Nano Banana 2 (Flow shows it as "Nano Banana 2.1"), never Pro: `pictures.py`
  already does this.
- Two stickers must never overlap; render.py separates them. Pin a sticker that sits near a face.
- A sticker only for a thing the line NAMES that the picture does NOT already show. No repeats of the
  picture, no decorations. If none fits, use a cut to a relevant picture.
- Flow swaps files between the scene and sticker folders too: check both `review.jpg` and
  `cutouts.jpg` before picking.
- Every picture is a full-colour scene in the chosen look. Test 2 shots before the batch.
- **Zero on-screen text:** do not place text, dates, numbers, or labels on pictures. Spoken narration
  names them; visuals show the story through illustrations and sticker props.
- Pick pictures by what they show, not by file number. Flow swaps them in batches.
- Never paste or ask for API keys or tokens in the chat. Keys go in `.env` files the user
  edits.
- On machines with 8 GB of RAM or less, keep ffmpeg at `-threads 3` (the scripts do) and run
  one heavy job at a time.
- Hindi and other non-Latin labels go through libass automatically; if a font lacks the
  script, set `STICK_FONT_COMPLEX` to a .ttf that covers it.
- For Claude usage: QC from grids, and suggest a new chat per new video.
