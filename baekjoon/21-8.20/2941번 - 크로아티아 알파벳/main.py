s = input()
l = ['c=' , 'c-' , 'dz=' , 'd-' , 'lj' , 'nj' , 's=' , 'z=']
count = 0
for x in l:
	if x in s:
		count += s.count(x)
		s = s.replace(x, ",")
s = s.split(',')
for x in s:
	count += len(x)
print(count)