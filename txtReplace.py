import sys, os, glob, argparse, fnmatch

parser = argparse.ArgumentParser(description='Mass single argument text file find and replace.')
parser.add_argument('-s','--source', help='Folder containing source text files.', required=True)
parser.add_argument('-f','--Find', help='Find argument', required=True)
parser.add_argument('-r','--Replace', help='Replace argument', required=True)
args = vars(parser.parse_args())

path = str(args['source'])
findarg = str(args['Find'])
replacearg = str(args['Replace'])
occurences = 0
 
textfiles = []
for root, dirnames, filenames in os.walk(path):
  for filename in fnmatch.filter(filenames, '*.txt'):
      textfiles.append(os.path.join(root, filename))

for textfile in textfiles:
	f = open(textfile,'r')
	contents = f.read()
	count = contents.count(findarg)
	occurences += count
	start = 0
	for i in range(count):
		start = contents.find(findarg,start)
		end = start+len(findarg)
		contents = contents[:start]+replacearg+contents[end:]
		start = end+1
	f.close()
	g = open(textfile,'w')
	g.write(contents)
	g.close()
print "Replaced " + str(occurences) + " occurences of " + findarg + " in " + path
