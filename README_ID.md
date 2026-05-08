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

> 📖 [🇬🇧 Read in English](README.md)

---

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

Salin `.env.example` ke `.env` dan isi API key kamu:

```bash
cp .env.example .env
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

## ⚡ Quick Start (Mode Minimal)

Cuma butuh **Ollama + FFmpeg** — tanpa API key:

```bash
# 1. Install Ollama dan pull model
ollama pull llama3.3:latest

# 2. Install FFmpeg
# Ubuntu: sudo apt install ffmpeg
# macOS: brew install ffmpeg
# Windows: https://ffmpeg.org/download.html

# 3. Jalankan dengan Ollama saja (skip footage, upload, analytics)
python main.py --channel ch_id_horror --skip-qc
```

Fitur yang jalan tanpa API key: AI scripting (Ollama), TTS (Edge TTS gratis), SFX, render.
Fitur yang butuh key: B-roll footage (Pexels/Pixabay), upload YouTube, Google Drive.

---

<div align="center">

---

## 📜 Lisensi

**MIT License** — bebas pakai, modifikasi, dan distribusi untuk keperluan apapun, termasuk komersial.

Lihat [LICENSE](LICENSE) untuk teks lengkap.

---

*Dibuat untuk kreator yang menolak dibatasi oleh waktu.*

```
[ 🤖 AI-POWERED ]  [ 🎬 CINEMATIC ]  [ 📡 VIRAL-READY ]  [ 🔄 24/7 AUTO ]
```

</div>
