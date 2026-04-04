from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

def generate_pdf(_filename, _num_pages, _directory="sample_pdfs"):
    filepath = os.path.join(_directory, _filename)
    os.makedirs(_directory, exist_ok=True)

    pdf=canvas.Canvas(filepath, pagesize=A4)
    width, height = A4

    for page_number in range(1,_num_pages+1):
        text=f"File {_filename} page {page_number} / {_num_pages}"
        pdf.drawString(width/2, height/2, text)
        pdf.showPage()
    pdf.save()

if __name__ == "__main__":
    # filename = "output.pdf"
    # num_pages = 5
    filename=input("Enter the filename: ")+".pdf"
    num_pages=int(input("Enter the number of pages: "))
    generate_pdf(filename, num_pages)
