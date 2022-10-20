import os.path

from django import forms

from tools.models import PdfDocument, JpegOptimize


class Pdf2JpgForm(forms.ModelForm):
    class Meta:
        model = PdfDocument
        fields = ('file_name', 'dpi', 'document', )


class JpegOptimizeForm(forms.ModelForm):
    class Meta:
        model = JpegOptimize
        fields = ('file_name', 'wanted_size', 'document', )
