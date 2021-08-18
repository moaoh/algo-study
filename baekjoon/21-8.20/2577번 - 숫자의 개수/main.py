a = int(input())
b = int(input())
c = int(input())
number = str(a * b * c)
print(type(number))
for x in range(10):
	print(number.count(str(x)))
