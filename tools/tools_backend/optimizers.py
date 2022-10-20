import os
import subprocess

from tools.tools_backend.common import Maker
from utilities.settings import MEDIA_ROOT


class JpegOptimizer(Maker):
    def __init__(self):
        super().__init__()
        self.__input_dir = os.path.join(MEDIA_ROOT, 'jpegs')
        self.__output_dir = os.path.join(MEDIA_ROOT, 'jpegs_output')

    def optimize_jpeg(self, file_name: str, wanted_size: int):
        subprocess.call([
            'jpegoptim',
            f'--size={str(wanted_size)}k',
            self.__input_dir + '/' + file_name,
        ])
