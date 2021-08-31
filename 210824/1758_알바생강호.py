# 돈 - (받은 등수 - 1)

N = int(input())

tip = []
total = []
for _ in range(N) :
	tip.append(int(input()))

tip.sort()
tip.reverse()

for i in range(N) :
	tip[i] = tip[i] - ((i + 1) - 1)
	if tip[i] < 0 :
		tip[i] = 0
print(sum(tip))