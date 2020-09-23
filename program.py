import requests
import fitz
#descarca pdfu ca trebe
url = "https://stirioficiale.ro/storage/26MODEL%20Declaratie%20proprie%20raspundere%202503.pdf"
r = requests.get(url, verify = False, stream = True)
#r.raw.decode_content = True
with open("declaratie.pdf", 'wb') as pdf:
    for chunk in r.iter_content(chunk_size=1024):

         # writing one chunk at a time to pdf file
         if chunk:
             pdf.write(chunk)
#aici bagam semnatura
doc = fitz.open("declaratie.pdf")          # open the PDF
rect = fitz.Rect(385, 625, 500, 675)     # where to put image: use upper left corner
doc[0].insertImage(rect, filename = "semnatura.png")
doc.saveIncr()

#bagam datele hehe
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

packet = io.BytesIO()
# create a new PDF with Reportlab
can = canvas.Canvas(packet, pagesize=letter)
can.drawString(10, 100, "Hello world")
can.save()

#move to the beginning of the StringIO buffer
packet.seek(0)
new_pdf = PdfFileReader(packet)
# read your existing PDF
existing_pdf = PdfFileReader(open("declaratie.pdf", "rb"))
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
# finally, write "output" to a real file
outputStream = open("declaratie.pdf", "wb")
output.write(outputStream)
outputStream.close()
