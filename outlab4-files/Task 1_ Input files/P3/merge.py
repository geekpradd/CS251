import numpy as np

data = np.genfromtxt('mumbai_data.csv',dtype=str,delimiter=',').astype('object')
unlock = np.genfromtxt('mumbai_unlock.csv',dtype=str,delimiter=',').astype('object')
# print(list(data))
tl,il,tu,iu,d = (0,0,0,0,0)

for k,ke in enumerate(data[0]):
    if ke.strip()=='Tests':
        tl = k
    elif ke.strip()=='Infected':
        il = k
    elif ke.strip()=='Day':
        d = k

for k,ke in enumerate(unlock[0]):
    if ke.strip()=='Tests':
        tu = k
    elif ke.strip()=='Infected':
        iu = k

data = data.T
unlock = unlock.T
infl = data[il].astype('object')
infu = unlock[iu].astype('object')
pl = np.round(infl[1:].astype(np.float)/data[tl][1:].astype(np.float),decimals=3).astype('object')
pu = np.round(infu[1:].astype(np.float)/unlock[tu][1:].astype(np.float),decimals=3).astype('object')
pu = np.concatenate((['Positivity Rate(UnLock)'],pu))
pl = np.concatenate((['Positivity Rate(Lock)'],pl))
infl[0] = 'Infected(Lock)'
infu[0] = 'Infected(Unlock)'
combined = np.vstack((data[d],infu,infl, pl, pu))
np.savetxt('info_combine.csv',combined.T,delimiter=',',fmt='%s')
