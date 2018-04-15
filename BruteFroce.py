def length(S,sub):
	n=len(S)
	m=len(sub)
	for i in range(n-m+1):
		for j in range(m):
			if S[i+j] != sub[j]:
				break
		if j==m-1:
			print("Pattern found at index "+ str(i))


print("Enter main string: ")
S=input()
print("Enter sub-string: ")
sub=input()
length(S,sub)
