def permutations(seq):
	if len(seq) < 2:
		return seq
	ans = []
	for i in range(len(seq)):
		char = seq[i]
		rest = seq[:i] + seq[i+1:]
		for p in permutations(rest):
			ans.append(char + rest)
	return ans

seq = input('> ')
permutations = permutations(seq)
for i in range(len(permutations)):
	print(i+1, "-", permutations[i])
	