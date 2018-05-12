import sys,collections
try:
	inputfile = sys.argv[1]
except Exception as e:
	print 'Invalid argument.'
try:	
	f = open(inputfile,'r')
except Exception as e:
	print 'Unable to open the file.'
	
lines = f.readlines()
for i in range(len(lines)):
	lines[i] = lines[i].strip('\n')
lines = [x for x in lines if x!='']
lines = lines[::-1]
#print lines
commit = []
var_dict = {}
for line in lines:
	line = line.strip('<').strip('>')
	t = line.replace(' ','').split(',')
	#print t
	if 'commit' in t:
		commit.append(t[0])
	elif 'start' in t:
		pass
	elif t[0][0]=='T' and t[0] not in commit:
		var_dict[t[1]] = int(t[2])

d=collections.OrderedDict(sorted(var_dict.items()))
for key in d:
	print key,d[key],
print

