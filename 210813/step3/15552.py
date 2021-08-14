# 빠른 A + B

# 본격적으로 for문 문제를 풀기 전에 주의해야 할 점이 있다.
# 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다는 점이다.

import sys

T = int(input())

for i in range(T) :
	A, B = map(int, sys.stdin.readline().split())
	print(A + B)