import sys

N = int(input())
arr = list(range(N))

for i in range(N) :
	arr[i] = sys.stdin.readline()

for i in range(N) :
	o_score = 1
	x_score = 0
	score = 0
	for j in range(len(arr[i])) :
		if arr[i][j] == 'O' :
			score += o_score
			o_score += 1
		else :
			o_score = 1
	print(score)