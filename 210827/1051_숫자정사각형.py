# 같은 줄에 같은 숫자가 있는지 확인
# -> col != arr[row].rfind(value)
# 두 인덱스 값을 비교하는 형식으로 해주었다.
# size 배열에 사각형 크기 저장

arr = []
size = []

def	check_square(row, col, N, M) :
	# 예시로 비교할 인덱스 값을 idx 배열에 넣어줌.
	idx = []
	value = arr[row][col]
	idx.append(col)
	idx.append(arr[row].rfind(arr[row][col]))

	# 같은 value이고 다른 인덱스인 경우를 탐색
	# row 다음 줄부터
	for i in range(row + 1, N) :
		for j in range(M) :
			if arr[i][j] == value and j != arr[i].rfind(value) :
				idx1 = j
				idx2 = arr[i].rfind(value)
				# 가로 세로 길이가 같은지 확인
				# 같으면 size 배열에 추가
				if idx[0] == idx1 and idx[1] == idx2 \
				and i - row == idx[1] - idx[0] :
					size.append(((idx[1] - idx[0]) + 1) ** 2)
	# print(value, row, idx)
	# print(size)
	return

N, M = map(int, input().split())

for _ in range(N) :
	arr.append(input())

for row in range(N) :
	for col in range(M) :
		value = arr[row][col]
		if col != arr[row].rfind(value) :	# 같은 value이고 인덱스가 다른지
			check_square(row, col, N, M)

# size 배열에 저장된 가장 큰 값을 출력
print(max(size))