def count(chicken, n, k):
	if n >= k:
		coupon = n // k
		chicken += n // k
		n = n % k
		n += coupon
		return count(chicken, n, k)
	return chicken

while True:
	try:
		n, k = map(int, input().split())
		chicken = n
		chicken = count(chicken, n, k)
		print(chicken)
	except:
		break


