#! /usr/bin/python3

def	main():
	n = int(input())
	lst = [input() for _ in range(n)]
	for s in lst:
		stack = []
		for c in s:
			if c == '(':
				stack.append(c)
			elif c == ')':
				if len(stack) > 0:
					del stack[-1:]
				else:
					stack.append(c)
					break
		if len(stack) > 0:
			print('NO')
		else:
			print('YES')

if __name__ == '__main__':
	main()
