from django.urls import path
from tools.views import MainPageView, Pdf2Jpg


tools_urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('pdf_to_jpg', Pdf2Jpg.as_view(), name='pdf_to_jpg'),
]