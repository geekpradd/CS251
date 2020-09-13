import csv
import numpy as np 

with open("mumbai_data.csv") as csvfile:
	reader = csv.reader(csvfile)
	data = [[], [], [], []]
	header = False
	for row in reader:
		if not header:
			header = True 
			continue
		for i, item in enumerate(row[1:]):
			data[i].append(int(item))

titles = ["Tests", "Infected", "Recovered", "Deceased"]


output_table = [["Field", "Mean", "Std. Dev."]]


for i, item in enumerate(data):
	array = np.array(item)
	row = [titles[i], "{:.3f}".format(np.mean(array)), "{:.3f}".format(np.std(array))]
	output_table.append(row)

max_length = []
for column in zip(*output_table):
	max_length.append(max([len(item) for item in column]))

space_format = ''

for length in max_length:
	space_format += "{0}\t".format('{{:{}}}'.format(length))

for row in output_table:
	print(space_format.format(*row))
		