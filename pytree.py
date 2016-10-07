#!/usr/bin/env python3
import sys
import os

total_dir = 0
total_files = 0


def listdir_nohidden(arg):
    not_hidden = []
    for f in sorted(os.listdir(arg), key=str.lower):
        if not f.startswith('.'):
            not_hidden.append(f)
    return not_hidden


def gettree(arg, branch):
    dirs = listdir_nohidden(arg)

    for i in range(0, len(dirs)):
        path = os.path.join(arg, dirs[i])
        global total_dir
        global total_files
        if os.path.isdir(path):
            if (i == len(dirs) - 1):
                print(branch + '└── ' + dirs[i])
                total_dir += 1
                gettree(path, branch + '    ')
            else:
                print(branch + '├── ' + dirs[i])
                total_dir += 1
                gettree(path, branch + '│   ')
        else:
            if (i == len(dirs) - 1):
                print(branch + '└── ' + dirs[i])
                total_files += 1
            else:
                print(branch + '├── ' + dirs[i])
                total_files += 1             

if __name__ == '__main__':
    if len(sys.argv) == 1:
        root = '.'
        print(root)
        gettree(root, '')
    else:
        root = sys.argv[1]
        print(root)
        gettree(root, '')
    print("")
    print(total_dir, "directories,", total_files, "files")
