import numpy as np
pop = 20.4e6
data = np.genfromtxt('mumbai_data.csv',dtype=str,delimiter=',').astype('object')
# print(list(data))
test = 0
infected = 0
for k,ke in enumerate(data[0]):
    if ke.strip()=='Tests':
        test = k
    elif ke.strip()=='Infected':
        infected = k
data = data.T
# print(data[infected]c)
p = np.round(data[infected][1:].astype(np.float)/data[test][1:].astype(np.float),decimals=3).astype(str)
data[infected][1:] = p
data[infected][0] = 'Test Positivity rate'
# print(p)
data[test][0] = 'Tests per Million'
data[test][1:] = np.round(data[test][1:].astype(np.float)*1e6/pop).astype(np.int).astype(str)
# print(list(data))
data = data.T
# print(data)
np.savetxt('transformed.csv',data,delimiter=',',fmt='%s')
