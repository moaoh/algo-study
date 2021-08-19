s = input()
arr = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=', 'dz=']
# 2: ~[6]
# 3: [7]

cnt = 0
i = 0
while i < len(s) :
	if s[i:i+2] == arr[0] or s[i:i+2] == arr[1] or s[i:i+2] == arr[2]\
	or s[i:i+2] == arr[3] or s[i:i+2] == arr[4] or s[i:i+2] == arr[5] or s[i:i+2] == arr[6]:
		i += 2
		cnt += 1
	elif s[i:i+3] == arr[7] :
		i += 3
		cnt += 1
	else :
		cnt += 1
		i += 1
print(cnt)
