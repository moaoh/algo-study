import sys

T = int(input())
arr = []

for i in range(T) :
	R, S = sys.stdin.readline().split()
	R = int(R)
	string = ''
	for j in range(len(S)) :
		string += S[j] * R
	arr.append(string)

for i in range(T) :
	print(arr[i])