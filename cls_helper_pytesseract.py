import pytesseract


class TesseractHelper:
    def image_to_string(self, image):
        return pytesseract.image_to_string(image)
