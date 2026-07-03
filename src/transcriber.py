from faster_whisper import WhisperModel
from pathlib import Path
from config import TXT_DIR
import traceback

print("Loading AI Model...")

model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8",
    cpu_threads=4,
    num_workers=1
)

TXT_DIR.mkdir(parents=True, exist_ok=True)


def transcribe_file(audio_file):

    try:
        print(f"Processing: {audio_file.name}")

        segments, info = model.transcribe(
            str(audio_file),task="transcribe",
            beam_size=1,
            vad_filter=True,
            condition_on_previous_text=False,
            temperature=0.0
        )

        lines = []

        for segment in segments:
            text = segment.text.strip()
            if text:
                lines.append(text)

        transcript = "\n".join(lines)

        output_file = TXT_DIR / f"{audio_file.stem}.txt"

        output_file.write_text(transcript, encoding="utf-8")

        return True, audio_file.name

    except Exception as e:

        error_log = TXT_DIR / "errors.log"

        with open(error_log, "a", encoding="utf-8") as f:
            f.write(f"\nERROR in {audio_file.name}\n")
            f.write(traceback.format_exc())
            f.write("\n----------------------\n")

        print(f"FAILED: {audio_file.name}")

        return False, audio_file.name