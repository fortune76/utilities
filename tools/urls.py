from django.urls import path
from tools.views import MainPageView, Pdf2Jpg, JpegOptimizeView


tools_urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('pdf_to_jpg', Pdf2Jpg.as_view(), name='pdf_to_jpg'),
    path('jpeg_optimize', JpegOptimizeView.as_view(), name='jpeg_optimize'),
]