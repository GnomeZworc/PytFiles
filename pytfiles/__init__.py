__version__ = "0.5"
from .get_deep import get_deep_func
from .get_dir import get_dir_func
from .remove_dir import remove_dir_func
from .mouve import mouve_func

def mouve(new_path, old_path):
    mouve_func(new_path, old_path)

def get_deep(path):
    return get_deep_func(path)

def get_dir(path):
    return get_dir_func(path)

def remove_dir(path):
    remove_dir_func(path)
