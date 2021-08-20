#! /usr/bin/python3

def	main():
	s = input().upper()
	out = ''
	m_count = 0
	for i in s:
		count = 0
		pos = s.find(i[0:])
		p_pos = -1
		while pos >= 0 and pos != p_pos and  pos < len(s):
			count += 1
			p_pos = pos
			pos = s.find(i[pos:])
		if count > m_count:
			out = i
			m_count = count
		elif count == m_count:
			out = '?'
	print(out)


if __name__ == '__main__':
	main()
