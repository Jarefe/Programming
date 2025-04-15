import PyPDF2

pdfObj = open('meetingminutes.pdf', 'rb')
pdfFileReader = PyPDF2.PdfReader(pdfObj)


pageObj = pdfFileReader.pages[0]
print(pageObj.extract_text())