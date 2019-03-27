with open("futbolcular.txt","r",encoding="utf-8") as file:
    gs = list()
    bjk = list()
    fb = list()

    for satır in file:
        satır = satır[:-1]
        satır_elemanları = satır.split(",")
        if (satır_elemanları[1] == "Fenerbahçe"):
            fb.append(satır + "\n")
        elif (satır_elemanları[1] == "Galatasaray"):
            gs.append(satır + "\n")

        else:
            bjk.append(satır + "\n")

    with open("gs.txt","w",encoding="utf-8") as file1:
        for i in gs:
            i = i[:-1]
            i= i.split(",")
            file1.write(i[0]+"\n")

    with open("fb.txt","w",encoding="utf-8") as file2:
        for i in fb:
            i = i[:-1]
            i= i.split(",")
            file2.write(i[0]+"\n")
    with open("bjk.txt","w",encoding="utf-8") as file3:
        for i in bjk:
            i = i[:-1]
            i= i.split(",")
            file3.write(i[0]+"\n")
