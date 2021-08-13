def	loop():
	a, b = map(int, input().split())
	if a == 0 and b == 0:
		return
	else:
		print(a + b)
		loop()


def main():
	loop()

main()
