# 한 번에 한 개의 원판만을 다른 탑으로 옮길 수 있다.
# 쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.
# 이 작업을 수행하는데 필요한 이동 순서를 출력하는 프로그램을 작성하라.
# 단, 이동 횟수는 최소가 되어야 한다.



n = int(input())
stick = [list(range(1, n + 1)), [], []]

def hanoi_tower(n, start, end) :
	if n == 1 :
		print(start, end)
		stick[end - 1].insert(0, stick[start - 1][0])
		del stick[start - 1][0]
		# print(n, start, end, stick)
		return

	hanoi_tower(n - 1, start, 6 - start - end)		# 1단계 1 -> 2
	print(start, end)								# 2단계 1 -> 3
	stick[end - 1].insert(0, stick[start - 1][0])
	del stick[start - 1][0]
	# print(n, start, end, stick)
	hanoi_tower(n - 1, 6 - start - end, end) 		# 3단계 2 -> 3

print((2 ** n) - 1)
# print(stick)
hanoi_tower(n, 1, 3)