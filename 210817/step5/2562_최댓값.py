import sys

arr = list(range(9))

for i in range(9) :
	arr[i] = int(sys.stdin.readline())

max = arr[0]
max_idx = 0
for i in range(8) :
	if max < arr[i + 1] :
		max = arr[i + 1]
		max_idx = i + 1
print(max, max_idx + 1, sep = '\n')