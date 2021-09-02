#! /usr/bin/python3

s_lst = [(0, 0), (1, 0), (1, 1), (0, 1)]

def	main():
	col, row = map(int, input().split())
	square = [input() for _ in range(col)]
	m = 0
	for y in range(col):
		for x in range(row):
			i = 0
			while True:
				if x + i >= row or y + i >= col:
					break
				cont = square[y][x]
				count = 0
				for a, b in s_lst:
					if square[y + b * i][x + a * i] == cont:
						count += 1
				if count == 4:
					if i > m:
						m = i
				i += 1
	print((m + 1) ** 2)


if __name__ == '__main__':
	main()
