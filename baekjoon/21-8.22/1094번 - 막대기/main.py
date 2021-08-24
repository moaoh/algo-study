# 23 = 16 + 4 + 2 + 1
# 32 = 32
# 64 = 64
# 48 = 32 + 16

x = int(input())
count = 0
n = 64
while x > 0:
	if n > x:
		n = n // 2
	else:
		count += 1
		x -= n
print(count)

