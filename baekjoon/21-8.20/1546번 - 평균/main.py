n = int(input())
s = list(map(int, input().split()))
rn = 0
max = max(s)
for x in s:
	rn += x/max*100
print(rn / n)