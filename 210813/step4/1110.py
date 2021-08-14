# 더하기 사이클

N = int(input())

i = 1
if N < 10 :
	amount = (N * 10) + N
else :
	amount = int(N % 10) * 10 + int(int(N / 10) + int(N % 10)) % 10
while i and amount != N :
	if amount < 10 :
		amount = (amount * 10) + amount
	else :
		amount = int(amount % 10) * 10 + int(int(amount / 10) + int(amount % 10)) % 10
	i += 1
print(i)
