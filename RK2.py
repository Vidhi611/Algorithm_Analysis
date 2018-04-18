import time
import numpy

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



start_time=time.time()

class RollingHash:
    def __init__(self, text, sizeWord):
        self.text = text
        self.hash = 0 
        self.sizeWord = sizeWord

        for i in range(0, sizeWord):
            #ord maps the character to a number
            #subtract out the ASCII value of "a" to start the indexing at zero
            self.hash += (ord(self.text[i]) - ord("a")+1)*(26**(sizeWord - i -1))

        #start index of current window
        self.window_start = 0
        #end of index window
        self.window_end = sizeWord

    def move_window(self):
        if self.window_end <= len(self.text) - 1:
            #remove left letter from hash value
            self.hash -= (ord(self.text[self.window_start]) - ord("a")+1)*26**(self.sizeWord-1)
            self.hash *= 26
            self.hash += ord(self.text[self.window_end])- ord("a")+1
            self.window_start += 1
            self.window_end += 1

    def window_text(self):
        return self.text[self.window_start:self.window_end]

def rabin_karp(word, text):
    count=0
    if word == "" or text == "":
        return count
    if len(word) > len(text):
        return count

    rolling_hash = RollingHash(text, len(word))
    word_hash = RollingHash(word, len(word))
    #word_hash.move_window()
    
    for i in range(len(text) - len(word) + 1):
        if rolling_hash.hash == word_hash.hash:
            if rolling_hash.window_text() == word:
                 count=count+1
        rolling_hash.move_window()
    return count

def search_disease(seq):
    """
    Searches for diseaes and returs the name of thr disease if diagnosed. 
    Disease is present or not depends on the symptoms
    """
    symp_count = []
    for i in range(len(symp_names)):
        symp_count.append(rabin_karp(symptoms[symp_names[i]], seq))
    for i in range(len(dis_names)):
        flag = 1
        for j in range(len(symp_names)):
            temp3 = diseases[dis_names[i]][symp_names[j]]
            if(ord(str(temp3)) != ord(str(symp_count[j]))):
                flag = 0
                break
        if flag == 1:
            print(dis_names[i])    


search_disease("ACGTTCGACGTTCCTGTGCAGATGTGCAGTAGTGCAGTGGTGCAGACATGCTGACATGCTGAGATGCTGAATGCTGATAACTGGATGCTGATAATGCTGA")
search_disease("ACGTTCGTCAGGCCTCACGTTCAGTCAGGCCGCATGCTGAGGCTTACGTGCATGCTGACGTCAGGCCTGAATGCTGAGCTCAGGCCGTCTTACGTGATGCTGA")
search_disease("CTTACGTAGTCAGGCCTATGTGCAGTGACTTACGTCGTCAGGCCATGTGCAGTATGCTTACGTGCGATGCTGAGATCTTACGTCAGATGCTGA")

start_time=time.time()
print("--- ",(time.time() - start_time),"seconds ---")
