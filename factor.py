def factor(mul, add):
	mx = max([abs(mul), abs(add)])*10
	for a in range(mx):
		for b in range(mx):
			if a + b == add and a * b == mul:
				return [a, b]
	for a in range(mx):
		for b in range(mx):
			if a + -b == add and a * -b == mul:
				return [a, -b]
	for a in range(mx):
		for b in range(mx):
			if -a + b == add and -a * b == mul:
				return [-a, b]
	for a in range(mx):
		for b in range(mx):
			if -a + -b == add and -a * -b == mul:
				return [-a, -b]
