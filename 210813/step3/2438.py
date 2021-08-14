# 별 찍기 - 1

N = int(input())

for i in range(1, N + 1) :
	star = '*'
	for j in range(i - 1) :
		star += '*'
	print(star)

# for i in range(1, N + 1) :
# 	print('*' * i)