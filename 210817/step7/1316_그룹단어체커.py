import sys

N = int(input())
arr = [0 for _ in range(N)]

for i in range(N) :
	arr[i] = input()

cnt = 0
for i in range(N) :
	flag = 0
	j = 0
	for j in range(len(arr[i]) - 1) :
		idx = j
		for k in range(j + 1, len(arr[i])) :
			if arr[i][j] == arr[i][k] :
				if idx + 1 != k :
					flag = 1
				else :
					idx = k
		if flag == 1:
			break ;
	if j + 2 ==  len(arr[i]) or len(arr[i]) == 1:
		cnt += 1
print(cnt)