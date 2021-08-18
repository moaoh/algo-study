c = int(input())
for x in range(c):
	stu = list(map(int, input().split()))
	n = stu[0]
	stu.remove(n)
	mid = sum(stu) / n
	count = 0
	for y in stu:
		if y > mid:
			count += 1
	print(f"{round(count / n * 100, 3):.3f}%")
	
