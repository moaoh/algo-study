n, m = map(int, input().split())
box = []
for x in range(n):
	box.append(list(map(int, input())))

# [y][x]
# [y + n][x]
# [y][x + n]
# [y + n][x + n]

max = 0
for y in range(n):
	for x in range(m):
		c = 0
		while True:
			if y + c >= n or x + c >= m:
				break
			if box[y][x] == box[y + c][x] and \
			box[y + c][x] == box[y][x + c] and \
			box[y][x + c] == box[y + c][x + c]:
				if max < c + 1:
					max = c + 1
			c += 1
print(max * max)