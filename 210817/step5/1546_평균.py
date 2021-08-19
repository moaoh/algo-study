N = int(input())
score = list(map(int, input().split()))

M = 0
for i in range(N) :
	if M < score[i] :
		M = score[i]

amount = 0
for i in range(N) :
	score[i] = ((score[i] / M) * 100)
	amount += score[i]
print(amount / N)
