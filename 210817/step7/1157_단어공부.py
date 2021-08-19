s = input()
s = s.upper()

alpha = ""
for i in range(len(s)) :
	if alpha.find(s[i])  == -1:
		alpha += s[i]

cnt = [0 for _ in range(len(alpha))]
for i in range(len(alpha)) :
	for j in range(len(s)) :
		if alpha[i] == s[j] :
			cnt[i] += 1

max = cnt[0]
max_c = alpha[0]
for i in range(len(cnt) - 1) :
	if max < cnt[i + 1] :
		max = cnt[i + 1]
		max_c = alpha[i + 1]

count = 0
for i in range(len(cnt)) :
	if max == cnt[i] :
		count += 1
if count > 1 :
	max_c = '?'
print(max_c)