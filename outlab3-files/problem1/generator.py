total = 100
s1 = ""
s2 = ""
s3 = ""
import random
for _ in range(total):
	x = random.randint(1, 25)
	k = random.randint(1, 35)
	n = random.randint(x+k+1, 2*(x+k))
	s3 += "{0} {1} {2} 3 \n".format(k, x, n)
	s2 += "{0} {1} {2} 2 \n".format(k, x, n)
	s1 += "{0} {1} {2} 1 \n".format(k, x, n)

with open("cases3.txt", "w") as f:
	f.write(s3)
with open("cases2.txt", "w") as f:
	f.write(s2)
with open("cases1.txt", "w") as f:
	f.write(s1)