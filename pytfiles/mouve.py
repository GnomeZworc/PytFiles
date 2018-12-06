#!/usr/bin/python3

import subprocess

def mouve_func(new_path, old_path):
    command = []
    command.append("mv")
    command.append(old_path)
    command.append(new_path)
    if new_path != old_path:
        subprocess.run(command, stdout=subprocess.PIPE)
