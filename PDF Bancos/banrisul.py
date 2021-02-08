from PyPDF2.pdf import PageObject
from PyPDF2 import PdfFileReader, PdfFileWriter

file_path = "Banrisul.pdf"
pdf = PdfFileReader(file_path)

with open('Banrisul.txt', 'w', encoding="utf-8") as f:
    for page_num in range(pdf.numPages):
        print('Page: {0}'.format(page_num))
        PageObject = pdf.getPage(page_num)

        try:
            txt = PageObject.extractText()
            print(''.center(100, '-'))
        except:
            pass
        else:
            f.write('Page {0}\n'.format(page_num +1))
            f.write(''.center(100, '-'))
            f.write(txt)
    f.close()
        