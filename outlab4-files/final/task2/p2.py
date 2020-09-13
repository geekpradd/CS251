import pandas as pd 
import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('--data', action='store', type=str, required=True)

args = parser.parse_args()

df = pd.read_csv(args.data)

instances = ['i-1.txt', 'i-2.txt', 'i-3.txt']
algorithms = ['round-robin', 'epsilon-greedy', 'ucb', 'kl-ucb', 'thompson-sampling']



for i, instance in enumerate(instances):
	filtered = df[df['instance'] == instance]
	plt.figure(i)
	plt.yscale('log')
	plt.xscale('log')

	for algo in algorithms:
		further = filtered[filtered['algorithm']==algo]

		if algo == 'epsilon-greedy':
			eps = [0.002, 0.02, 0.2]
			for ep in eps:
				f = further[further['epsilon']==ep]
				values = f.horizon.unique()
				ver = []
				hor = []
				for val in values:
					samples = f[f['horizon'] == val].sample(50)
					y = samples.mean(axis=0)['REG']
					hor.append(val)
					ver.append(y)

				plt.plot(hor, ver, label='epsilon-greedy with epsilon=' + str(ep))

		else:
			ver = []
			hor = []
			values = further.horizon.unique()
			for val in values:
				samples = further[further['horizon'] == val].sample(50)
				y = samples.mean(axis=0)['REG']
				hor.append(val)
				ver.append(y)

			plt.plot(hor, ver, label=algo)

	plt.xlabel('horizon')
	plt.ylabel('Regret')
	plt.legend()
	plt.title('Instance {0} - both axes in log scale'.format(i+1))
	plt.savefig('instance{0}.png'.format(i+1))
