#! /usr/bin/python3

def	main():
	hour, minute = map(int, input().split())
	total = (60 * hour + minute) - 45
	if total < 0:
		total += 24 * 60
	print(total // 60, total % 60)

if __name__ == '__main__':
	main()
