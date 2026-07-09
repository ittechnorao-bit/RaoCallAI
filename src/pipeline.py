from pathlib import Path

from transcriber import transcribe_file
from translator import translate_to_english
from excel_exporter import save_transcript


class Pipeline:
    """
    RCIS Processing Pipeline

    Current Steps
    -------------
    1. Transcribe Audio
    2. Translate Transcript
    3. Save English Transcript
    4. Save Excel

    Future Steps
    ------------
    5. AI Information Extraction
    6. Generate Reports
    """

    def __init__(self, db):
        self.db = db

    def process(self, audio_file):

        audio_file = str(audio_file)

        try:

            print(f"\nStarting Pipeline : {Path(audio_file).name}")

            # STEP 1 : Transcription
            transcript_file = transcribe_file(audio_file)

            if not transcript_file:

                self.db.update(
                    filepath=audio_file,
                    status="Failed",
                    error="Transcription Failed"
                )

                return False

            # STEP 2 : Read Transcript
            with open(transcript_file, "r", encoding="utf-8") as f:
                original_text = f.read()

            # STEP 3 : Translate
            print("Translating...")

            english_text = translate_to_english(original_text)

            # STEP 4 : Save English TXT
            english_dir = Path(r"D:\RaoCallAI\output\english")
            english_dir.mkdir(parents=True, exist_ok=True)

            english_file = english_dir / f"{Path(audio_file).stem}_en.txt"

            english_file.write_text(
                english_text,
                encoding="utf-8"
            )

            # STEP 5 : Save Excel
            save_transcript(
                Path(audio_file).name,
                original_text,
                english_text
            )

            print("Translation Completed")

            self.db.update(
                filepath=audio_file,
                status="Completed",
                transcript=transcript_file
            )

            print("Pipeline Completed")

            return True

        except Exception as e:

            self.db.update(
                filepath=audio_file,
                status="Failed",
                error=str(e)
            )

            print(e)

            return False