def		cmp_sub(N) :
	i = 0
	sub1 = 0
	sub2 = 0
	for i in range(len(N) - 1) :		
		if i == 0 :
			sub1 = int(N[i]) - int(N[i + 1])
		else :
			sub2 = int(N[i]) - int(N[i + 1])
			if sub1 != sub2 :
				break ;
	if sub1 == sub2 :
		return (1)
	else :
		return (0)

N = input()
cnt = 0
while int(N) >= 1 :
	if len(N) <= 2:
		cnt += 1
	else :
		cnt += cmp_sub(N)
	N = str(int(N) - 1)
print(cnt)