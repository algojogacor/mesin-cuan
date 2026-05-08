<div align="center">

```
██████████████████████████████████████████████████████████
█                                                        █
█   ███╗   ███╗███████╗███████╗██╗███╗   ██╗            █
█   ████╗ ████║██╔════╝██╔════╝██║████╗  ██║            █
█   ██╔████╔██║█████╗  ███████╗██║██╔██╗ ██║            █
█   ██║╚██╔╝██║██╔══╝  ╚════██║██║██║╚██╗██║            █
█   ██║ ╚═╝ ██║███████╗███████║██║██║ ╚████║            █
█                                                        █
█          C U A N   V I R A L   A R C H I T E C T      █
█                                                       █
█                                                        █
██████████████████████████████████████████████████████████
```

### *Automate the Fame. Master the Algorithm.*

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![FFmpeg](https://img.shields.io/badge/FFmpeg-7.x-007808?style=flat-square&logo=ffmpeg&logoColor=white)](https://ffmpeg.org)
[![YouTube API](https://img.shields.io/badge/YouTube_API-v3-FF0000?style=flat-square&logo=youtube)](https://developers.google.com/youtube)
[![Gemini](https://img.shields.io/badge/Gemini_AI-2.5_Pro-4285F4?style=flat-square&logo=google)](https://ai.google.dev)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

</div>

---

## 🌐 Language / Bahasa

> **[🇮🇩 Bahasa Indonesia](#-bahasa-indonesia)** &nbsp;|&nbsp; **[🇬🇧 English](#-english)**

---

<br/>

# 🇮🇩 Bahasa Indonesia

## Visi & Misi

> *"Ini bukan bot. Ini arsitek konten berbasis AI yang bekerja tanpa henti — menemukan tren, menulis naskah, merender video sinematik, dan mengupload ke YouTube, semuanya otomatis."*

**Mesin Cuan Viral Architect v5** adalah sistem produksi konten YouTube bertenaga AI yang beroperasi penuh 24/7. Ia bukan sekadar script; ia adalah **pabrik video otonom** yang memahami algoritma, mendeteksi tren sebelum viral, dan mengeksekusi setiap frame dengan presisi sinematik.

Bayangkan memiliki tim produksi lengkap — riset tren, penulis naskah, voice-over artist, video editor, dan manajer upload — yang bekerja tanpa istirahat, tanpa gaji, tanpa keluhan. Itulah Mesin Cuan.

---

## ⚙️ Arsitektur 12 Engine

### 📡 Viral Loop Engine
Riset tren real-time menggabungkan **YouTube Data API v3**, **Google Trends**, dan **YouTube Search Suggestions** — diperbarui setiap 6 jam.

### 🧠 Dual Parallel AI Scripting
**Qwen + Ollama generate naskah secara paralel**, lalu saling menilai dengan cross-provider scoring (anti-sycophancy). Skor tertinggi yang lanjut ke produksi. Fallback chain: Ollama → Qwen → Groq.

### 🎯 Script Quality Scorer
Multi-dimensional scoring: **hook strength**, **curiosity gap**, **pacing**, **emotional impact**, **retention prediction** — naskah di bawah threshold otomatis ditulis ulang.

### 🔗 Hook Engine
Auto-inject hook pembuka yang mempertahankan retensi penonton di 3 detik pertama — berbasis data retention analytics per channel.

### 📚 Memory Engine
Melacak topik yang sudah diproduksi — mencegah pengulangan konten dan memastikan variasi antar video.

### 🔍 Research Engine
Web research otomatis sebelum penulisan naskah — memastikan fakta akurat dan konteks terkini.

### 📺 Series Engine
Auto-generate konten berseri (Part 1, 2, 3...) dengan cliffhanger logic dan call-back ke episode sebelumnya.

### 🌟 Neon Visuals v5
Renderer video sinematik FFmpeg: **teks glowing neon**, **glassmorphism panels**, **cinematic letterbox** + vignette + color grading.

### 🔊 Smart SFX Mixer
Sound effect otomatis berdasarkan niche: Horror → heartbeat/thunder, Psychology → mind-tone/focus hum, Motivation → crowd cheer/stadium echo.

### 🖼️ Thumbnail Intelligence
AI-driven thumbnail text & style selection berdasarkan niche dan topik — optimasi CTR.

### 📊 OAuth2 Analytics
Integrasi **YouTube Analytics API v2** — dashboard retensi per channel, analisis drop-off, optimasi konten.

### ⚡ Pipeline Estimator
Prediksi ETA untuk batch render multi-channel — estimasi akurat sebelum eksekusi.

---

## 🛠️ Tech Stack

| Komponen | Teknologi | Fungsi |
|---|---|---|
| **Bahasa** | Python 3.11+ | Orkestrasi pipeline |
| **AI Primary** | Qwen self-hosted + Ollama | Dual parallel script generation + cross-scoring |
| **AI Quality** | Script Quality Scorer | Multi-dimensional validation |
| **AI Vision QC** | NVIDIA API / Ollama Vision | Quality control video |
| **AI Fallback** | Groq | Last-resort script generation |
| **Text-to-Speech** | F5-TTS · Edge TTS · Coqui | 50+ suara multilingual |
| **Rendering** | FFmpeg 7.x | Render video & audio |
| **Footage** | Pexels API · Pixabay API | B-roll footage + clip cache |
| **SFX** | Freesound API | Sound effect otomatis |
| **Upload** | YouTube Data API v3 (OAuth2) | Upload & scheduling |
| **Analytics** | YouTube Analytics API v2 | Retensi & insight |
| **Trending** | YouTube API · Google Trends | Deteksi tren real-time |
| **Research** | Web scraping + NLP | Konteks akurat sebelum naskah |
| **Storage** | Google Drive API v3 | Antrian upload |
| **Notifikasi** | Telegram Bot API | Alert real-time |
| **Scheduler** | APScheduler | Campaign automation |

---

## 🚀 Instalasi & Setup

### Langkah 1 — Clone & Environment

```bash
git clone https://github.com/algojogacor/mesin-cuan.git
cd mesin-cuan

python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Linux / Mac

pip install -r requirements.txt
```

### Langkah 2 — Konfigurasi `.env`

Buat file `.env` di root folder:

```env
# ── AI ───────────────────────────────────────────
GEMINI_API_KEY=your_key
GROQ_API_KEY=your_key
ANTHROPIC_API_KEY=your_key

# ── Footage ───────────────────────────────────────
PEXELS_API_KEY=your_key
PIXABAY_API_KEY=your_key
FREESOUND_API_KEY=your_key          # Opsional

# ── YouTube & Google ──────────────────────────────
YT_API_KEY=your_key
GOOGLE_CLIENT_ID=your_id
GOOGLE_CLIENT_SECRET=your_secret
GOOGLE_DRIVE_FOLDER_ID=your_folder

# ── Notifikasi ────────────────────────────────────
TELEGRAM_BOT_TOKEN=your_token
TELEGRAM_CHAT_ID=your_chat_id

# ── Cloudflare Trends ─────────────────────────────
CF_ACCOUNT_ID=your_id
CF_API_TOKEN=your_token
```

### Langkah 3 — Setup Assets & Auth

```bash
# Download SFX pack + buat folder assets
python tools/setup_assets.py

# OAuth2 YouTube (buka browser, login sekali)
python setup_auth.py

# Verifikasi semua koneksi
python check_requirements.py
```

---

## 💻 Cara Penggunaan

```bash
# Jalankan semua channel sesuai campaign
python main.py

# Jalankan channel tertentu saja
python main.py --channel ch_id_horror

# Jalankan semua channel sekaligus
python main.py --all

# Preview jadwal tanpa render
python main.py --preview

# Test pipeline tanpa upload ke GDrive
python main.py --dry-run

# Skip QC Vision (lebih cepat, untuk testing)
python main.py --skip-qc

# Update dashboard analytics retensi
python main.py --analytics
```

---

<br/>

# 🇬🇧 English

## The Vision

> *"This isn't a bot. It's an AI Video Architect that works around the clock — discovering trends, writing scripts, rendering cinematic footage, and uploading to YouTube, fully automated."*

**Mesin Cuan Viral Architect v5** is a 24/7 AI-powered YouTube content production system. It's not merely a script; it's an **autonomous video factory** that understands the algorithm, detects trends before they peak, and executes every frame with cinematic precision.

Imagine having a complete production team — trend researcher, scriptwriter, voice actor, video editor, and upload manager — working without rest, without salary, without complaints. That's Mesin Cuan.

---

## ⚙️ 12-Engine Architecture

### 📡 Viral Loop Engine
Real-time trend intelligence combining **YouTube Data API v3**, **Google Trends**, and **YouTube Search Suggestions** — refreshed every 6 hours.

### 🧠 Dual Parallel AI Scripting
**Qwen + Ollama generate scripts in parallel**, then cross-score each other (anti-sycophancy). Highest-scoring script proceeds to production. Fallback chain: Ollama → Qwen → Groq.

### 🎯 Script Quality Scorer
Multi-dimensional scoring: **hook strength**, **curiosity gap**, **pacing**, **emotional impact**, **retention prediction** — scripts below threshold are auto-rewritten.

### 🔗 Hook Engine
Auto-injects opening hooks that maintain viewer retention in the first 3 seconds — driven by per-channel retention analytics.

### 📚 Memory Engine
Tracks previously produced topics — prevents content repetition and ensures variety across videos.

### 🔍 Research Engine
Automated web research before script generation — ensures factual accuracy and up-to-date context.

### 📺 Series Engine
Auto-generates multi-part content (Part 1, 2, 3...) with cliffhanger logic and cross-episode callbacks.

### 🌟 Neon Visuals v5
Cinematic FFmpeg renderer: **glowing neon text**, **glassmorphism panels**, **cinematic letterbox** + vignette + color grading.

### 🔊 Smart SFX Mixer
Niche-aware sound effects: Horror → heartbeat/thunder, Psychology → mind-tone/focus hum, Motivation → crowd cheer/stadium echo.

### 🖼️ Thumbnail Intelligence
AI-driven thumbnail text & style selection based on niche and topic — CTR optimization.

### 📊 OAuth2 Analytics
**YouTube Analytics API v2** integration — per-channel retention dashboard, drop-off analysis, content optimization.

### ⚡ Pipeline Estimator
ETA prediction for multi-channel batch renders — accurate estimation before execution.

---

## 🛠️ Tech Stack

| Layer | Technology | Role |
|---|---|---|
| **Language** | Python 3.11+ | Pipeline orchestration |
| **AI Primary** | Qwen self-hosted + Ollama | Dual parallel script generation + cross-scoring |
| **AI Quality** | Script Quality Scorer | Multi-dimensional validation |
| **AI Vision QC** | NVIDIA API / Ollama Vision | Automated quality control |
| **AI Fallback** | Groq | Last-resort script generation |
| **Text-to-Speech** | F5-TTS · Edge TTS · Coqui | 50+ multilingual voices |
| **Rendering** | FFmpeg 7.x | Video & audio composition |
| **Footage** | Pexels API · Pixabay API | B-roll footage + clip cache |
| **SFX** | Freesound API | Automated sound effects |
| **Upload** | YouTube Data API v3 (OAuth2) | Scheduled uploads |
| **Analytics** | YouTube Analytics API v2 | Retention & insights |
| **Trending** | YouTube API · Google Trends | Real-time trend detection |
| **Research** | Web scraping + NLP | Accurate context before scripting |
| **Storage** | Google Drive API v3 | Upload queue |
| **Notifications** | Telegram Bot API | Real-time alerts |
| **Scheduler** | APScheduler | Campaign automation |

---

## 🚀 Installation & Setup

### Step 1 — Clone & Environment

```bash
git clone https://github.com/algojogacor/mesin-cuan.git
cd mesin-cuan

python -m venv venv
source venv/bin/activate          # Linux / Mac
# venv\Scripts\activate           # Windows

pip install -r requirements.txt
```

### Step 2 — Configure `.env`

Create a `.env` file in the root directory:

```env
# ── AI ───────────────────────────────────────────
GEMINI_API_KEY=your_key
GROQ_API_KEY=your_key
ANTHROPIC_API_KEY=your_key

# ── Footage ───────────────────────────────────────
PEXELS_API_KEY=your_key
PIXABAY_API_KEY=your_key
FREESOUND_API_KEY=your_key          # Optional

# ── YouTube & Google ──────────────────────────────
YT_API_KEY=your_key
GOOGLE_CLIENT_ID=your_id
GOOGLE_CLIENT_SECRET=your_secret
GOOGLE_DRIVE_FOLDER_ID=your_folder

# ── Notifications ─────────────────────────────────
TELEGRAM_BOT_TOKEN=your_token
TELEGRAM_CHAT_ID=your_chat_id

# ── Cloudflare Trends ─────────────────────────────
CF_ACCOUNT_ID=your_id
CF_API_TOKEN=your_token
```

### Step 3 — Asset Bootstrap & Auth

```bash
# Download SFX packs and initialize asset folders
python tools/setup_assets.py

# One-time OAuth2 YouTube authorization (opens browser)
python setup_auth.py

# Verify all connections and dependencies
python check_requirements.py
```

---

## 💻 Usage

```bash
# Run all channels according to campaign schedule
python main.py

# Run a specific channel only
python main.py --channel ch_id_horror

# Run all channels simultaneously
python main.py --all

# Preview campaign schedule without rendering
python main.py --preview

# Full pipeline test without uploading to GDrive
python main.py --dry-run

# Skip QC Vision for faster iteration
python main.py --skip-qc

# Refresh per-channel retention analytics
python main.py --analytics
```

---

<div align="center">

---

## 📜 License

**MIT License** — bebas pakai, modifikasi, dan distribusi untuk keperluan apapun, termasuk komersial.

Lihat [LICENSE](LICENSE) untuk teks lengkap.

---

*Built for creators who refuse to be limited by time.*

```
[ 🤖 AI-POWERED ]  [ 🎬 CINEMATIC ]  [ 📡 VIRAL-READY ]  [ 🔄 24/7 AUTO ]
```

</div>