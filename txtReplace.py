#!/usr/bin/env python2
import os
import re
import sys

try:
   scriptname, source, find, replace = argv
except:
    print( """Invalid arguments passed. Usage:\n scriptname.py source-path find-argument replace-argument""")
    sys.exit()

textfiles = []
for root, dirnames, filenames in os.walk(args.source):
    for filename in filter(lambda s: s.endswith(".txt"), filenames):
        textfiles.append(os.path.join(root, filename))

args.find, args.replace = map(re.escape, [args.find, args.replace])
for textfile in textfiles:
    with open(textfile, 'r') as f:
        content, count = re.subn(args.find, args.replace, f.read())

    with open(textfile, 'w') as f:
        f.write(content)

print "Replaced {} occurences of {} in {}".format(
    str(count), args.find, args.source)
