# 세 수

a, b, c = map(int, input().split())

if a == b == c :
	print(a)
elif a != b != c :
	if a > b > c or c > b > a :
		print(b)
	elif a > c > b or b > c > a :
		print(c)
	else :
		print(a)
else :
	if a != b and b == c :
		print(c)
	elif b != c and a == c :
		print(a)
	elif a != c and a == b :
		print(b)

# a != b != c -> a != b and b != c
# -> a != b and b != c and c != a