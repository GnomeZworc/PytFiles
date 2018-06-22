__version__ = "0.3"
from .get_deep import get_deep_func
from .get_dir import get_dir_func

def get_deep(path):
    return get_deep_func(path)

def get_dir(path):
    return get_dir_func(path)
