
import io
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

def extract_text_from_pdf(pdf_path):
    text = ""
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
    page_interpreter = PDFPageInterpreter(resource_manager, converter)

    with open(pdf_path, 'rb') as pdf_file:
        for page in PDFPage.get_pages(pdf_file, check_extractable=True):
            page_interpreter.process_page(page)
            text += fake_file_handle.getvalue()  


    converter.close()
    fake_file_handle.close()
    return text

pdf_path = r"C:\Users\gokul\Desktop\Mtech\ARVR\ArVr.pdf"
extracted_text = extract_text_from_pdf(pdf_path)


output=r"C:\Users\gokul\Desktop\DW Lab\6.PdfMiner\doc4.txt"
with open(output, "w", encoding="utf-8", errors="replace") as output_file:
    output_file.write(extracted_text)
    print("success")
