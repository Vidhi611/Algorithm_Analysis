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
