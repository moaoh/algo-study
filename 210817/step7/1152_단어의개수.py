s = input()

cnt = 0
for i in range(len(s) - 1) :
	if s[i] != ' ' and s[i + 1] == ' ' :
		cnt += 1
if s[len(s) - 1] != ' ' :
	cnt += 1
print(cnt)