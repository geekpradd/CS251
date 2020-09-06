# Enter your code here
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument('-inp', action='store', type=str, required=True, dest='inp')
my_parser.add_argument('-out', action='store', type=str, required=True)

args = my_parser.parse_args()
s = ""
with open(args.inp,'r') as f:
    s=f.read().rstrip()
if s[-1]=='\n':
    s=s[:-1]
files = s.split('/')
final = []
for i in files:
    if i == "" or i==".":
        continue
    elif i == "..":
        final = final[:-1]
    else:
        final.append(i)
    # print(final)

s = ''
for i in final:
    s+='/'+i

with open(args.out,'w') as f:
    f.write(s)
