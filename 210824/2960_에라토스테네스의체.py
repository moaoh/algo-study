N, K = map(int, input().split())

arr = [int(x) for x in range(2, N + 1)]
P = min(arr)

cnt = 0
flag = 0
for i in range(2, N + 1) :
	P = i
	for j in range(len(arr)) :
		if arr[j] % P == 0 and arr[j] != 0:
			cnt += 1
			if cnt == K :
				print(arr[j])
				flag = 1
				break
			arr[j] = 0
	if flag == 1:
		break