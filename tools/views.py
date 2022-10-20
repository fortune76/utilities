import logging

from django.http import request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView

from tools.forms import Pdf2JpgForm, JpegOptimizeForm
from tools.models import PdfDocument, JpegOptimize
from tools.tools_backend.optimizers import JpegOptimizer
from tools.tools_backend.pdf_converters import PdfConverter

log = logging.getLogger(__name__)

# Create your views here.
class MainPageView(View):
    template_name = 'tools/main.html'

    def get(self, request: request):
        return render(request, self.template_name)


class Pdf2Jpg(FormView):
    def __init__(self):
        super(Pdf2Jpg, self).__init__()
        self.__pdf_converter = PdfConverter()

    form_class = Pdf2JpgForm
    template_name = 'tools/pdf2jpg.html'
    success_url = reverse_lazy('pdf_to_jpg')

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        data = {'file_name': request.POST['file_name'], 'dpi': request.POST['dpi'], 'document': request.FILES['document']}

        if form.is_valid():
            PdfDocument.objects.create(**data)
            self.__pdf_converter.pdf2jpg(request.FILES['document'].name, request.POST['dpi'], request.POST['file_name'])
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class JpegOptimizeView(FormView):
    def __init__(self):
        super(JpegOptimizeView, self).__init__()
        self.__jpeg_optimizer = JpegOptimizer()

    form_class = JpegOptimizeForm
    template_name = 'tools/jpeg_optimize.html'
    success_url = reverse_lazy('jpeg_optimize')

    def post(self, request: request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        data = {'file_name': request.POST['file_name'], 'wanted_size': request.POST['wanted_size'], 'document': request.FILES['document']}

        if form.is_valid():
            JpegOptimize.objects.create(**data)
            self.__jpeg_optimizer.optimize_jpeg(request.FILES['document'].name, request.POST['wanted_size'])
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

