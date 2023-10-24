#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import sys

try:
   args = sys.argv
   sourcearg = args[1]
   findarg = args[2]
   replacearg = args[3]
except:
    print( """Invalid arguments passed. Usage:\n scriptname.py source-path findtring replacetring""")
    sys.exit()

# input from user
confirm = input("Will replace strings in files located in {} and all subfolders. Is this what you want to do? (Y/N)\n".format(sourcearg))
if confirm.lower() != "y" and confirm.lower() != "yes":
    print("Exiting.")
    sys.exit()

count = 0

textfiles = []
for root, dirnames, filenames in os.walk(sourcearg):
    for filename in [s for s in filenames if s.endswith(".txt")]:
        print("Processing: {}".format(filename))
        textfiles.append(os.path.join(root, filename))

findarg, replacearg = list(map(re.escape, [findarg, replacearg]))
for textfile in textfiles:
    with open(textfile, 'r') as f:
            try:
                content, count = re.subn(findarg, replacearg, f.read())
                count += 1
            except UnicodeDecodeError:
                print("ERROR: UnicodeDecodeError")

    with open(textfile, 'w') as f:
        f.write(content)
        count -= 1

print("Replaced {} occurences of {} in {}".format(
    str(count), findarg, sourcearg))
