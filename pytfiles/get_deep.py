#!/usr/bin/python3

if __name__ == '__main__':
    from get_dir import get_dir_func
else:
    from .get_dir import get_dir_func

def get_deep_func(path):
    wia = get_dir_func(path)
    for elem in wia:
        if elem["is_dir"] == True:
            print (elem["name"])
            elem["deep"] = get_deep_func(path + "/" + elem["name"])
    return wia

if __name__ == '__main__':
    print (get_deep_func(".."))
