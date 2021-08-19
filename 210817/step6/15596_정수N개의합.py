def		solve(a) :
	amount = 0
	for i in range(len(a)) :
		amount += int(a[i])
	return (amount)

# a = list(map(int, input().split()))
# print(solve(a))