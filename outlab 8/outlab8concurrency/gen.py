import sys
import random
x = int(sys.argv[1])-2
r1 = open("r1.txt","w")
r2 = open("r2.txt","w")
w1 = open("w1.txt","w")
w2 = open("w2.txt","w")
# common = 0
for i in range(x):
    num = str(random.randint(0,100*x)) + "\n"
    if random.random()<0.5:
        r1.write(num)
    else:
        r2.write(num)
    
    if random.random()<0.5:
        w1.write(num)
    else:
        # common+=1
        w2.write(num)

# print("2xNumber of common = {}".format(2*common))
for i in range(x):
    if random.random()<0.5:
        w1.write(str(random.randint(0,100*x)))
        w1.write("\n")
    else:
        w2.write(str(random.randint(0,100*x)))
        w2.write("\n")
r1.write(str(random.randint(0,100*x)))
r2.write(str(random.randint(0,100*x)))
w2.write(str(random.randint(0,100*x)))
w1.write(str(random.randint(0,100*x)))
