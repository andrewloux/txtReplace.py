import sys, os, glob, argparse, fnmatch

parser = argparse.ArgumentParser(description='Mass single argument text file find and replace.')
parser.add_argument('-s','--source', help='Folder containing source text files.', required=True)
parser.add_argument('-f','--find', help='Find argument', required=True)
parser.add_argument('-r','--replace', help='Replace argument', required=True)
args = parser.parse_args()

occurences = 0
 
textfiles = []
for root, dirnames, filenames in os.walk(args.source):
  for filename in fnmatch.filter(filenames, '*.txt'):
      textfiles.append(os.path.join(root, filename))

for textfile in textfiles:
	f = open(textfile,'r')
	contents = f.read()
	count = contents.count(args.find)
	occurences += count
	start = 0
	for i in range(count):
		start = contents.find(args.find,start)
		end = start+len(args.find)
		contents = contents[:start]+args.replace+contents[end:]
		start = start+len(args.replace)		#begin next pass right after what was added
		
	f.close()
	g = open(textfile,'w')
	g.write(contents)
	g.close()
print "Replaced " + str(occurences) + " occurences of " + args.find + " in " + args.source
