import time
start_time = time.time()
def KMPSearch(pat, txt,comp):
    m=len(pat)
    n=len(txt)
    lps=[0]*m
    j=0 
    k=0
    computeLPSArray(pat, m, lps)
 
    i=0 
    while (i<n):
        if pat[j]==txt[i]:
            comp=comp+1
            i+=1
            j+=1
        if j==m:
            print("Pattern is found at index : ", str(i-j))
            k=k+1
            j=lps[j-1]
        elif i<n and pat[j]!=txt[i]:
            comp=comp+1
            if j!=0:
                j=lps[j-1]
            else:
                i+=1
    return (k,comp)
 
def computeLPSArray(pat,m,lps):
    len=0 
    lps[0] 
    i=1
    while i<m:
        if pat[i]==pat[len]:
            len+=1
            lps[i]=len
            i+=1
        else:
            if len!=0:
                len=lps[len-1]
            else:
                lps[i]=0
                i+=1
 
comp=0
txt=input("Enter the text:")
pat=input("Enter pattern")
(k,comp)=KMPSearch(pat,txt,comp)
print("No of times its repeating : ",k) 
print("--- %s seconds ---" % (time.time() - start_time))
print("The no of comparisions are : ",comp)
