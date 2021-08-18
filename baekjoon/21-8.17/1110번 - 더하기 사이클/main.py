n = int(input())

save_n = n
count = 0
while(1):
	n =  ((n % 10) + (n // 10)) % 10 + (n % 10) * 10
	count += 1
	if n == save_n:
		break
print(count)