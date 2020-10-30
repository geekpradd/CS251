import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
from scipy import stats
from math import ceil, floor

url="https://api.covid19india.org/csv/latest/case_time_series.csv"

df=pd.read_csv(url)
j = 0
begin = False

data_points = []
day_points = []
for i, row in df.iterrows():
	if (row['Date'].strip() == '15 April'):
		j = i 
		begin = True 
	if begin:
		metric = row['Total Deceased']/(row['Total Deceased'] - row['Daily Deceased'])
		data_points.append(metric)
		day_points.append(len(data_points))

data_points = np.array(data_points)
day_points = np.array(day_points)


slope, intercept, r_value, p_value, std_err = stats.linregress(day_points, data_points)
regression = intercept + slope*day_points

plt.plot(day_points, data_points, 'o', label='H(t)')
plt.plot(day_points, regression, 'r', label='fitted line')

plt.legend()
plt.title("Levitt’s Metric for COVID 19") 
plt.xlabel("Time in Days")
plt.ylabel("Levitt’s Metric H(t)")
plt.savefig('covid.png')

day = ceil((1-intercept)/slope)

print (day)
