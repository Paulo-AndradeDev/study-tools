from django.shortcuts import render, redirect
from django.http import HttpResponse
from PyPDF2.utils import PdfReadError
import PyPDF2
import docx
import io

def index(request):
    if request.method == 'POST':
        pdf_file = request.FILES['pdf_file']

        try:
            pdf_reader = PyPDF2.PdfFileReader(io.BytesIO(pdf_file.read()))

            text = ""
            for page_num in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_num)
                text += page.extractText()
            return HttpResponse(f'<pre>{text}</pre>')

        except PdfReadError:

            return HttpResponse("Não foi possível ler o arquivo PDF. Ele está criptografado ou corrompido.")

    return render(request, 'index.html')

def word(request):
    if request.method == 'POST':
        word_file = request.FILES['word_file']
        doc = docx.Document(io.BytesIO(word_file.read()))
        text = ""
        for para in doc.paragraphs:
            if "Licensed to Paulo Andrade - eupauloandrade@gmail.com - 78672813553" not in para.text and para.text.strip():
                text += para.text + '\n'
        return HttpResponse(f'<pre>{text}</pre>')
    return render(request, 'word.html')