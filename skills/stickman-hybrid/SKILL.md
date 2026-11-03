---
name: stickman-hybrid
description: Make a complete stickman documentary explainer in the HYBRID look, end to end: clean full-colour scene pictures (Google Flow, Nano Banana 2) with cut-out stickers that pop in on the spoken words, animated counters and paper collage beats, in the style of the viral "ancient humans" explainer channels. Covers setup, topic ideas, the expressive TTS script (text2speech tags for Gemini 3.8 TTS / Google Cloud TTS Playground / ElevenLabs), user audio merge (VO.wav) or automated VO (Kokoro for English, Indic Parler on Kaggle for Hindi/Indian languages), consistent stickman cast, LaMa watermark removal, word-timed cuts, Hindi and English on-screen text, sound design and the final MP4. Use when the user says "stickman hybrid", "hybrid stickman", "stickman sticker video", "stickman hybrid start", "stickman hybrid continue", or opens the stickman-animation zip.
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
ELEMENTS.tsv stickers, counters and a few paper collage beats. Make plain stills only if the user
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
| 2 | Look, cast, pictures: START IMMEDIATELY after the OK, in parallel with stage 3 | **Character Consistency Protocol:** First, analyze the entire script and identify all unique characters required (one or multiple). Use Google Flow to generate canonical reference images for each character first (`img/ref_<name>.jpg` or `sheet.jpg`). Then for every scene, identify required characters and provide their exact reference image in `SHOTS.tsv` (`ref` column) to Google Flow image-to-image (`flow-image-to-image`). Maintain identical appearance, clothing, facial features, proportions, and art style across all scenes. Never recreate or change an already established character. Choose look (`looks/`), write `STYLE.txt`, `ELEMENTS.tsv`, submit test shots, batch submit, and run `delama.py --watch`. | One line: "Look X, N characters locked, N pictures generating while audio is made" |
| 3 | Voice: same turn as stage 2 | vox-doc-sound. Two supported paths: **Path A (Expressive TTS / User VO):** User takes the tagged script from Stage 1, generates audio in Gemini 3.8 TTS, Google Cloud TTS Playground, ElevenLabs, or mic recording, and saves as `VO.wav`. Run `align.py --vo VO.wav --lines LINES.tsv --out WORDS.tsv --lang <code>`. **Path B (Automated):** Hindi/Indian languages → **Indic Parler-TTS** on Kaggle (`kaggle/make_parler_job.py`, speaker Aman); English/other → Kokoro (`--speed 1.0`). Then `vo_join.py` + `align.py`. | Path A: `WORDS.tsv` word count confirmed. Path B: Play 2 lines; user approves Aman or chooses another speaker. |
| 4 | Scenes | `SCENES.tsv` on the words (PLAYBOOK §5, §9), then `render.py --pacing` and fix EVERY long hold with a beat the line names (cut, sticker, counter, tag, a "no" sticker) | A short table: line → what is on screen (no approval wait) |
| 5 | Collect pictures | When the queue is empty: re-submit refused ids once. `pictures.py review` → look → `PICK.tsv` for swaps → regenerate wrong ones → `pictures.py pick` → `delama.py` (copies the LaMa-cleaned pictures; instant) | One line: "N pictures in, fixed X" |
| 6 | Sound | vox-doc-sound: `cues.tsv` on words (PLAYBOOK §7), then `mix.py ... --out mix.wav` | Loudness numbers |
| 7 | Render + QC | `render.py`, then `pictures.py qc` and read `qc.jpg` YOURSELF: wrong picture, tag over a face, sheet line-ups, leftover sparkle. Fix, re-render. Do not show the contact sheet to the user | Open the video for the user and give its full path. **They judge the final video** |

**Never run the voice first and the pictures later.** The pictures depend only on the
script's words; start them in the same turn the script is approved (users noticed and
objected when this was done in sequence).

## Rules that are easy to forget

- **Voice:** Hindi, Hinglish and every Indian language are voiced with Indic Parler-TTS (Kaggle), never Kokoro, whose Hindi is flat. Hindi and Hinglish start with speaker **Aman**; offer Kabir, Bhanu, Dinesh or Aakash only if the user wants a change (Rohit sounds robotic). English and other languages use Kokoro (`--speed 1.0`). Parler uses make_parler_job.py's defaults (`natural` description, seed 11) and is NEVER sped up: no `--tempo`, ever (1.10x made Hindi robotic). vo_join adds the approved pauses itself (Indian +0.3 s, others +0.35 s); a line it flags `RE-MAKE` is voiced again with another seed. Counter sounds go on the same word as the counter's `+cue`.
- **Never swap in another voice engine on your own** (Edge/Azure voices such as Madhur,
  Google TTS, Piper, MMS, gTTS), not even "temporarily". The user did not choose it, the film
  would need re-timing, and those licences are not cleared for this pack.
- **Where Parler runs is the user's decision.**
  - SETUP Step 0 records the machine as strong (an NVIDIA GPU with ≥ 8 GB VRAM, or ≥ 16 GB
    RAM) or weak. Kaggle is the default either way.
  - If the Kaggle job is QUEUED, or the user would rather run it locally, follow PLAYBOOK §4
    "Kaggle queue": stop and ASK, with the options and their honest cost on THIS machine.
  - Do what the user picks. Never decide alone.
- **Strict Character Consistency Invariant:**
  1. Analyze the entire script first and identify all unique characters required (one or multiple).
  2. Use Google Flow to generate canonical reference images for each character first (`img/ref_<name>.jpg`).
  3. For every scene in `SHOTS.tsv`, identify which character(s) are needed and supply their exact reference image (`ref` column).
  4. Google Flow runs image-to-image with that reference to anchor facial features, clothing, proportions, and art style.
  5. Never recreate, regenerate from scratch, or change an already established character across scenes.
- Scene pictures are full, natural scenes (leave SHOTS `space` empty).
  NEVER USE STANDALONE FULL-SCREEN "card" ROWS (`img = "card"`) in `SCENES.tsv`. The scene illustration (`img/sNN.jpg`) must remain continuous on screen; never flash or cut away to a blank or paper card just to show text, questions, or a counter.
  OVERLAY TEXT DIRECTLY ON TOP OF THE SCENE: All emphasis text, questions, and labels must be overlaid on the active scene using the "+" prefix:
    `+<cue>  tag    <TEXT>    auto,0.28    pop`
  Animated number counters must also be overlaid directly on the scene:
    `+<cue>  count  <NUMBER|CAPTION>  0.5,0.5,0.44  rise`
  The renderer automatically places tags in the quietest corner (sky/wall) without covering stickman characters or faces.
- 2-SECOND PACING BUDGET (NOT 3 SECONDS):
  Target a new visual beat (picture cut, sticker pop-in, counter, or overlay tag) every ~2.0 seconds on average (~60 visual beats per 2 minutes; ~150 per 5 minutes).
  In the first 30 seconds (hook), cut even faster (every ~1.2 to 1.5 seconds).
  No frozen shot should stay unchanged for more than 3.5 seconds. Make it dynamic and fast-paced.
- Scene pictures stay still. Motion comes only from stickers, counters and tags popping on the spoken words (PLAYBOOK §9). No zooms, no AI video.
- Pictures and stickers use Nano Banana 2 (Flow shows it as "Nano Banana 2.1"), never Pro: `pictures.py`
  already does this.
- Two stickers must never overlap; render.py separates them. Pin a sticker that sits near a face.
- A sticker only for a thing the line NAMES that the picture does NOT already show. No repeats of the
  picture, no decorations. If none fits, use a cut to a relevant picture.
- Flow swaps files between the scene and sticker folders too: check both `review.jpg` and
  `cutouts.jpg` before picking.
- Every picture is a full-colour scene in the chosen look. Test 2 shots before the batch.
- Text on pictures for numbers, dates, questions, and emphasis: always overlay as tags (`+<cue> tag ...`), never over a face (render.py places tags automatically in quiet spots). Zero standalone card cuts.
- Pick pictures by what they show, not by file number. Flow swaps them in batches.
- Never paste or ask for API keys or tokens in the chat. Keys go in `.env` files the user
  edits.
- On machines with 8 GB of RAM or less, keep ffmpeg at `-threads 3` (the scripts do) and run
  one heavy job at a time.
- Hindi and other non-Latin labels go through libass automatically; if a font lacks the
  script, set `STICK_FONT_COMPLEX` to a .ttf that covers it.
- For Claude usage: QC from grids, and suggest a new chat per new video.
