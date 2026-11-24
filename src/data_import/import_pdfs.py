from pypdf import PdfReader
from pathlib import Path
import os
import json

PDF_FOLDER = Path("pdfs")
DATA_FOLDER = Path("data")

CSV_FILE = os.path.join(DATA_FOLDER, "shopping_data.csv")
PROCESSED_FILE = os.path.join(DATA_FOLDER, "processed.json")

def pdf_to_string(pdf_name):
    reader = PdfReader(PDF_FOLDER / pdf_name)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def read_new_pdfs():
    processed = load_processed()
    for file in PDF_FOLDER.iterdir():

        if not file.is_file():
            continue

        if file.suffix.lower() != ".pdf":
            continue

        file_name = file.stem

        if file_name in processed:
            continue

        


def load_processed():
    if os.path.exists(PROCESSED_FILE):
        with open(PROCESSED_FILE, "r") as f:
            return json.load(f)
    return {}


def save_processed(processed):
    with open(PROCESSED_FILE, "w") as f:
        json.dump(processed, f, indent=4)



