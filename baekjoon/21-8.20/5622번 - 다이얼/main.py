l = [2] * 3 + [3] * 3 + [4] * 3 + [5] * 3 + [6] * 3 + [7] * 4 + [8] * 3 + [9] * 4
s = input()
n = 0
for x in s:
	n += l[ord(x) - ord('A')]
print(n + len(s))