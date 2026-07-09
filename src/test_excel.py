from translator import translate_to_english
from excel_exporter import save_transcript

original = """
મારું નામ આનંદ છે.
હું કેનેડા જવા માંગું છું.
"""

english = translate_to_english(original)

save_transcript(
    "Test_Call.mp3",
    original,
    english
)

print("Excel Created Successfully.")