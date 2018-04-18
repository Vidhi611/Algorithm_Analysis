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

diseases = {}
diseases["chicken_pox"] = {"cold": 2, "cough": 0, "diarrhea": 4, "fatigue": 0, "fever": 6}
diseases["dengue"] = {"cold": 2, "cough": 4, "diarrhea": 0, "fatigue": 2, "fever": 4}
diseases["hepatitis"] = {"cold": 0, "cough": 2, "diarrhea": 2, "fatigue": 4, "fever": 2}
diseases["jaundice"] = {"cold": 0, "cough": 4, "diarrhea": 8, "fatigue": 2, "fever": 6}
diseases["typhoid"] = {"cold": 4, "cough": 2, "diarrhea": 6, "fatigue": 4, "fever": 0}


start_time=time.time()

def search_disease(seq):
    """
    Searches for diseaes and returs the name of thr disease if diagnosed. 
    Disease is present or not depends on the symptoms
    """
    symp_count = []
    for i in range(len(symp_names)):
        symp_count.append(len(length(symptoms[symp_names[i]], seq)))
    for i in range(len(dis_names)):
        flag = 1
        for j in range(len(symp_names)):
            temp3 = diseases[dis_names[i]][symp_names[j]]
            if(ord(str(temp3)) != ord(str(symp_count[j]))):
                flag = 0
                break
        if flag == 1:
            print(dis_names[i])

def length(sub,S):
	"""
	This is a simple brute force algorithm for searching a string
	"""
	n=len(S)
	m=len(sub)
	matches=[]
	for i in range(n-m+1):
		flag=0
		for j in range(m):
			if S[i+j] != sub[j]:
				flag=1
				break
		if(flag==0):
			matches.append(str(i))
	return matches

def main():
	"""
	main program where the DNA string to be diagnosed is passed
	"""
	search_disease("ACGTTCGTCAGGCCTCACGTTCAGTCAGGCCGCATGCTGAGGCTTACGTGCATGCTGACGTCAGGCCTGAATGCTGAGCTCAGGCCGTCTTACGTGATGCTGA")
	print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
	main()
