from config import AUDIO_DIR, SUPPORTED_FORMATS

def scan_audio():

    files = []

    for ext in SUPPORTED_FORMATS:

        files.extend(AUDIO_DIR.rglob(f"*{ext}"))

    files.sort()

    return files