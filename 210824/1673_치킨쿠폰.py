# plus = 치킨쿠폰 / 도장
# plus // k = (치킨쿠폰 / 도장) / 도장

arr = []
while True : 
	try :
		n, k = map(int, input().split())
		chicken = n
		stamp = n
		while stamp >= k :
			chicken += stamp // k
			stamp = stamp % k + stamp // k
		print(chicken)
	except :
		break