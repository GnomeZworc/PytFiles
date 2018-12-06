# PytFiles

## Use

* Install the package:
```
pip3 install https://github.com/GnomeZworc/PytFiles/archive/0.5.2.zip
```
* Use package:
```python
from pytfiles import get_deep
get_deep(".")
```

## Function List

* `remove_dir(path)` remove a directory
* `get_dir(path)` send back a list of dict with:
  * A string for the file/dir name
  * A bool to know if the file is a directory
  * A string for the path of the file/dir
* `get_deep(path)` return a list of dict with:
  * A string for the file/dir name
  * A bool to know if the file is a directory
  * A string for the path of the file/dir
  * Another list of dict in recursive
