#!/usr/bin/env python3
import sys
import os


def gettree(arg, branch):
    dirs = sorted(os.listdir(arg))

    for i in range(0, len(dirs)):
        path = arg + dirs[i]
        if path[-1] != '/':
            path_slash = path + '/'
        filename = os.path.split(path)[-1]
        if os.path.isdir(path):
            if (i == len(dirs) - 1):
                print(branch + '└── ' + filename)
                gettree(path_slash, branch + '    ')
            else:
                print(branch + '├── ' + filename)
                gettree(path_slash, branch + '│   ')
        else:
            if (i == len(dirs) - 1):
                print(branch + '└── ' + filename)
            else:
                print(branch + '├── ' + filename)        

if __name__ == '__main__':
    if len(sys.argv) == 1:
        root = os.getcwd()
        print(root)
        gettree(root, '')
    else:
        root = sys.argv[1]
        print(root)
        gettree(root, '')
