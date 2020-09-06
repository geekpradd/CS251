# Enter your code here
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument('-ca', action='store', type=str, required=True)
my_parser.add_argument('-ch', action='store', type=str, required=True)

args = my_parser.parse_args()

candies_counter = {}

with open(args.ca, "r") as f:
	lines = f.readlines()
	m = int(lines[0])
	candies = [int(x) for x in lines[1].split()]
	
	for candy in candies:
		candies_counter[candy] = candies_counter.get(candy, 0) + 1

wish_counter = {}
with open(args.ch, "r") as f:
	lines = f.readlines()
	n = int(lines[0])
	for count in range(n):
		wish = lines[count+1]
		current = [int(x) for x in wish.split()]
		if current[0] in wish_counter.keys():
			wish_counter[current[0]].append(current[1])
		else:
			wish_counter[current[0]] = [current[1]]

cost = 0

for candy, amount in candies_counter.items():
	if candy in wish_counter.keys():
		cost += sum(sorted(wish_counter[candy])[-min(len(wish_counter[candy]), amount):])

print(cost)