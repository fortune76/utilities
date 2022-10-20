import logging
import os.path
import subprocess

from tools.tools_backend.common import Maker
from utilities.settings import MEDIA_ROOT

log = logging.getLogger(__name__)


class PdfConverter(Maker):
    def __init__(self):
        super().__init__()
        self.__input_dir = os.path.join(MEDIA_ROOT, 'pdfs')
        self.__output_dir = os.path.join(MEDIA_ROOT, 'pdfs_output')

    def pdf2jpg(self, src_file_name: str, dpi: int, out_file_name: str):
        subprocess.call([
            'pdftoppm',
            '-jpeg',
            '-r',
            str(dpi),
            os.path.join(self.__input_dir, src_file_name),
            os.path.join(self.__output_dir, out_file_name),
        ])
        return self.send_file(os.path.join(self.__output_dir, out_file_name))

    @property
    def get_input_dir(self):
        return self.__input_dir
