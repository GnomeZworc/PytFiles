#!/usr/bin/python3

import subprocess
from os.path import exists

def make_dir_func(path):
    command = []
    command.append("mkdir")
    command.append(path)
    if exists(path) == False:
        subprocess.run(command, stdout=subprocess.PIPE)
