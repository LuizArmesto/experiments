from django.shortcuts import render
from django.http import HttpResponse

from django_xhtml2pdf.utils import generate_pdf

def index(request):
    return pdf_view(request, 'index.html')

def pdf_view(request, template):
    resp = HttpResponse(content_type='application/pdf')
    result = generate_pdf(template, file_object=resp)
    return result
