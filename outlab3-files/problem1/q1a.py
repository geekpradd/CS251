# Enter your code here
import argparse
from ring import RingInt
def s1(k,x,n):
    try:
        # if k==0:
        r = RingInt(1,n)
        fac = RingInt(1,n)
        S = RingInt(1,n)
        for i in range(1,k):
            fac = fac*RingInt(i,n)
            r = r*RingInt(x,n)
            S = S + (r/fac)
            # print(S)
        return S.__str__()
    except ValueError:
        return "UNDEFINED"

def s2(k,x,n):
    try:
        v = RingInt(1,n)
        for i in range(1,x+k-1):
            v = v*RingInt(i, n)
        r = RingInt(x,n)
        fac = [v/v]
        P = RingInt(1,n)
        for i in range(1,k):
            I = RingInt(i,n)
            fac = [fac[j]*(r+I)/(RingInt(1+j,n)) for j in range(i)]
            fac.insert(0,RingInt(1,n))
            s = RingInt(0,n)
            for j in fac:
                s=s+j
            P = P*s
            # print(P)
        return P.__str__() 
    except ValueError:
        return "UNDEFINED"

def s3(k,x,n):
    try:
        S = RingInt(0,n)
        for i in range(1,k+1):
            S = S+RingInt(i,n)**x
        return S.__str__()
    except ValueError:
        return "UNDEFINED" 

my_parser = argparse.ArgumentParser()
my_parser.add_argument('-in', action='store', type=str, required=True, dest='inp')
my_parser.add_argument('-out', action='store', type=str, required=True)

args = my_parser.parse_args()
o = open(args.out,'w')
f = open(args.inp,'r')
for line in f:
    inp = line.rstrip()
    k,x,n,t = [int(i) for i in inp.split(' ')]
    if t==1:
        s = s1(k,x,n)
        o.write(s)
        o.write('\n')
    if t==2:
        s = s2(k,x,n)
        o.write(s)
        o.write('\n')        
    if t==3:
        s = s3(k,x,n)
        o.write(s)
        o.write('\n')
o.close()
f.close()