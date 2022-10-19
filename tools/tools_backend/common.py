import os
from pathlib import Path

from django.http import HttpResponse, HttpResponseNotFound

from utilities.settings import MEDIA_ROOT


class Converter:
    def __init__(self, input_dir: str | None = None, output_dir: str | None = None):
        self.__input_dir = input_dir
        self.__output_dir = output_dir

    @staticmethod
    def get_username() -> str:
        return os.getlogin()

    @staticmethod
    def send_file(file: str) -> HttpResponse:
        file_path = Path(file)
        try:
            with open(file, 'r') as fd:
                file_data = fd.read()
            response = HttpResponse(file_data, content_type='application/image')
            response['Content-Disposition'] = f'attachment; filename={file_path.name}'
        except IOError:
            # handle file not exist case here
            response = HttpResponseNotFound('<h1>File not exist</h1>')

        return response

    @staticmethod
    def handle_uploaded_file(file, file_type: str):
        with open(os.path.join(MEDIA_ROOT, file_type) + file.name, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
