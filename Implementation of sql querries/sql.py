import sys
import re
metafile=open('metadata.txt')
total_record=100
temp_var=0
tab1_col=0
tab2_col=0
tabledict={}
metadata={}

def Arithmatic_cond_check(a,b,opr,c):
	global temp_var
	if '>=' in opr:
		return a>=b
	if '<=' in opr:
		return a<=b
	if '=' in opr:
		return a==b
	if '<' in opr:
		return a<b
	if '>' in opr:
		return a>b
	temp_var+=1		
	return False

def process_meta_data(metalist,total_record):
	global temp_var
	D={}
	i=0
	temp_var+=1
	while i < len(metalist):
		metalist[i]=metalist[i].strip('\r\n ')
		if metalist[i]=='<begin_table>':
			i+=1
			table=metalist[i].strip('\r\n ')
			D[table]=[]
		elif metalist[i]!='<end_table>':
			D[table].append(metalist[i])
		i+=1
		temp_var+=1
	return D

def volatile_data(table1_name,table2_name,col1,col2):
	temp=col1
	col1=col2
	col2=temp

def column_name_change(colname,tablename,total_record):
		global temp_var
		tables=tablename.split(',')
		temp_var+=1
		if colname in metadict[tables[0]] and colname in metadict[tables[1]]:
			global exp
			exp=2
			sys.exit()
		for table in tables:
			if colname in metadict[table]:
				temp_var+=1
				return table+'.'+colname
		temp_var+=1

#{'table2': ['B', 'D'], 'table1': ['A', 'B', 'C'],'table1,table2':[table1.A,...]}
def check_query(query):
	if 'from' not in query:
		print "Error: Invalid Query."
		sys.exit()

def process_column(first,second):
	temp=second
	second=first
	first=temp

def processcsv(tablerows,tablename,total_record):
	global temp_var
	temp_var+=1
	cols=metadict[tablename]
	rows=[]
	temp_var+=1
	for row in tablerows:
		values=map(int,row.strip('\r\n ').split(','))
		D={}
		temp_var+=1
		for i in range(len(values)):
			D[cols[i]]=values[i]
		rows.append(dict(D))
		temp_var+=1
	return rows

def print_table(tablename):
	for colus in tablename:
		for colu in colus:
			print colu
def avg(l):
	summ=0
	global temp_var
	temp_var+=1
	for el in l:
		summ+=el
	return summ*1.0/len(l)

#tabledict={}
def main():
	global metadict
	global tabledict
	global temp_var
	global total_record
	metadict=process_meta_data(metafile.readlines(),total_record)
	for table in metadict:
		tabledict[table]=processcsv(open(table+'.csv').readlines(),table,total_record)
	#{'table2': [{'B': 158, 'D': 11191}, {'B': 773, 'D': 14421}, {'B': 85, 'D': 5117}, 
	#{'B': 811, 'D': 13393}, {'B': 311, 'D': 16116}, {'B': 646, 'D': 5403}, 

	#{'B': 335, 'D': 6309}, {'B': 803, 'D': 12262}, {'B': 718, 'D': 10226}, 
	#{'B': 731, 'D': 13021}], 
	#'table1': [{'A': 922, 'C': 5727, 'B': 158}, {'A': 640, 'C': 5058, 'B': 773}, 

	#{'A': 775, 'C': 10164, 'B': 85}, {'A': -551, 'C': 1534, 'B': 811}, 
	#{'A': -952, 'C': 1318, 'B': 311}, {'A': -354, 'C': 7063, 'B': 646}, 
	#{'A': -497, 'C': 4549, 'B': 335}, {'A': 411, 'C': 10519, 'B': 803}, 
	#{'A': -900, 'C': 9020, 'B': 718}, {'A': 858, 'C': 3668, 'B': 731}]}

	query=sys.argv[1]
	#take query from the command line
	check_query(query.lower())
	#check whether querry contain from or not 
	query=query.replace(', ',',').replace(' ,',',')
	#parse query
	temp_var=total_record
	process_column(temp_var,total_record)
	if query.count('distinct')>1:
		print 'Error: More than one distinct.'
		sys.exit()
	#process_column(temp_var,total_record)
	volatile_data("tab1","tab2",tab1_col,tab2_col)
	if 'distinct(' in query:
		if ',' in query[query.index('('):query.index(')')]:
			print 'Error: Invalid use of distinct'
			sys.exit()
		query=query.replace('(',' ').replace(')','')
	#	process_column(temp_var,total_record)
	#print_table("tab1")
	process_column(temp_var,total_record)
	#process column
	tokens=query.split()
	#split the tokens
	shift=0
	aggr=False
	#agg flag == false
	if tokens[0].lower()!='select':
		#check for select
		print 'Error: Invalid query.'
		#"exit"
		sys.exit()
	if tokens[1].lower()=='distinct':
			shift+=1
			#shift for the distinct
	volatile_data("tab1","tab2",tab1_col,tab2_col)
	#table name		
	table=tokens[3+shift]
		
	#print_table("tab1")
	volatile_data("tab1","tab2",tab1_col,tab2_col)
	#table join
	exp=0
	try:
		try:
			#try for handling the exception
			if ',' in table:
				tabledict[table]=[]
				#table dict contains the info of tables
				tables=table.split(',')
				for x in tabledict[tables[0]]:
					for y in tabledict[tables[1]]:
						#join process
						d1={tables[0]+'.'+key:x[key] for key in x}
						d2={tables[1]+'.'+key:y[key] for key in y}
						d1.update(d2)
						#update the dictionary
						process_column(temp_var,total_record)
						tabledict[table].append(d1)
						#print_table("tab1")
				metadict[table]=[tables[0]+'.'+i for i in metadict[tables[0]]]+[tables[1]+'.'+i for i in metadict[tables[1]]]
				#change the metadata
			else:
				metadict[table]=metadict[table]
				#do nothing
		except:
			exp=1
			#raise exception
			sys.exit()

		#where clause
		if len(tokens) > 4+shift:
			#where clause start
			if tokens[4+shift].lower()=='where':
				condition=reduce(lambda x,y:x+y,tokens[5+shift:])
				#call lamda function
			else:
				print 'error'
				sys.exit()
			if 'and' not in condition:
				#if and is not present in querry
				conds=condition.split('or')
				#print_table("tab1")
				i=0
				process_column(temp_var,total_record)
				while i<len(tabledict[table]):
					#check the query conditions 
					flag=False
					for cond in conds:
						#split on = < > 
						con=re.split('=|<|>',cond)
						try:
							con.remove('')
						except:
							pass
						colname=con[0].strip(' ')
						#print_table("tab1")
						if '.' not in colname and ',' in table:
							#change the col name to table.col name
							colname=column_name_change(colname,table,total_record)
						try:
							value=int(con[1].strip(' '))
							volatile_data("tab1","tab2",tab1_col,tab2_col)
							if Arithmatic_cond_check(tabledict[table][i][colname],value,cond,total_record):
								flag=True
								##
								break
						except:
							value=con[1].strip(' ')
							#print_table("tab1")
							if '.' not in value and ',' in table:
								volatile_data("tab1","tab2",tab1_col,tab2_col)
								value=column_name_change(value,table,total_record)
								#if only one table
							if 	Arithmatic_cond_check(tabledict[table][i][colname],tabledict[table][i][value],cond,total_record):
								if '=' in cond and '<' not in cond and '>' not in cond:
									try:
										volatile_data("tab1","tab2",tab1_col,tab2_col)
										metadict[table].remove(value)
									except:
										pass
								flag=True
								break
					if not flag:
						#check arth flag
						tabledict[table].remove(tabledict[table][i])
					else:
						i+=1
			else:
				conds=condition.split('and')
				#split based on and
				process_column(temp_var,total_record)
				for cond in conds:
					con=re.split('=|<|>',cond)
					try:
						con.remove('')
					except:
						pass
					colname=con[0].strip(' ')
					if '.' not in colname and ',' in table:
						colname=column_name_change(colname,table,total_record)
					i=0
					while i < len(tabledict[table]):
						try:
							value=int(con[1].strip(' '))
							if not Arithmatic_cond_check(tabledict[table][i][colname],value,cond,total_record):
								tabledict[table].remove(tabledict[table][i])
							else:
								i+=1
						except:
							process_column(temp_var,total_record)
							value=con[1].strip(' ')
							#print value
							volatile_data("tab1","tab2",tab1_col,tab2_col)
							if '.' not in value and ',' in table:
								#print_table("tab1")
								value=column_name_change(value,table,total_record)
							if Arithmatic_cond_check(tabledict[table][i][colname],tabledict[table][i][value],cond,total_record):
								if '=' in cond and '<' not in cond and '>' not in cond:
									try:
										metadict[table].remove(value)
									except:
										pass
										#print_table("tab1")
								i+=1
							else:
								tabledict[table].remove(tabledict[table][i])

		volatile_data("tab1","tab2",tab1_col,tab2_col)
		if tokens[1+shift]=='*':
			#-------------------------------------------------------------------#
			cols=metadict[table]
		elif '(' in tokens[1+shift]:
			#---------------aggr-----------------------------------------------#
			process_column(temp_var,total_record)
			aggr=True
			func=tokens[1+shift][:3].lower()
			volatile_data("tab1","tab2",tab1_col,tab2_col)
			col=tokens[1+shift][4:-1]
			if '.' not in col and ',' in table:
				col=column_name_change(col,table,total_record)
			if col not in metadict[table]:
				raise Exception('')
			l=[]
			#print '-'*13
			#print
			print
			print("%10s  |" % tokens[1+shift])
			print
			#print '-'*13
			for row in tabledict[table]:
				l.append(row[col])
			if func=='max':
				print("%10d  |" % max(l))
			elif func=='avg':
				print("%10f  |" % avg(l))
			elif func=='min':
				print ("%10d  |" %min(l))
			elif func=='sum':
				print ("%10d  |" %sum(l))
		 	#print '-'*13
			#print
			volatile_data("tab1","tab2",tab1_col,tab2_col)
			print
		if not aggr:
			if shift==1: # distinct=true
				L=[]
				if tokens[1+shift]!='*':
					#print_table("tab1")
					cols=tokens[1+shift].split(',')

					process_column(temp_var,total_record)
					#print_table("tab1")
					volatile_data("tab1","tab2",tab1_col,tab2_col)
				for row in tabledict[table]:
					l=[]	
					for col in cols:
						if '.' not in col and ',' in table:
							col=column_name_change(col,table,total_record)
						l.append(row[col])
					if tuple(l) not in L:
						volatile_data("tab1","tab2",tab1_col,tab2_col)
						L.append(tuple(l))
				
				#print '-'*(13*len(cols)-1)
				#print
				print
				for key in cols:
					print("%10s |" % key),
				print
				#print
				#print '-'*(13*len(cols)-1)
				for el in L:
					volatile_data("tab1","tab2",tab1_col,tab2_col)
					for e in el:
						print("%10d |" % e),
					print
			else:
				if tokens[1+shift]!='*':
					#print_table("tab1")
					volatile_data("tab1","tab2",tab1_col,tab2_col)
					cols=tokens[1+shift].split(',')
				#print cols	
				for col in cols:
					if '.' not in col and ',' in table:
							#print_table("tab1")
							col=column_name_change(col,table,total_record)
							volatile_data("tab1","tab2",tab1_col,tab2_col)
					if col not in metadict[table]:
						process_column(temp_var,total_record)
						raise Exception('')			

				
				#print '-'*(13*len(cols)-1)
				#print
				print
				for key in cols:
					print("%10s |" % key),
				print
				#print '-'*(13*len(cols)-1)
				#print
				print
				for row in tabledict[table]:

					for col in cols:
						if '.' not in col and ',' in table:
							#print_table("tab1")
							col=column_name_change(col,table,total_record)
						print("%10s |" % row[col]),
					print
			#print '-'*(13*len(cols)-1)
			print
	except:
		if exp==1:
			print 'Error: Table does not exist.'
		elif exp==2:
			print 'Error: Ambigous Column name.'
		else:
			print 'Error: Invalid Column name'
		sys.exit()

main()