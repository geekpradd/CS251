class Node(object):
	"""
	Node contains two objects - a left and a right child, both may be a Node or both None,
	latter representing a leaf
	"""
	def __init__(self, left=None, right=None):
		super(Node, self).__init__()
		self.left = left
		self.right = right

	def __str__(self):
		"""
		Default inorder print
		"""
		if self.left is None and self.right is None:
			return "(   )"
		else:
			return "( " + str(self.left) + " " + str(self.right) + " )"

	def __eq__(self, other):
		if self.left is None and self.right is None:
			return other.left is None and other.right is None
		elif other.left is None and other.right is None:
			return False
		else:
			return self.left == other.left and self.right == other.right


def mirrorTree(node):
	"""
	Returns the mirror image of the tree rooted at node
	"""
	if node.left is None:
		return node

	left_mirror = mirrorTree(node.left)
	right_mirror = mirrorTree(node.right)
	return Node(left=right_mirror, right=left_mirror)


def allTrees(n):
	"""
	Returns a list of all unique trees with n internal nodes
	"""
	if n==0:
		return [Node()]
	out = []
	for l in range(1,2*n, 2):
		left = allTrees((l-1)//2)
		right = allTrees((2*n-l-1)//2)
		[[out.append(Node(x,y)) for x in left] for y in right]

	return out



def allSymTrees(n):
	"""
	Returns a list of all unique symmetrical trees with n internal nodes
	"""
	if n==0:
		return [Node()]
	if n%2 == 0:
		return []

	half = (n-1)//2
	return [Node(x, mirrorTree(x)) for x in allTrees(half)]


if __name__ == '__main__':
	for x in allSymTrees(int(input())):
		print(x)
	node = Node(Node(Node(), Node()), Node())
	print(node)