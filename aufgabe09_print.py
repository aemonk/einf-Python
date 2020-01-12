# aufgabe09.py
def multtable(a=1, b=9):
	minlen = b*b # calculate the biggest multiplication (integer)
	minlen = len(str(minlen)) # find the length of the biggest number and use it as minlen for the alignment
	
	first_pipe = "{0:>{w}} |".format("", w=minlen)
	print(first_pipe, end=' ') # print first pipe with whitespace
	
	# get first row and all col from a to b
	for i in range(a, b+1):	
		first_row = "{0:>{w}}".format(i, w=minlen) # format align:right
		print(first_row, end=' ')
	print() # next line
	
	# print "-" for the length of the row
	c = (b-a) +2 # (b-a)+1 = differenz der range
	d = c * minlen # differenz * minlen (pro printed number)
	e = d + c + 1 # number characters + diff der range für whitespaces + 1 für die pipe am anfang
	print("-" * e) # print "-" for all characters in the row
	
	# print values in the first row
	for row in range(a,b+1): 
		row_style = "{0:>{w}} |".format(row, w=minlen)
		print(row_style, end=' ')
		
		# iterate over all columns and print row*col (multitable)
		for col in range(a,b+1): 
			col_style = "{multi:>{w}}".format(multi=row*col, w=minlen)
			print(col_style, end=' ')

		print() # next line (row)
		
	print()
		
if __name__ == '__main__':
	multtable()
#	multtable(a=99, b=104)
#	multtable(a=3, b=9)
#	multtable(a=1, b=13)
