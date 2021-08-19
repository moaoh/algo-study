a = [0] * 100
s = input()
for x in s:
	a[ord(x.upper())] += 1
m = max(a)
m_list = []
for i, v in enumerate(a):
	if m == a[i]:
		m_list.append(i)
if len(m_list) != 1:
	print("?")
else:
	print(chr(m_list[0]))