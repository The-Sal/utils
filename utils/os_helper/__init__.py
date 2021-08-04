import os
from .paths import *

def get_current_home_dir():
    return os.path.expanduser('~')

def os_walk(file_name, path):
    for r, d, f in os.walk(path):
        for file in f:
            if file == file_name:
                return os.path.abspath(os.path.join(r, file))


def waste():
    pass