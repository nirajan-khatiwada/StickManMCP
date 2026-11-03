# Setup Status for stickman-hybrid (Antigravity)

| Step | Tool / Component | Status | Version / Diagnostics |
|---|---|:---:|---|
| **0** | **Machine Profile** | ✅ | Windows 11, 16 GB RAM, RTX 3050 (4 GB VRAM) |
| **1** | **Node.js & Flow CLI** | ✅ | Node v24.18.0, flow-connector-cli 1.0.12 verified |
| **2** | **FFmpeg Full Build** | ✅ | FFmpeg 6.1.1 (Gyan.dev), FriBidi + HarfBuzz `libass` verified with complex Hindi conjunct shaping |
| **3** | **Python Core Packages** | ✅ | Python 3.12 (numpy, pillow, scipy, soundfile, faster-whisper) |
| **3b** | **LaMa Watermark Remover** | ⏭️ | Ready (download big-lama.pt to ~/.cache/lama/ when cleaning Sparkles) |
| **4** | **Voiceover & Alignment** | ✅ | align.py (faster-whisper) + text2speech expressive tags active |
| **5** | **Sound Kit & Catalog** | ✅ | 1,053 tracks indexed in CATALOG.tsv (878 SFX, 132 ambiences, 43 music beds) |
| **6** | **Global Antigravity Skills** | ✅ | Installed and synchronized in ~/.gemini/config/skills/ |

**Verified Python Executable:** `python` (`C:\Users\Nirajan\AppData\Local\Programs\Python\Python312\python.exe`)
**Fonts:** `PatrickHand-Regular.ttf` (Latin handwriting) and `Kalam-Bold.ttf` (Devanagari / complex scripts)
