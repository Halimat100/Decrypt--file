import PyPDF2
from reportlab.pdfgen import canvas

class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift

    def decrypt(self, text):
        result = ""
        for char in text:
            if char.isalpha():
                if char.isupper():
                    result += chr((ord(char) - self.shift - 65) % 26 + 65)
                elif char.islower():
                    result += chr((ord(char) - self.shift - 97) % 26 + 97)
            else:
                result += char
        return result

class PDFHandler:
    def __init__(self, output_pdf_path):
        self.output_pdf_path = output_pdf_path

    def create_pdf_with_text(self, text):
        c = canvas.Canvas(self.output_pdf_path)
        y = 750
        for line in text.split('\n'):
            c.drawString(100, y, line)
            y -= 20
        c.save()

class PDFDecryptionTool:
    def __init__(self, input_pdf_path, output_pdf_path, shift):
        self.input_pdf_path = input_pdf_path
        self.output_pdf_path = output_pdf_path
        self.cipher = CaesarCipher(shift)
        self.pdf_handler = PDFHandler(output_pdf_path)

    def process_pdf(self):
        decrypted_text = ""
        with open(self.input_pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text = page.extract_text()
                if text:
                    decrypted_text += self.cipher.decrypt(text) + "\n"
        
        self.pdf_handler.create_pdf_with_text(decrypted_text.strip())


if __name__ == "__main__":
    input_pdf_path = r"C:\Users\USER\Assignment\Fossu_encrypted_pdf.pdf"
    output_pdf_path = "Fossu_decrypted_pdf.pdf"
    shift = 3

    tool = PDFDecryptionTool(input_pdf_path, output_pdf_path, shift)
    tool.process_pdf()
