from scanner import scan_audio
from transcriber import transcribe_file

print("=" * 60)
print(" Rao Call Intelligence Suite ")
print("=" * 60)

files = scan_audio()

print(f"\nTotal Files : {len(files)}\n")

results = []

for audio in files:

    try:

        result = transcribe_file(audio)

        results.append(result)

        print("Done")

    except Exception as e:

        print(e)

print()

print("=" * 60)

print("Completed")

print("=" * 60)