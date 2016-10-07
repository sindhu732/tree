#!/usr/bin/env python3
import sys
import os


def gettree(arg, branch):
    dirs = sorted(os.listdir(arg))

    for i in range(0, len(dirs)):
        path = os.path.join(arg, dirs[i])
        if os.path.isdir(path):
            if (i == len(dirs) - 1):
                print(branch + '└── ' + dirs[i])
                gettree(path, branch + '    ')
            else:
                print(branch + '├── ' + dirs[i])
                gettree(path, branch + '│   ')
        else:
            if (i == len(dirs) - 1):
                print(branch + '└── ' + dirs[i])
            else:
                print(branch + '├── ' + dirs[i])        

if __name__ == '__main__':
    if len(sys.argv) == 1:
        root = os.getcwd()
        print(root)
        gettree(root, '')
    else:
        root = sys.argv[1]
        print(root)
        gettree(root, '')
