import sys

remainder = list(range(10))

for i in range(10) :
	num = int(input())
	remainder[i] = num % 42

for i in range(10) :
	for j in range(i + 1, 10) :
		if remainder[i] > remainder[j] :
			tmp = remainder[i]
			remainder[i] = remainder[j]
			remainder[j] = tmp
cnt = 1
for i in range(9) :
	if remainder[i] != remainder[i + 1] :
		cnt += 1
print(cnt)