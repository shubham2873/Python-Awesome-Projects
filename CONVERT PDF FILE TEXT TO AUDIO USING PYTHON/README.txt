Packages Used:
1) pyttsx3: It is a Python library for Text to Speech. It has many functions which will help the machine to communicate with us. It will help the machine to speak to us.

2) PyPDF2: It will help to the text from the PDF. A Pure-Python library built as a PDF toolkit. It is capable of extracting document information, splitting documents page by page, merging documents page by page etc.

Both These Modules need to be installed:
pip install pyttsx3
pip install PyPDF2

Approach:
1) Import the PyPDF2 and pyttsx3 modules.
2) Open the PDF file.
3) Use PdfFileReader() to read the PDF. We just have to give the path of the PDF as the argument.
4) Use the getPage() method to select the page to be read.
5) Extract the text from the page using extractText().
6) Instantiate a pyttsx3 object.
7) Use the say() and runwait() methods to speak out the text.