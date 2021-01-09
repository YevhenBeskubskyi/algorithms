def factorize(num):
	if num < 2:
		return [num]
	denominators = []
	denominator = 2
	while num > 1:
		if num % denominator == 0:
			denominators.append(denominator)
			num //= denominator
		else:
			denominator += 1
	return denominators

num = int(input('> '))
denominators = factorize(num)
print(num, "-", denominators)