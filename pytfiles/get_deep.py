#!/usr/bin/python3

if __name__ == '__main__':
    from get_dir import get_dir
else:
    from .get_dir import get_dir

def get_deep(path):
    wia = get_dir(path)
    for elem in wia:
        if elem["is_dir"] == True:
            print (elem["name"])
            elem["deep"] = get_deep(path + "/" + elem["name"])
    return wia

if __name__ == '__main__':
    print (get_deep(".."))
