from ring import *

class Series:
	# Write your code here
	def __init__(self,k,x,n):
		self.k = int(k)
		self.x = int(x)
		self.n = int(n)

	def __iter__(self):
		self.item = RingInt(1,self.n)
		self.i = 0
		return self

	def __next__(self):
		if self.i>=self.k:
			self.i = self.k-1
			raise StopIteration
		else:
			if self.i==0:
				r = self.item
			else:
				self.item = self.item*RingInt(self.x,self.n)/RingInt(self.i,self.n)
				r=self.item
			self.i+=1
			return r

def main():

	in_str = str(input())
	in_list = in_str.split(' ')
	k, x, n = in_list[0], in_list[1], in_list[2]
	
	for ele in Series(k, x, n):
		print(ele)


if __name__=="__main__":
	main()

