# X보다 작은 수

N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N) :
	if A[i] < X :
		print(A[i], end = ' ')