from pypdf import PdfReader
from pathlib import Path
import os

PDF_FOLDER = Path("pdfs")
DATA_FOLDER = Path("data")

def pdf_to_string(pdf_name):
    reader = PdfReader(PDF_FOLDER / pdf_name)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def read_new_pdfs():
    for file in PDF_FOLDER.iterdir():

        if not file.is_file():
            continue

        if file.suffix.lower() != ".pdf":
            continue

        file_name = file.stem

        if file_name in processed:
            continue



