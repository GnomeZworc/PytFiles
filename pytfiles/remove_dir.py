#!/usr/bin/python3

import subprocess

def remove_dir_func(dir_path):
    command = []
    command.append("rmdir")
    command.append(dir_path)
    subprocess.run(command, subprocess.PIPE).stdout.decode('utf-8')
