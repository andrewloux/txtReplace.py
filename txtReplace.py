import sys, os, re, glob, argparse, fnmatch

parser = argparse.ArgumentParser(description='Mass single argument text file find and replace.')
parser.add_argument('-s','--source', help='Folder containing source text files.', required=True)
parser.add_argument('-f','--find', help='Find argument', required=True)
parser.add_argument('-r','--replace', help='Replace argument', required=True)
args = parser.parse_args()

textfiles = []
for root, dirnames, filenames in os.walk(args.source):
  for filename in fnmatch.filter(filenames, '*.txt'):
      textfiles.append(os.path.join(root, filename))

args.find, args.replace = map(re.escape, [args.find, args.replace])
for textfile in textfiles:
    with open(textfile, 'r') as f:
        content, count = re.subn(args.find, args.replace, f.read())

    with open(textfile, 'w') as f:
        f.write(content)

print "Replaced {} occurences of {} in {}".format(
    str(count), args.find, args.source)
