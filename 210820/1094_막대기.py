# 문제 : 64cm인 막대를 잘라서 Xcm로 만듦.
# ex) x = 32
# stick -> 64
# stick -> 32 32 total = 32 >= X
# stick -> 32
# == 1

def		minimum(arr) :
	min = arr[0]
	min_idx = 0
	for i, value in enumerate(arr) :
		if value > 1 and min >= value :
			min = value
			min_idx = i
	return min_idx

def		calc_stick(X) :
	arr = [64]
	total = 0
	while total != X :
		idx = minimum(arr)
		arr[idx] = arr[idx] // 2
		total = 0
		for i in arr :
			total += i
		if total < X :
			arr.append(arr[idx])
	print(len(arr))
	return

X = int(input())

if X == 64 :
	print('1')
else :
	calc_stick(X)
