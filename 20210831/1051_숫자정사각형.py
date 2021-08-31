#! /usr/bin/python3

s_lst = [(0, 0), (1, 0), (1, 1), (0, 1)]

def	search_(start:tuple, square:list):
		end = 0
		endx = len(square[0]) - start[0]
		endy = len(square) - start[1]
		if endx > endy:
			end = endy
		else:
			end = endx
		for j in range(1, end):
			count = 0
			for x, y in s_lst:
				i = square[y * j][x * j]
				if square[start[1]][start[0]] == i:
					count += 1
			if count == 4:
				return (j + 1) ** 2
		return 0

def	main():
	row, col = map(int, input().split())
	square = [input() for _ in range(col)]
	m = 0
	for y in range(col):
		for x in range(row):
			out = search_((x, y), square)
			if out > m:
				m = out
	print(m)


if __name__ == '__main__':
	main()
