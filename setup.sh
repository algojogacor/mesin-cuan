#!/usr/bin/env bash
set -e

echo "╔════════════════════════════════════════════════╗"
echo "║     MESIN CUAN — One-Click Setup Wizard       ║"
echo "╚════════════════════════════════════════════════╝"
echo ""

# Step 1: .env setup
if [ ! -f .env ]; then
    echo "📋 Step 1/4: Creating .env from .env.example..."
    cp .env.example .env
    echo "   ✅ .env created. Edit it with your API keys:"
    echo "      nano .env"
    echo ""
else
    echo "📋 Step 1/4: .env already exists — skipping."
fi

# Step 2: Python venv
if [ ! -d venv ]; then
    echo "🐍 Step 2/4: Creating Python virtual environment..."
    python3 -m venv venv
    echo "   ✅ venv created."
fi

source venv/bin/activate
echo "🐍 Step 2/4: Installing dependencies..."
pip install -q --upgrade pip
pip install -q -r requirements.txt
echo "   ✅ Dependencies installed."

# Step 3: Ollama check
echo "🤖 Step 3/4: Checking Ollama..."
if command -v ollama &> /dev/null; then
    echo "   ✅ Ollama found."
    if ! ollama list | grep -q "llama3.3"; then
        echo "   📥 Pulling llama3.3:latest (this may take a while)..."
        ollama pull llama3.3:latest
    else
        echo "   ✅ llama3.3 already pulled."
    fi
else
    echo "   ⚠️  Ollama not found. Install from https://ollama.com"
fi

# Step 4: Assets
echo "📦 Step 4/4: Setting up assets..."
python tools/setup_assets.py 2>/dev/null || echo "   ⚠️  Assets setup skipped (optional)"

echo ""
echo "╔════════════════════════════════════════════════╗"
echo "║           ✅ SETUP COMPLETE!                   ║"
echo "║                                                ║"
echo "║  Quick start:                                  ║"
echo "║    python main.py --preview                    ║"
echo "║    python main.py --channel ch_id_horror       ║"
echo "║                                                ║"
echo "║  Docker:                                       ║"
echo "║    docker compose up                           ║"
echo "╚════════════════════════════════════════════════╝"
