# 별 찍기 - 2

N = int(input())

# for i in range(1, N + 1) :
# 	space = ''
# 	for j in range(N - i) :
# 		space += ' '
# 	star = '*'
# 	for k in range(i - 1) :
# 		star += '*'
# 	print(space + star)

for i in range(1, N + 1) :
	print(' ' * (N - i), '*' * i, sep = '')
