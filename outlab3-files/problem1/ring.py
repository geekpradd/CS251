# Enter your code here

def extendedGCD(a,b):
    if a==0:
        return 0,1,b

    x1,y1,gcd = extendedGCD(b%a,a)
    x = y1 - (b//a)*x1
    y = x1
    return x,y,gcd

class RingInt:
    def __init__(self,v=0,c=1):
        v = int(v)
        c = int(c)
        self.val = v%c
        self.ch = c
        
    def __str__(self):
        return (str(self.val)+'['+str(self.ch) + ']')

    def __add__(self,other):
        if other.ch!=self.ch:
            raise ValueError
        else:
            return RingInt((self.val+other.val),self.ch)

    def __sub__(self,other):
        if other.ch!=self.ch:
            raise ValueError
        else:
            return RingInt((self.val-other.val),self.ch)

    def __mul__(self,other):
        if other.ch!=self.ch:
            raise ValueError
        else:
            return RingInt((self.val*other.val),self.ch)

    def __pow__(self,other):
        return RingInt((self.val**other),self.ch)


    def __truediv__(self,other):
        if other.ch!=self.ch:
            raise ValueError
        x,_,gcd = extendedGCD(other.val,other.ch)
        if other.val==0 or gcd!=1:
            raise ValueError
        else:
            return RingInt((self.val*x),self.ch)

    def __eq__(self,other):
        if other.ch!=self.ch:
            raise ValueError
        else:
            return self.val==other.val