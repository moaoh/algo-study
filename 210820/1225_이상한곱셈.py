a, b = input().split()

def		sum(n) :
	sum = 0
	for i in n :
		sum += int(i)
	return (sum)

if len(a) > len(b) :
	short = b
	long = sum(a)
else :
	short = a
	long = sum(b)

sum = 0
for i in short :
	sum += long * int(i)
print(sum)