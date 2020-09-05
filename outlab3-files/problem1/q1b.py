# Enter your code here
import argparse
import re
from ring import RingInt
my_parser = argparse.ArgumentParser()
my_parser.add_argument('-m', action='store', type=str, required=True, dest='inp')

args = my_parser.parse_args()

msg = open(args.inp, 'r')

lines = msg.readlines()
n = int(lines[0].rstrip())
flag  =False
for l in lines[1:]:
    if flag:
        break
    possible = re.findall('\$\([\d,]+\)#\([\d,]+\)\$',l)
    print(possible)
    for e in possible:
        x,y = e.split(')#(')
        x = x[2:]
        y = y[:-2]
        A = [int(i) for i in x.split(',')]
        B = [int(i) for i in y.split(',')]
        sum = RingInt(0,n)
        for i,a in enumerate(A):
            if a>=n:
                flag=True
                break
            sum = sum+RingInt((i+1)*a,n)
        if flag or (not sum==RingInt(0,n)):
            flag=True
            break
        sum = RingInt(0,n)
        for i,b in enumerate(B):
            if b>=n:
                flag=True
                break
            sum = sum+RingInt((i+1)*b,n)
        
        if flag or (not sum==RingInt(0,n)):
            flag=True
            break
if flag:
    print("CORRUPTED")
else:
    print("OK")