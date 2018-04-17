import time
start_time=time.time()
def length(sub,S):
	n=len(S)
	m=len(sub)
	#print("Pattern found at index \n")
	matches=[]
	for i in range(n-m+1):
		for j in range(m):
			if S[i+j] != sub[j]:
				break
		if j==m-1:
			matches.append(str(i))
	return matches

print("Enter main string: ")
S=input()
print("Enter sub-string: ")
sub=input()
m=length(sub,S)
count=len(m)
print(m)
print("Frequency:",+count)
print("--- %s seconds ---" % (time.time() - start_time))
