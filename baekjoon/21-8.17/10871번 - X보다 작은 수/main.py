n, x = map(int, input().split())
a_list = list(map(int, input().split()))
for count in a_list:
	if count < x:
		print(count, end=" ")