def fill_primes(n):
	table = [True] * (n + 1)
	table[0] = table[1] = False
	for i in range(2, n + 1):
		if table[i]:
			for j in range(2 * i, n + 1, i):
				table[j] = False
	return table

n = int(input('> '))
primes = fill_primes(n)
for i in range(len(primes)):
	print(i, 'is prime:', primes[i])
