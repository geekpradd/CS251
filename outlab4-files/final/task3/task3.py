import numpy as np
from scipy.cluster.vq import kmeans2
import argparse
from matplotlib import pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('--input',action='store',type=str,required=True)
parser.add_argument('--output',action='store',type=str,required=True)
parser.add_argument('--k',action='store',type=int,required=True)
args = parser.parse_args()

inp = plt.imread(args.input)
if inp.dtype != np.dtype('float32'):
    inp = inp/255
sh = list(inp.shape)
# print(sh)
inp = np.reshape(inp,[-1,sh[-1]])
centroid,label = kmeans2(inp,args.k,minit='++')
output = np.reshape(centroid[label],sh)
# print('done')
plt.imsave(args.output,output)
# plt.imshow(output)
# plt.show()