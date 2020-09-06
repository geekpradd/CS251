total = 100
s = ""
import random
for _ in range(total):
	x = random.randint(1, 25)
	k = random.randint(1, 35)
	n = random.randint(x+k+1, 2*(x+k))
	s += "{0} {1} {2} 2 \n".format(k, x, n)

with open("cases.txt", "w") as f:
	f.write(s)