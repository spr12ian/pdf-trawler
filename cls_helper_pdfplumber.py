import cls_helper_pdfplumber

class PdfPlumberHelper:
    def __init__(self, file_path):
        self.file_path = file_path

    @classmethod
    def open(cls, file_path):
        return cls(file_path)

    def __enter__(self):
        import pdfplumber
        self.pdf = pdfplumber.open(self.file_path)
        return self.pdf

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.pdf.close()

with cls_helper_pdfplumber.open("o2.pdf") as pdf:
    for page in pdf.pages:
        print(page)
        tables = page.extract_tables()
        print(tables)
        for table in tables:
            print(table)
            for row in table:
                print(row)