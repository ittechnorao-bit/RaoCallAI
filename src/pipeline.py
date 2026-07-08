from pathlib import Path

from transcriber import transcribe_file


class Pipeline:
    """
    RCIS Processing Pipeline

    Current Steps
    -------------
    1. Transcribe Audio

    Future Steps
    ------------
    2. Translate Transcript
    3. AI Information Extraction
    4. Generate Reports
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