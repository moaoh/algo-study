self_num = list(range(1, 10000))

def		find_selfnum(n) :
	dn = n
	n = str(n)
	for i in range(len(n)) :
		dn += int(n[i])
	return (dn)

for n in range(1, 10001) :
	dn = n
	while dn < 10000 :
		dn = find_selfnum(dn)
		if dn < 10000 :
			self_num[dn - 1] = 0

for i in range(len(self_num)) :
	if self_num[i] != 0 :
		print(self_num[i])