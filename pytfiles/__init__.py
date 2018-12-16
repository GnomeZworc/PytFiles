__version__ = "0.5.2"
from .function.get_deep import get_deep_func
from .function.get_dir import get_dir_func
from .function.remove_dir import remove_dir_func
from .function.mouve import mouve_func
from .function.make_dir import make_dir_func

def make_dir(path):
    make_dir_func(path)

def mouve(new_path, old_path):
    mouve_func(new_path, old_path)

def get_deep(path):
    return get_deep_func(path)

def get_dir(path):
    return get_dir_func(path)

def remove_dir(path):
    remove_dir_func(path)