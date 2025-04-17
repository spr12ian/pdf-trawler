from PyPDF2 import PdfReader

class PdfReaderHelper:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.reader = PdfReader(pdf_path)
        self.text = ""

    def extract_text(self):
        for page in self.reader.pages:
            self.text += page.extract_text() + "\n"
        return self.text.strip()
    
    
# Load the uploaded PDF file
pdf_path = "/mnt/data/2025-04-08 letter.pdf"
reader = PdfReader(pdf_path)

# Extract text from all pages
pdf_text = ""
for page in reader.pages:
    pdf_text += page.extract_text() + "\n"

pdf_text.strip()[:3000]  # Show the first 3000 characters if available
