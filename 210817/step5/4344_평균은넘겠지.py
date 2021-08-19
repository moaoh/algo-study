import sys

C = int(input())
percent = list(range(C))

for i in range(C) :
	student = list(map(int, sys.stdin.readline().split()))
	amount = 0
	average = 0
	for j in range(1, len(student)) :
		amount += student[j]
	average = amount / student[0]
	cnt = 0
	for j in range(1, len(student)) :
		if student[j] > average :
			cnt += 1
	percent[i] = (cnt / student[0]) * 100

for i in range(C) :
	print("%.3f%%" % percent[i])