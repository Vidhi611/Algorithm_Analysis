import time

symp_names = []
symp_names.append("cold")
symp_names.append("cough")
symp_names.append("diarrhea")
symp_names.append("fatigue")
symp_names.append("fever")

dis_names = []
dis_names.append("chicken_pox")
dis_names.append("dengue")
dis_names.append("hepatitis")
dis_names.append("jaundice")
dis_names.append("typhoid")


symptoms = {}
symptoms["cold"] = 'ACGTTC'
symptoms["cough"] = 'TCAGGCC'
symptoms["diarrhea"] = 'GTGCAG'
symptoms["fatigue"] = 'CTTACGT'
symptoms["fever"] = 'ATGCTGA'

symp_names = []
symp_names.append("cold")
symp_names.append("cough")
symp_names.append("diarrhea")
symp_names.append("fatigue")
symp_names.append("fever")

dis_names = []
dis_names.append("chicken_pox")
dis_names.append("dengue")
dis_names.append("hepatitis")
dis_names.append("jaundice")
dis_names.append("typhoid")


symptoms = {}
symptoms["cold"] = 'ACGTTC'
symptoms["cough"] = 'TCAGGCC'
symptoms["diarrhea"] = 'GTGCAG'
symptoms["fatigue"] = 'CTTACGT'
symptoms["fever"] = 'ATGCTGA'

diseases = {}
diseases["chicken_pox"] = {"cold": 2, "cough": 0, "diarrhea": 4, "fatigue": 0, "fever": 6}
diseases["dengue"] = {"cold": 2, "cough": 4, "diarrhea": 0, "fatigue": 2, "fever": 4}
diseases["hepatitis"] = {"cold": 0, "cough": 2, "diarrhea": 2, "fatigue": 4, "fever": 2}
diseases["jaundice"] = {"cold": 0, "cough": 4, "diarrhea": 8, "fatigue": 2, "fever": 6}
diseases["typhoid"] = {"cold": 4, "cough": 2, "diarrhea": 6, "fatigue": 4, "fever": 0}

def KMPSearch(pat, txt):
    m=len(pat)
    n=len(txt)
    lps=[0]*m
    j=0 
    k=0
    computeLPSArray(pat, m, lps)
 
    i=0 
    while (i<n):
        if pat[j]==txt[i]:
            #comp=comp+1
            i+=1
            j+=1
        if j==m:
            #print("Pattern is found at index : ", str(i-j))
            k=k+1
            j=lps[j-1]
        elif i<n and pat[j]!=txt[i]:
            #comp=comp+1
            if j!=0:
                j=lps[j-1]
            else:
                i+=1
    return (k)
 
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
 
def search_disease(seq):
    """
    Searches for diseaes and returs the name of thr disease if diagnosed. 
    Disease is present or not depends on the symptoms
    """
    symp_count = []
    for i in range(len(symp_names)):
        symp_count.append(KMPSearch(symptoms[symp_names[i]], seq))
    for i in range(len(dis_names)):
        flag = 1
        for j in range(len(symp_names)):
            temp3 = diseases[dis_names[i]][symp_names[j]]
            if(ord(str(temp3)) != ord(str(symp_count[j]))):
                flag = 0
                break
        if flag == 1:
            print(dis_names[i])

#txt=input("Enter the text:")
#pat=input("Enter pattern")
#print(len("ACGTTCGACGTTCCTGTGCAGAT"))
#b=appendp("ACGTTCGA","CGTTCGAC")
#print(b)
start_time = time.time()
#for possibilities in b:
    #search_disease(possibilities)
search_disease("ACGTTCGACGTTCCTGTGCAGATGTGCAGTAGTGCAGTGGTGCAGACATGCTGACATGCTGAGATGCTGAATGCTGATAACTGGATGCTGATAATGCTGA")
print("--- %s milli seconds ---" %( (time.time() - start_time)*1000))

#print(KMPSearch)
#print("No of times its repeating : ",k) 

#print("The no of comparisions are : ",comp)
