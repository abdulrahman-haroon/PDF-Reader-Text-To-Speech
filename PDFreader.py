import pyttsx3
import PyPDF2

pdfFile=open('DoingDataScience.pdf','rb')
pdfReader=PyPDF2.PdfFileReader(pdfFile)
pages = pdfReader.numPages #This is to know the pages in PDF file.
#print(pages)

reader=pyttsx3.init()
for numOfPage in range(16,pages):
    page=pdfReader.getPage(numOfPage)
    text=page.extractText()
    reader.say(text)
    reader.runAndWait()