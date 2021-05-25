import pathlib

def exist(dir_name):
    dir_name = pathlib.Path.cwd() / dir_name
    if not dir_name.exists():
        pathlib.Path.mkdir(dir_name)
