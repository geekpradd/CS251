# Enter your code here
from functools import reduce

def collapse(L):
	reducer = lambda x: collapse(x) if isinstance(x, list)  else x
	return reduce(lambda x,y: reducer(x) + " " + reducer(y), L)
