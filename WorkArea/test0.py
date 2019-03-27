"""
file = open("/tmp/alivei99999999999999999999","w")
file.write("Servet INCE\nArzu INCE\nIbrahim Berk INCE\n\n\n\n\n\n")
file.close


file = open("bilgiler.txt","r")
for i in file:
    print(i, end = "")
file.close

file = open("bilgiler.txt","r")
icerik = file.read()
print(icerik)
icerik2 = file.read()

file = open("bilgiler.txt","r")
print(file.readline())
print("---------------------")
print(file.readline())
print("---------------------")
print(file.readline())
print("---------------------")
print(file.readline())
print("---------------------")
print(file.readline())
file.close



file = open("bilgiler.txt","r")

print(file.readlines())

file.close


with open("bilgiler.txt","r") as file:
    for i in file:
        if (i == "Arzu INCE\n"):
            print(i)



with open("bilgiler.txt","r") as file:
    file.seek(3)
    print(file.tell())


with open("bilgiler.txt","r") as file:
    file.seek(3)
    print(file.tell())
    file.seek(1)
    print(file.read(5))
    print(file.tell())


def alan_hesapla(demet):
    return demet[0] * demet[1]


liste = [(3,4),(10,3),(5,6),(1,9)]

print(list(map(alan_hesapla,liste)))



def ucgen_mi (demet):
    if (demet[0] * demet[0]) + (demet[1] * demet[1]) ==  (demet[2] * demet[2]):
        return True

liste = [(3,4,5),(6,8,10),(3,10,7)]

print(list(filter(ucgen_mi,liste)))




#print ("sarvat".replace("a","e").upper().lower())

liste2 = "Python-Php-Javascript-C-Java".split("-")

print(liste2)

print("                      Python           djjjjjhu ddhdhhd                   duduududud          ".strip())
"""

from datetime import datetime

import os
su_an = datetime.now()

tarih = datetime(1985,3,8)

print(tarih - su_an)

os.rmdir("AAAA")
for i in os.listdir():
    print(i)
