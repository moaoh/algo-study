s = input()

# 2 - 9
# len(num) = 8
num = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

time = 0
flag = 0
for i in range(len(s)) :
	for j in range(len(num)) :
		for k in range(len(num[j])) :
			if s[i] == num[j][k] :
				time += (j  + 2) + 1
				flag == 1
				break ;
	if flag == 1:
		break ;
print(time)