# 알람 시계

hour, min = map(int, input().split())

if min >= 45 :
	print(hour, min - 45, sep = ' ')
elif hour == 0 and min < 45 :
	print('23', (min + 60) - 45, sep = ' ')
else :
	print(hour - 1, (min + 60) - 45, sep = ' ')