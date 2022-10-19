import os.path

from django import forms

from tools.models import PdfDocument


class Pdf2JpgForm(forms.ModelForm):
    class Meta:
        model = PdfDocument
        fields = ('file_name', 'dpi', 'document', )
