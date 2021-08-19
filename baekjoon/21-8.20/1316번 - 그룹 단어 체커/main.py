t = int(input())
count = 0
for x in range(t):
	s = input()
	ch = 0
	for y in range(ord('a'), ord('z') + 1):
		n = s.count(chr(y))
		if not chr(y) * n in s:
			ch = 1
	if ch == 0:
		count += 1
print(count)