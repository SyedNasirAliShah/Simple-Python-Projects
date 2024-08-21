from PyPDF2 import PdfWriter
import os

merger = PdfWriter()
files = [file for file in os.listdir() if file.endswith(".pdf")]
i = 0

for pdf in files:
    if i == 2:# for 2 files only
        break
    else:
        merger.append(pdf)
    i = i + 1

merger.write("mergedPDF.pdf")
merger.close()
print(files)
