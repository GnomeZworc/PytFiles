#!/usr/bin/python3

import subprocess

def make_dir_func(path):
    command = []
    command.append("mkdir")
    command.append(path)
    if new_path != old_path:
        subprocess.run(command, stdout=subprocess.PIPE)
