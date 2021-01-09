def powerset(seq):
	ans = [[]]
	for val in seq:
		copy = [list(v) for v in ans]
		for lst in copy:
			lst.append(val)
		ans += copy
	return ans

seq = input('> ')
powerset = powerset(seq)
for i in range(len(powerset)):
	print(i+1, "-", powerset[i])
