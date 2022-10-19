import os.path

from django.db import models


# Create your models here.
class PdfDocument(models.Model):
    file_name = models.CharField(max_length=64, default='somefile')
    document = models.FileField(upload_to='pdfs/')
    dpi = models.IntegerField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
