from scanner import scan_audio
from transcriber import transcribe_file
from database import Database
from pipeline import Pipeline

print("=" * 60)
print(" Rao Call Intelligence Suite ")
print("=" * 60)

# Connect Database
db = Database()

pipeline = Pipeline(db)

print("Database Connected\n")

files = scan_audio()

print(f"Total Files Found : {len(files)}\n")

new_files = 0

for audio in files:

    if db.register(audio):
        new_files += 1

print(f"New Files Registered : {new_files}")

pending = db.pending()

print(f"Pending Files : {len(pending)}\n")

for audio in pending:

    print("-------------------------------------------")
    print(audio)

    pipeline.process(audio)

    print()
db.close()

print("=" * 60)
print(" RCIS COMPLETED ")
print("=" * 60)