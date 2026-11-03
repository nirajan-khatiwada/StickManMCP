# Stickman Hybrid: Antigravity Assistant & Agent Guidelines

You are paired with the user to create complete, viral-style Stickman Hybrid documentary explainers (clean full-colour scene pictures from Google Flow / Nano Banana 2, cut-out stickers that pop in on spoken words, paper collage beats, expressive narration, and professional documentary sound design).

Whenever the user opens this workspace or types **"start"**, **"continue"**, **"stickman hybrid start"**, **"setup"**, or names a **topic**, execute the following protocol:

---

## 1. Global Skill Installation & Synchronization

Antigravity loads global skills from `~/.gemini/config/skills/` (on Windows: `C:\Users\<me>\.gemini\config\skills\`).

1. Ensure the skills are installed and synchronized globally:
   - Copy `skills/stickman-hybrid/` to `~/.gemini/config/skills/stickman-hybrid/`
   - Copy `skills/vox-doc-sound/` to `~/.gemini/config/skills/vox-doc-sound/`
   - If target folders already exist, update them by copying changed files over. **Never delete** existing user data: `.env`, `SETUP_STATUS.md`, `CATALOG.tsv`, or custom sounds in `music/` and `sfx/`.
2. Verify that:
   - `~/.gemini/config/skills/stickman-hybrid/SKILL.md` exists.
   - `~/.gemini/config/skills/vox-doc-sound/SKILL.md` exists.
3. Inform the user in their language (Hinglish / English) that the skills are active globally, so they can trigger `stickman hybrid start` or `stickman hybrid continue` from **any** Antigravity chat or workspace.

---

## 2. One-Time Setup Check (`SETUP_STATUS.md`)

Before generating videos, check `~/.gemini/config/skills/stickman-hybrid/SETUP_STATUS.md`.
If the file is missing or any required step is not ✅:
1. Follow `skills/stickman-hybrid/SETUP.md` (or read `README.md`) step-by-step.
2. Required tools:
   - **Step 0**: Machine profile (OS, RAM, GPU/VRAM, shell).
   - **Step 1**: Node.js 20+ & `flow-connector-cli` (`flow-auto`).
   - **Step 2**: FFmpeg (full build with `libass` and complex font shaping: `winget install Gyan.FFmpeg`).
   - **Step 3**: Python 3.11–3.13 (`numpy`, `pillow`, `scipy`, `soundfile`, `faster-whisper`).
   - **Step 3b**: LaMa watermark remover (`big-lama.pt` in `~/.cache/lama/`, 206 MB).
   - **Step 4**: Expressive TTS / Voiceover pipeline setup (`align.py` + `text2speech` or Kokoro/Kaggle).
   - **Step 5**: Sound kit catalog indexing (`python scripts/index_sfx.py` inside `vox-doc-sound`).
3. Record checkpoints in `SETUP_STATUS.md`.

---

## 3. Project Management

All projects live in `~/StickmanHybrid/<topic-slug>/`:
- **"continue" without topic:** Find the most recently modified `PROGRESS.md` under `~/StickmanHybrid/`; resume that project and report the stage.
- **New topic provided:** Create `~/StickmanHybrid/<slug>/` (short, lowercase, hyphenated) with a fresh `PROGRESS.md`.
- **No topic provided:** Ask in one concise message:
  1. **Topic** (or offer 10 curated documentary questions).
  2. **Language** of narration (English, Hindi, Nepali, etc.).
  3. **Target length** (e.g., 2, 5, or 8 minutes).
- Always work and execute scripts from inside the active project folder.
- After every stage, update `PROGRESS.md` with: stage, ✅ status, chosen look, cast, voice, and user approvals.

---

## 4. End-to-End 7-Stage Pipeline

| # | Stage | Action | Checkpoint |
|---|---|---|---|
| **1** | **Script & Expressive Tags** | Write `SCRIPT.md` and `LINES.tsv`. Format narration with companion skill **text2speech** using natural breath/pause markers (`<short pause>`, `<breath>`, `<sigh>`, `<whispers>`) inside a copyable code block, along with voice recommendations. | **Wait for user's OK on script** |
| **2** | **Look, Cast, & Flow Pictures** | *Start immediately in parallel with Stage 3 upon script approval.* Choose look (`looks/`), write `STYLE.txt`, define cast & reference sheet. Connect Flow: `flow-auto bridge start` in background. Write `SHOTS.tsv` & `ELEMENTS.tsv`. Submit test shots (`pictures.py submit 1 2`), then submit the batch. Run `delama.py --watch` in background. | 1 line: "Look X, N pictures generating while audio is made" |
| **3** | **Voiceover (Audio Merge / TTS)** | *Start immediately in parallel with Stage 2.*<br>• **Path A (Expressive TTS - Recommended):** User generates audio using the tagged script from Stage 1 (Gemini 3.8 TTS, Google Cloud TTS Playground, ElevenLabs, or mic recording) and places `VO.wav` in the project root. Run `align.py --vo VO.wav --lines LINES.tsv --out WORDS.tsv --lang <code>`.<br>• **Path B (Automated):** Indic Parler-TTS on Kaggle (speaker Aman) for Hindi; Kokoro for English. Run `vo_join.py` then `align.py`. | Path A: `WORDS.tsv` word count confirmed.<br>Path B: User approves Aman sample. |
| **4** | **Scenes & Pacing** | Write `SCENES.tsv` mapping shots and stickers to aligned words (`WORDS.tsv`). Run `render.py --pacing` to identify and fix any dead holds with cuts or sticker pop-ins (`+cue`). Completely text-free visuals: NO text, tags, counters, or cards inside the video. Enforce Frame Count Invariant: total frames must ALWAYS be greater than total expected seconds / 3 ($N > T / 3$, expected ~2s per frame). | Table: line → on-screen action |
| **5** | **Collect Pictures** | When Flow queue completes: `pictures.py review` → inspect `review.jpg` & `cutouts.jpg` → write `PICK.tsv` for swaps → `pictures.py pick` → `delama.py` cleans watermarks instantly. | 1 line: "N pictures collected, X replaced" |
| **6** | **Sound Design** | Using `vox-doc-sound`: map whooshes, UI clicks, paper sounds, and ambiences to words in `cues.tsv`. Run `mix.py --vo VO.wav --cues cues.tsv --out mix.wav` (leveled to -14 LUFS). | Report loudness & peak dB |
| **7** | **Render & QC** | Run `render.py` to assemble MP4. Run `pictures.py qc` and inspect `qc.jpg` yourself for sticker alignment, sheet line-ups, or leftover artifacts. Re-render if needed. | Open final MP4 and provide clickable file path |

---

## 5. Non-Negotiable Rules

- **Parallel Execution:** Never run voice and pictures sequentially. Both depend only on the approved script words; initiate both immediately after Stage 1 is approved.
- **File Links:** Always provide clickable links with absolute paths (e.g., `file:///C:/Users/...`).
- **No Hallucinated URLs:** Never invent or guess URLs. Give documented URLs only or direct the user to menu paths.
- **Secrets & API Keys:** Never ask for or paste API keys into chat. Guide the user to place keys in local `.env` files or Kaggle credentials.
- **ABSOLUTELY NO ON-SCREEN TEXT:** Zero text inside the video. No text cards, no question cards, no sticky tags, no labels under stickers, no animated counters, and no bar charts. The voiceover speaks all information; the video displays 100% pure artwork (scene illustrations and cut-out stickers).
- **No Full-Screen Cards:** Never replace the scene picture with an `img="card"` row in `SCENES.tsv` (it flashes a flat amber background between artwork). Keep `img/sNN.jpg` continuous throughout the scene. `render.py` stops with an error if any text, tag, counter, chart, or card row is present. Clean old files: `python scripts/migrate_cards.py SCENES.tsv`.
- **Dynamic Pacing (No Fixed 3-Second Holds):** Visual beats adapt dynamically to each scene: e.g. 1 second for fast or punchy moments, ~2 seconds on average for smooth blend and visual flow, and up to ~3 seconds for emotional beats or complex scenes. In the first 30 s (hook), changes happen faster (generally every 1.2-1.5 s). No unchanged still over 3.5 s without a deliberate reason. Every beat is driven by a spoken word in the narration.
- **Frame Count Invariant ($N > T / 3$):** Total frames / visual beats (scene cuts + sticker pop-ins) must ALWAYS be strictly greater than expected total seconds / 3, never less. Since one frame is expected to take ~2 seconds on average, expected frames $\approx T / 2$ (e.g. 2-minute video: $> 40$ frames minimum, ~60 expected; 5-minute video: $> 100$ frames minimum, ~150 expected).
- **Visual Restraint:** Stickers must never cover character faces. Motion comes from cuts and stickers timed to words—never AI video pans/zooms.
