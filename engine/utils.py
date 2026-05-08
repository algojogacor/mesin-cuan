"""
utils.py - Helper functions shared across all engines
"""
import os
import json
import logging
import textwrap
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

ANSI_RESET = "\033[0m"
ANSI_BOLD = "\033[1m"
ANSI_DIM = "\033[2m"
ENABLE_CONSOLE_COLOR = not os.getenv("NO_COLOR") and hasattr(os, "isatty") and os.isatty(1)
ANSI_COLORS = {
    "grey": "\033[90m",
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "magenta": "\033[95m",
    "cyan": "\033[96m",
    "white": "\033[97m",
}

LOGGER_NAME_COLORS = {
    "main": "cyan",
    "script_engine": "magenta",
    "script_quality_scorer": "blue",
    "video_engine": "blue",
    "tts_engine": "green",
    "topic_engine": "yellow",
    "footage_engine": "cyan",
    "metadata_engine": "magenta",
    "thumbnail_engine": "magenta",
    "upload_engine": "green",
    "gdrive_engine": "green",
    "qc_engine": "green",
    "qc_vision": "yellow",
    "hook_engine": "magenta",
    "research_engine": "cyan",
    "state_manager": "grey",
}


def _enable_windows_ansi() -> None:
    if os.name != "nt" or not ENABLE_CONSOLE_COLOR:
        return
    try:
        import ctypes

        kernel32 = ctypes.windll.kernel32
        handle = kernel32.GetStdHandle(-11)
        mode = ctypes.c_uint32()
        if kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
            kernel32.SetConsoleMode(handle, mode.value | 0x0004)
    except Exception:
        pass


def _colorize(text: str, color: str | None = None, *, bold: bool = False, dim: bool = False) -> str:
    if not ENABLE_CONSOLE_COLOR:
        return text
    prefixes: list[str] = []
    if bold:
        prefixes.append(ANSI_BOLD)
    if dim:
        prefixes.append(ANSI_DIM)
    if color and color in ANSI_COLORS:
        prefixes.append(ANSI_COLORS[color])
    if not prefixes:
        return text
    return f"{''.join(prefixes)}{text}{ANSI_RESET}"


class ConsoleFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        timestamp = _colorize(
            datetime.fromtimestamp(record.created).strftime("%Y-%m-%d %H:%M:%S"),
            "grey",
            dim=True,
        )
        level_color = {
            logging.DEBUG: "grey",
            logging.INFO: "white",
            logging.WARNING: "yellow",
            logging.ERROR: "red",
            logging.CRITICAL: "red",
        }.get(record.levelno, "white")
        name_color = LOGGER_NAME_COLORS.get(record.name, "white")
        level = _colorize(f"[{record.levelname}]", level_color, bold=record.levelno >= logging.WARNING)
        name = _colorize(f"[{record.name}]", name_color, bold=record.name == "main")
        message = self._colorize_message(record, record.getMessage())
        rendered = f"[{timestamp}] {level} {name} {message}"
        if record.exc_info:
            rendered += "\n" + self.formatException(record.exc_info)
        if record.stack_info:
            rendered += "\n" + self.formatStack(record.stack_info)
        return rendered

    def _colorize_message(self, record: logging.LogRecord, message: str) -> str:
        if any(token in message for token in ("╔", "╠", "╚", "║")):
            return _colorize(message, "cyan", bold=True)
        if "[ETA][BATCH]" in message:
            return _colorize(message, "blue", bold=True)
        if "[ETA][VIDEO]" in message:
            return _colorize(message, "cyan")
        if "✓" in message or "✅" in message or "PASS" in message:
            return _colorize(message, "green")
        if "✗" in message or "FAILED" in message:
            return _colorize(message, "red", bold=True)
        if "▶" in message or "STEP " in message:
            return _colorize(message, "magenta", bold=record.name == "main")
        if record.levelno >= logging.ERROR:
            return _colorize(message, "red", bold=True)
        if record.levelno >= logging.WARNING:
            return _colorize(message, "yellow")
        if record.levelno == logging.DEBUG:
            return _colorize(message, "grey")
        return message


def _box_lines(title: str, subtitle: str | None = None, width: int = 84) -> list[str]:
    inner_width = max(40, width - 4)
    rows = textwrap.wrap(str(title).strip(), inner_width) or [""]
    if subtitle:
        rows.extend(textwrap.wrap(str(subtitle).strip(), inner_width) or [""])
    top = "╔" + ("═" * (inner_width + 2)) + "╗"
    middle = [f"║ {row.ljust(inner_width)} ║" for row in rows]
    bottom = "╚" + ("═" * (inner_width + 2)) + "╝"
    return [top, *middle, bottom]


def log_box(logger: logging.Logger, title: str, subtitle: str | None = None,
            level: int = logging.INFO, width: int = 84) -> None:
    for line in _box_lines(title, subtitle=subtitle, width=width):
        logger.log(level, line)


def log_step_box(logger: logging.Logger, label: str, step_index: int, step_total: int,
                 title: str, subtitle: str | None = None, width: int = 84) -> None:
    heading = f"{label}  STEP {step_index}/{step_total}  {title}"
    log_box(logger, heading, subtitle=subtitle, level=logging.INFO, width=width)

# ─── Logger Setup ─────────────────────────────────────────────────────────────
def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        import sys
        _enable_windows_ansi()
        ch = logging.StreamHandler(
            stream=open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)
        )
        ch.setFormatter(ConsoleFormatter())
        logger.addHandler(ch)

        os.makedirs("logs", exist_ok=True)
        log_date = datetime.now().strftime("%Y%m%d")
        primary_log = f"logs/pipeline_{log_date}.log"
        fallback_log = f"logs/pipeline_{log_date}_{os.getpid()}.log"
        try:
            fh = logging.FileHandler(primary_log, encoding='utf-8')
        except PermissionError:
            try:
                fh = logging.FileHandler(fallback_log, encoding='utf-8')
            except PermissionError:
                fh = None
        if fh:
            fh.setFormatter(formatter)
            logger.addHandler(fh)
        logger.propagate = False

    return logger


# ─── Config Loader ────────────────────────────────────────────────────────────
def load_settings() -> dict:
    with open("config/settings.json", "r", encoding="utf-8") as f:
        return json.load(f)


def get_channel_config(channel_id: str) -> dict:
    settings = load_settings()
    for ch in settings["channels"]:
        if ch["id"] == channel_id:
            return ch
    raise ValueError(f"Channel '{channel_id}' not found in settings.json")


def load_prompt(niche: str, language: str, profile: str = "shorts") -> str:
    """
    Load prompt template.
    - shorts   : templates/prompts/{niche_slug}_{language}.txt
    - long_form: templates/prompts/{niche_slug}_{language}_long.txt
    niche_slug: horror_facts → horror, psychology → psychology
    """
    niche_slug = niche.replace("_facts", "")
    suffix     = "_long" if profile == "long_form" else ""
    path       = f"templates/prompts/{niche_slug}_{language}{suffix}.txt"

    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Prompt tidak ditemukan: {path}\n"
            f"Pastikan file ada di folder templates/prompts/"
        )

    with open(path, "r", encoding="utf-8") as f:
        return f.read()


# ─── File & Path Helpers ──────────────────────────────────────────────────────
def timestamp() -> str:
    # Microseconds menghindari tabrakan nama file saat pipeline berjalan paralel.
    return datetime.now().strftime("%Y%m%d_%H%M%S_%f")


def channel_data_path(channel_id: str, subfolder: str) -> str:
    path = f"data/{channel_id}/{subfolder}"
    os.makedirs(path, exist_ok=True)
    return path


def save_json(data: dict, path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_json(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# ─── Env Helpers ──────────────────────────────────────────────────────────────
def require_env(key: str) -> str:
    val = os.getenv(key)
    if not val:
        raise EnvironmentError(f"Missing required environment variable: {key}")
    return val


# ─── Ollama Model Rotator ───────────────────────────────────────────────────
def get_ollama_model() -> str:
    import random
    logger = get_logger("ollama_rotator")

    preferred = os.getenv("OLLAMA_MODEL", "").strip()
    if preferred:
        logger.info(f"Ollama Model selected from OLLAMA_MODEL: {preferred}")
        return preferred

    candidates = os.getenv("OLLAMA_MODEL_CANDIDATES", "").strip()
    if candidates:
        models = [m.strip() for m in candidates.split(",") if m.strip()]
    else:
        models = [
            # Sudah dites via /api/chat: aktif, non-coder, dan fokus text generation kreatif.
            "minimax-m2.7:cloud",
            "qwen3.5:397b-cloud",
            "deepseek-v3.1:671b-cloud",
            "glm-4.6:cloud",
            "gemma4:31b-cloud",
            "gpt-oss:120b-cloud",
        ]
    chosen = random.choice(models)
    logger.info(f"Ollama Model selected: {chosen}")
    return chosen
