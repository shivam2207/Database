import sys
import re
import collections
delim = '[+*\-/]'
local_var = []
count = 0
gldict = {}
trans = []
transections = {}
finish_flag = []

def operation(s,i):
	tokens = re.split(delim,s)
	if tokens[0].isdigit():
		val1 = int(tokens[0])
	else:
		val1 = int(local_var[i][tokens[0]])

	if tokens[1].isdigit():
		val2 = int (tokens[1])
	else:
		val2 = int (local_var[i][tokens[1]])

	if '+' in s:
		return val1+val2
	elif '-' in s:
		return val1-val2
	elif '*' in s:
		return val1*val2
	elif '/' in s:
		return val1/val2

def printdict():
	d=collections.OrderedDict(sorted(gldict.items()))
	for key in d:
		print key,d[key],
	print

try:
	file = sys.argv[1]
	k = int(sys.argv[2])

except Exception as e:
	print "Invalid Argument"
	sys.exit(1)

try:
	fd=open(file,'r')
except Exception as e:
	print "Unable to open the file"
	sys.exit(1)


for line in fd:
	if count == 0:
		glvar = line.split(' ')
		for i in range (len(glvar)):
			if i%2 == 0:
				gldict[glvar[i]] = 0
			else:
				gldict[glvar[i-1]] = int(glvar[i])
	else:
		if line != '\n':
			trans.append(line.strip('\n').strip(' '))
		else:
			if len(trans) <=1:
				continue
			t = trans[0].split(' ')
			transections[t[0]] = trans
			trans = []
	count+=1

if len(trans) > 1 :
	t = trans[0].split(' ')
	transections[t[0]] = trans

total = len(transections)
#print total

for i in range (total+1):
	local_var.append({})
	finish_flag.append(0)

cnt = 1
while (True):
	counter = 1
	for counter in range(1,total+1):
		tnum = 'T'+str(counter)
		l = transections[tnum]
		#print 'counter', counter
		if len(l) <= 1 :
			if finish_flag[counter] == 0:
				print '<'+tnum+', commit>'
			finish_flag[counter] = 1
			#print 'finished', counter
			
			continue

		if cnt == 1:
			print '<'+tnum+', start>'
			printdict()

		for count in range(1,k+1):
			
			if 'read' in l[1]:
				t = l[1][4:]
				t = t.strip(' ').strip('(').strip(')').split(',')
				var = t[1]
				try:
					local_var[counter][var] = gldict[t[0]]
				except Exception as e:
					print 'invalid read operation'
					sys.exit(1)

			elif 'write' in l[1]:
				t = l[1][5:]
				t = t.strip(' ').strip('(').strip(')').split(',')
				var = t[1]
				print '<'+tnum+', '+t[0]+', '+str(gldict[t[0]])+'>'
				try:
					gldict[t[0]] = local_var[counter][var]
				except Exception as e:
					print 'invalid write operation'
					sys.exit(1)
				printdict()
				#print gldict

			elif 'output' in l[1]:
				pass
			
			else:
				t = l[1].replace(':','').split('=')
				var = t[0].strip(' ')
				local_var[counter][var] = operation(t[1].strip(' '),counter)

			del l[1]
			if len(l) <= 1:
				if finish_flag[counter] == 0:
					print '<'+tnum+', commit>'
					printdict()
				finish_flag[counter] = 1
				#print counter
				break
		transections[tnum] = l

	cnt +=1
	if sum(finish_flag) == total:
		break
#print gldict