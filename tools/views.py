import logging

from django.http import request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView

from tools.forms import Pdf2JpgForm
from tools.models import PdfDocument
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
        log.warning('asd %s', request.FILES)
        data = {'file_name': request.POST['file_name'], 'dpi': request.POST['dpi'], 'document': request.FILES['document']}

        if form.is_valid():
            PdfDocument.objects.create(**data)
            self.__pdf_converter.pdf2jpg(request.FILES['document'].name, request.POST['dpi'], request.POST['file_name'])
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
