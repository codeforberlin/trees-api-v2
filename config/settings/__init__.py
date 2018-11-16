import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from .base import *
from .local import *

try:
    MEDIA_URL = BASE_URL + MEDIA_URL
    STATIC_URL = BASE_URL + STATIC_URL
except NameError:
    pass
