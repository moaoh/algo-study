S = input()
alphabet = [chr(x) for x in range(97, 123)]
arr = [int(-1) for x in range(len(alphabet))]

# 97 - 122
for i in range(len(alphabet)) : 
	for j in range(len(S)) :
		if alphabet[i] == S[j] :
			arr[i] = int(j)
			break ;

for i in range(len(alphabet)) :
	print(arr[i], end = " ")
print()
