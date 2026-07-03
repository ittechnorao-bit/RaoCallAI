from pathlib import Path

# ===========================
# Rao Call Intelligence Suite
# Configuration
# ===========================

BASE_DIR = Path(r"D:\RaoCallAI")

AUDIO_DIR = BASE_DIR / "audio"

OUTPUT_DIR = BASE_DIR / "output"

TXT_DIR = OUTPUT_DIR / "txt"

EXCEL_DIR = OUTPUT_DIR / "excel"

LOG_DIR = OUTPUT_DIR / "logs"

DB_DIR = OUTPUT_DIR / "database"

TOOLS_DIR = BASE_DIR / "tools"

FFMPEG = TOOLS_DIR / "ffmpeg.exe"

FFPROBE = TOOLS_DIR / "ffprobe.exe"

MODEL_NAME = "base"

SUPPORTED_FORMATS = [
    ".mp3",
    ".wav",
    ".m4a",
    ".amr",
    ".aac",
    ".ogg",
    ".flac",
    ".wma"
]

MAX_WORKERS = 2