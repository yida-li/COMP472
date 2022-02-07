# install pyDF2
import PyPDF2


# importing all the required modules

# creating an object
file = open('freud1.pdf', 'rb')

# creating a pdf reader object
fileReader = PyPDF2.PdfFileReader(file)

text = ''
for i in range(0, fileReader.numPages):
    # creating a page object
    pageObj = fileReader.getPage(i)
    # extracting text from page
    text = text+pageObj.extractText()
print(text)
