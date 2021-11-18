#!/usr/bin/env python3

from urllib import request
from PIL import Image
import codecs
import io

PNG_URL = 'http://www.pythonchallenge.com/pc/def/oxygen.png'

if __name__ == '__main__':
    r = request.urlopen(PNG_URL)
    data = r.read()
    img = Image.open(io.BytesIO(data))
    pass
