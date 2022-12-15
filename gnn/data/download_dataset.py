import gdown
import os
from zipfile import ZipFile

url = 'https://drive.google.com/file/d/1sAPzKKxLSGvXx83cSSkcfSg2SAD5KDkk/view?usp=share_link'
filedir = os.path.dirname(os.path.realpath(__file__))
output = os.path.join(filedir, 'dataset.zip')
gdown.download(url, output, quiet=False, fuzzy=True)

with ZipFile(output) as zpbj:
    zpbj.extractall(filedir)