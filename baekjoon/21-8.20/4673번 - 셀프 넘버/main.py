n = []

for x in range(10001):
	n.append(int(0))

for x in range(10000):
	x = int(x)
	num = x
	temp = x
	while temp >= 1:
		num += temp % 10
		temp = temp // 10
	if num < 10000:
		n[num] = 1

for x in range(10000):
	if n[x] == 0:
		print(x)