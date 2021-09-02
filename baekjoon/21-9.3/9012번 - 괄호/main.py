t = int(input())

def yes_or_no(s):
	left = 0
	for x in s:
		if x == "(":
			left += 1
		elif x == ")" and left > 0:
			left -= 1
		else:
			return print("NO")
	if left == 0:
		print("YES")
	else:
		print("NO")

for x in range(t):
	s = input()
	yes_or_no(s)
