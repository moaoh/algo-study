A = int(input())
B = int(input())
C = int(input())

amount = str(A * B * C)

for i in range(10) :
	cnt = 0
	for j in range(len(amount)) :
		if amount[j] == str(i) :
			cnt += 1
	print(cnt)