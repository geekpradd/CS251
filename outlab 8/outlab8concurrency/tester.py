import sys
f = open("o",'r')
x = int(sys.argv[1])
a = f.readlines()
if len(a)!=int(sys.argv[1]):
    print("ERROR")
    print("number numbers not equal: {}, {}".format(a,sys.argv[1]))
    exit()
i = 0
if a[i].strip()!="WE":
    print("ERROR")
    print("first line not WE")
    exit()
wc = 0
rc = 0
while i<len(a):
    s = a[i].strip()
    if s=="WE":
        i+=1
        s=a[i].strip()
        if s!="WX":
            print("ERROR")
            print("Something printed between WE and WX")
            print("Line number = {}".format(i))
            break
        wc+=1
    else:
        if rc >= wc:    
            print("ERROR")
            print("more read than write")
            print("Line number = {}".format(i))
            break
        if s=="RS":
            rc+=1
    i+=1

print("successful reads: {}".format(rc))
print("writes: {}".format(wc))