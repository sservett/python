def histogram(your_text):
    
    letter_fre = dict()

    for i in your_text:
        if (i in letter_fre):
            letter_fre[i] += 1
        else:
            letter_fre[i] = 1
    for i,j in letter_fre.items():
        
        print(i,":",j)

your_text =  "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"

print(histogram(your_text))