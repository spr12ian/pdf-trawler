from cls_helper_pytesseract import TesseractHelper
from pdf2image import convert_from_path


class Pdf2ImageHelper:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def convert(self):
        # Convert PDF to images
        images = convert_from_path(self.pdf_path)
        return images


tes = TesseractHelper()
pdf2image = Pdf2ImageHelper("letter-eyes-2025-04-11.pdf")
images = pdf2image.convert()

# Perform OCR on each image
ocr_text = ""
for image in images:
    ocr_text += tes.image_to_string(image) + "\n"

ocr_text.strip()[:3000]  # Show the first 3000 characters if available

print(ocr_text)
