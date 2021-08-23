arr = []

while 1 :
	arr.append(input())
	if '0' in arr :
		break

for i in arr :
	if i == '0' :
		break
	if i == i[::-1] :
		print('yes')
	else :
		print('no')