class CamelotHelper:
    def __init__(self):
        import camelot

        self.camelot = camelot

    def read_pdf(self, file_path, pages="1"):
        return self.camelot.read_pdf(file_path, pages=pages)

    def show(self, file_path):
        self.camelot.view.show(file_path)   
        
