N = int(input())
# arr = [int (x) for x in input().split()]
arr = list(map(int, input().split()))

min = arr[0]
for i in range(N - 1) :
	if (min > arr[i + 1]) :
		min = arr[i + 1]
max = arr[0]
for i in range(N - 1) :
	if (max < arr[i + 1]) :
		max = arr[i + 1]
print(min, max)