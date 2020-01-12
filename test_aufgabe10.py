# test to import functions from other files
from aufgabe10 import potential_top_marks, no_improvement


all_list = [0, 0, 0, 0, 0, 0, 8, 8, 8, 9,
						10, 11, 11, 12, 12, 13, 14, 14, 15, 15,
						16, 16, 17, 17, 18, 19,	21, 21, 23, 23,
						24, 24, 24, 25,	25, 25, 26, 27, 27, 28,
						29, 29,	29, 29, 30, 30, 30, 31, 31, 32,
						34, 35, 36, 36, 37, 38]

anwesend_list = [8, 8, 8, 9, 10, 11, 11, 12, 12, 13,
								14, 14, 15, 15, 16, 16, 17, 17, 18, 19,
								21, 21, 23, 23, 24, 24, 24,	25,	25, 25,
								26, 27, 27,	28,	29, 29, 29, 29, 30, 30,
								30,	31, 31, 32, 34, 35, 36,	36, 37, 38]

check_all_list = [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1]

check_anwesend_list = [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1]
																																
								
test_empty_lst = []

'''
def checker(lst):
	# some list 
	l2=[]
	N=0
	while N < len(l):
		#some instructions with l[N]
		l2.append( l[N] )
		N+=1 
	return l == l2
'''

print(potential_top_marks(all_list))
print(type(potential_top_marks(all_list)))
print()
print(no_improvement(all_list))
print(type(no_improvement(all_list)))
print("---")
print(potential_top_marks(anwesend_list))
print(type(potential_top_marks(anwesend_list)))
print()
print(no_improvement(anwesend_list))
print(type(no_improvement(anwesend_list)))
print("---")
print(potential_top_marks(test_empty_lst))
print(type(potential_top_marks(test_empty_lst)))
print()
print(no_improvement(test_empty_lst))
print(type(no_improvement(test_empty_lst)))


#ergebnis = "Potential Top Marks: {:%}".format(prozent_sehr_gut)
#ergebnis = "Marks if no improvement is made: {}".format(marks)

#print("Potential Top Marks: {:%}".format(potential_top_marks(all_list))

#print("Marks if no improvement is made: {}".format(fuck)
#print("Potential Top Marks: {:%}".format(potential_top_marks(anwesend_list))
#print("Marks if no improvement is made: {}".format(no_improvements(anwesend_list))
#print("Potential Top Marks: {:%}".format(potential_top_marks(test_empty_lst))
#print("Marks if no improvement is made: {}".format(no_improvements(test_empty_lst))
