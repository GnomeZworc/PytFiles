#!/usr/bin/python3

import os

def get_dir(dir_path):
    response = os.listdir(dir_path)
    ret = []
    i = 0
    for elem in response:
        if not (".BIN" in elem or "System Volume Information" in elem):
            ret.append({})
            ret[i]["name"] = elem
            if os.path.isdir(dir_path + "/" + ret[i]["name"]):
                ret[i]["is_dir"] = True
            else:
                ret[i]["is_dir"] = False
            i += 1
    return ret

if __name__ == '__main__':
    print(get_dir("/"))
