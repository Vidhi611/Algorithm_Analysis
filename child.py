import random
import math

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
symptoms["cold"] = 'AC'
symptoms["cough"] = 'TCAGGCC'
symptoms["diarrhea"] = 'GTGCAG'
symptoms["fatigue"] = 'CTTACGT'
symptoms["fever"] = 'ATGCTGA'

diseases = {}
diseases["chicken_pox"] = {"cold": 1, "cough": 0, "diarrhea": 0, "fatigue": 0, "fever": 0}
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
    k=0
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
            #print(dis_names[i])
            k=k+1
    return k

def child(p1,p2):
    l=int(len(p1)/2)
    p1r=[]
    p2r=[]
    #x=[]
    f=0
    #y=[]
    I=math.factorial(2*l)/((math.factorial(l))*(math.factorial(l)))
    #print(len(p1r))
    while(len(p1r)!=I*I):
        x=random.sample(p1,l)
        #print("x=",x)
        if(len(p1r)!=0):
            for string in p1r:
                if(x==string):
                    f=1
                else:
                    f=0
            if(f!=1):
                 p1r.append(x)
        else:
            p1r.append(x)
               
    g=0                  
    while(len(p2r)!=I*I):
        y=random.sample(p2,l)
        if(len(p2r)!=0):
            for j in p2r:
                if(y==j):
                    g=1
                else:
                    g=0
            if(g!=1):
                 p2r.append(y)
        else:
            p2r.append(y)
            
    return p1r,p2r

def appendp(p1,p2):
    List=child(p1,p2)
    print(List)
    print(len(List))
    a=[]
    children=[]
    for i in range(int(len(p1))):
        for j in range(int(len(p2))):
            a.append(List[0][i]+List[1][j])
    for i in range(int(len(p1))):
        for j in range(int(len(p2))):
            a.append(List[1][i]+List[0][j])
    #print("ais",a)
    for i in range(int(len(a))):
        c=''.join(a[i])
        children.append(c)
    return children
    

b=appendp("ACGT","CGTT")
print(b)
Length=len(b)
print(Length)
l=0
for possibilities in b:
    l=l+search_disease(possibilities)
print("The probability of child inherting a disease is : ",(l/Length)*100)

