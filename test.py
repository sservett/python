"""
####################################################################EXAMPLE1####################################################################

print("Registering Player Programme")

name = input("Player\'s Name: ")

surname = input("Player\'s Surname: ")

team = input("Player\'s Team: ")

information = [name,surname,team]

print("Information is being recorded..")

print("Player\'s Name: {}\nPlayer\'s Surname: {}\nPlayer\'s Team {}".format(information[0],information[1],information[2]))

print("Information is recorded now, thanks..")

####################################################################EXAMPLE2####################################################################

age = int (input("Please enter your age: "))

if (age < 17):

    print ("You are not allowed to enter!")

else:

    print ("Welcome to the club")


####################################################################EXAMPLE3####################################################################

age = int (input("Please enter your age: "))

if (age < 17):

    print ("You are not allowed to enter!!")

elif age > 75:

    print ("You are too old for this club!!")

else:

    print ("Welcome to the club!!")


####################################################################EXAMPLE4####################################################################

# PS: To run this code need to remove triple quotes from print below.
print(""""""-------------------------------------------------
Hesap Makinesi Programına Hoşgeldiniz
İşlemler;

1. Toplama İşlemi

2. Çıkarma İşlemi

3. Çarpma İşlemi

4. Bölme İşlemi
-----------------------------------------------------------
"""""")
a = float(input("Birinci Sayı:")) # Birinci Sayıyı Alıyoruz.
b = float(input("İkinci Sayı:")) # İkinci Sayıyı Alıyoruz.

işlem =  input("İşlem Numarasını Giriniz:") # Buna göre koşullarımızı yazacağız.

if (işlem == "1"): # Toplama İşlemi

    print("{} ile {} 'nin toplamı {} dır.".format(a,b,a+b))
elif (işlem == "2"):

    print("{} ile {} 'nin farkı {} dır.".format(a, b, a - b))

elif (işlem == "3"):

    print("{} ile {} 'nin çarpımı {} dır.".format(a, b, a * b))

elif (işlem == "4"):

    print("{} 'nın {} 'e bölümü {} dır.".format(a, b, a / b))
else:

    print("Lütfen geçerli bir işlem giriniz...")



####################################################################EXAMPLE5####################################################################

print (""""""********************************************************
User Login Page
********************************************************
"""""")

sys_username = "servet"
sys_password = "1983"


username = input("Username: ")
password = input("Password: ")

if (username == sys_username) and (password != sys_password):
    print("Password failure")

elif (username != sys_username) and (password == sys_password):
    print("Username failure")

elif (username != sys_username) and (password != sys_password):
    print("Username and Password failure")

else:
    print("Welcome to the SYSTEM!!")


####################################################################EXAMPLE6####################################################################

print (""""""********************************************************
 Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

 BKİ 18.5'un altındaysa -------> Zayıf

 BKİ 18.5 ile 25 arasındaysa ------> Normal

 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

 BKİ 30'un üstündeyse -------------> Obez
********************************************************
"""""")

boy1 = float(input("Boyunuzu giriniz: "))
kilo = float(input("Kilonuzu giriniz: "))

if boy1 > 2.5:
    boy = boy1 /100
else:
    boy = boy1

index = kilo / (boy * boy)

if index < 18.5 :
    print("Zayifsiniz")
    print("Indexiniz:" )
    print (index)

elif index >= 18.5 and index <= 25 :
    print("Normal kilodasiniz")

elif index > 25 and index <= 30 :
    print("Uzgunum Fazla kilolusunuz")
    print("Indexiniz:" )
    print (index)

elif index > 30 :
    print("Malasef obezsiniz, diyete baslayain")
    print("Indexiniz:" )
    print (index)

else  :
    print("Gceersiz deger girdiniz")
x

####################################################################EXAMPLE7####################################################################

dictionary = {"one": "1","two": "2","three": "3","four": "4","five": "5",}
for i in dictionary.values():
    print(i)


for i in range(1,50):
    print(i * "*")

list = [[1,2,3], [4,5,6,7],[8,9]]

list1 = [2 * i for i in list]

print(list1)

list = [(1,2),(3,4),(5,6)]

list1 = [i * j for i,j in list]

print(list1)


list1 = [[1,2,3], [4,5,6,7],[8,9]]

list2 = list()

for i in list1:

    for x in i:

        list2.append(x)

print(list2)

list1 = [[1,2,3], [4,5,6,7],[8,9]]

list2 = [x * 2 for i in list1 for x in i]

print(list2)


####################################################################EXAMPLE8####################################################################

print (""""""********************************************************
User Login Program
********************************************************
"""""")

sys_username = "servet"

sys_password = "1983"

failure_count = 3

while True:

    username = input("Username: ")
    password = input("Password: ")

    if (username != sys_username and password == sys_password):
        print("Invalid username")
        failure_count -= 1
    elif (username == sys_username and password != sys_password):
        print("Invalid password")ile
        
        failure_count -= 1

    elif (username != sys_username and password != sys_password):
        print("Invalid username and password")
        failure_count -= 1
    else :
        print("Logon succesfully! Welcome..")
        break

    if failure_count <= 0:
        print("Your do not have right for any more attept")
        break


####################################################################EXAMPLE9####################################################################

print (""""""********************************************************
Welcome to the Cash Machine

Menu;

1. Balance Query

2. Withdraw Cash

3. Deposit In

Please press "q" to exit from process.

********************************************************
"""""")


balance = 1000

while True:
    process = input("Please select one of process: ")

    if (process == "q") :
        print("Hope to see you again! Have a nice day")
        break

    elif (process == "1"):
        print("Your balance is {} pound".format(balance))

    elif (process == "2"):
        amount = int(input("Please enter amount: "))

        if (balance - amount < 0 ):
            print("Yo do not have engough balance for amount!!")
            continue

        balance -= amount
        print("Your new balance is {}".format(balance))

    elif (process == "3"):
        amount = int(input("Please enter amount: "))
        balance += amount
        print("Your new balance is {}".format(balance))

    else:
        print("Invalid option!")

####################################################################EXAMPLE10####################################################################


print(""""""*******************
Faktoriyel Bulma Programı

Programdan çıkmak için 'q' ya basın.
*******************"""""")
while True:
    sayi =  input("Sayı:")
    if (sayi == "q"):
        print("Programdan çıkılıyor...")
        break
    sayi = int(sayi)

    faktoriyel = 1
    for i in range(2,sayi+1):
        faktoriyel *= i

    print("Faktoriyel:",faktoriyel)



####################################################################EXAMPLE12####################################################################

""""""
Fibonacci Serisi yeni bir sayıyı önceki iki sayının toplamı şeklinde oluşturur.

1,1,2,3,5,8,13,21,34...............
""""""
ilk_sayı = 1

ikincisayi = 1

fibonacci = [ilk_sayı,ikincisayi]
for i in range(10):


    ilk_sayı,ikincisayi = ikincisayi,ilk_sayı + ikincisayi

    fibonacci.append(ikincisayi)

print(fibonacci)



####################################################################EXAMPLE13####################################################################

""""""
Problem 1
Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.

Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)
""""""
#number = int(input("Please enter one number: "))

sayı = int(input("Sayı:"))

i = 1
toplam = 0
while (i < sayı):
    if (sayı % i == 0):
        toplam += i
    i += 1

if (toplam == sayı):
    print(sayı,"mükemmel bir sayıdır.")
else:
    print(sayı,"mükemmel bir sayı değildir.")

# Yada tum mukemmel sayilari arariz;
for sayı in range(50000):

    i = 1
    toplam = 0
    while (i < sayı):
        if (sayı % i == 0):
            toplam += i
        i += 1

    if (toplam == sayı):
        print(sayı,"mükemmel bir sayıdır.")
    else:
        continue

""""""
Problem 2
Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.

Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4

 Programlamada her detayı öğrenemeyiz. Bunun için bazı yerlerde deneme yanılma yoluyla da öğrendiğimiz şeyler olur. Bu problemde deneme yanılma yoluyla list comprehension'ın koşullu durumlarla kullanımını öğreneceksiniz.

""""""
sayı = input("Sayı:")
basamak_sayisi = len(sayı)
sayı = int(sayı)
basamak = 0
toplam = 0

gecici_sayı = sayı

while (gecici_sayı > 0):

    basamak = gecici_sayı % 10

    toplam += basamak ** basamak_sayisi

    gecici_sayı //= 10


if (toplam == sayı):
    print(sayı,"bir armstrong sayısıdır.")
else:
    print(sayı,"bir armstrong sayısı değildir.")

""""""
Problem 3
1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.

İpucu: İç içe 2 tane for döngüsü kullanın. Aynı zamanda sayıları range() fonksiyonunu kullanarak elde edin.
""""""
for i in range(1,11):
    print("*************************************************")
    for j in range(1,11):

        print("{} x {} = {}".format(i,j,i*j))

#Benim bait ornek
print("Please enter 2 number in order to multiply them")
i = int(input("1st Number: "))
j = int(input("2nd Number: "))

print("{} multiply {} equal {}".format(i,j,i*j))

""""""
Problem 4
Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin. Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.

İpucu : while döngüsünü sonsuz koşulla başlatın ve kullanıcı q'ya basarsa döngüyü break ile sonlandırın.

""""""

toplam = 0

while True:

    sayı = input("Sayı:")

    if (sayı == "q"):
        break
    sayı = int(sayı)

    toplam += sayı

print("Girdiğiniz Sayıların Toplamı:",toplam)


""""""
Problem 5
1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın. Bu işlemi continue ile yapmaya çalışın.
""""""

for i in range(1,101):

    if (i % 3 != 0):
        continue
    print(i)

""""""
Problem 6
Buradaki problemin çözümünü derslerimizde özellikle öğrenmedik. Burada mantık yürüterek ve list comprehension kullanarak 1'den 100'e kadar olan sayılardan sadece çift sayıları bir listeye atmayı yapmayı çalışın.

Not: Programlamada her detayı öğrenemeyiz. Bunun için bazı yerlerde deneme yanılma yoluyla da öğrendiğimiz şeyler olur. Bu problemde deneme yanılma yoluyla list comprehension'ın koşullu durumlarla kullanımını öğreneceksiniz.

İpucu: Basit düşünmeye çalışın.

""""""
liste = [x for x in range(1,101) if x % 2 == 0]
print(liste)


####################################################################EXAMPLE14####################################################################

def greetings(name):
    print("Hello!",name)
    print("How are you?")

#print(type(greetings))

greetings("Servet")

def multiply(a,b,c):
    print("Total: ", a * b * c)

multiply(100,4,5)

def subtrack(a,b):
    print("Subtrack Result: ", a - b)

subtrack(450,23)



####################################################################EXAMPLE15####################################################################


### LAMBDA

adding = lambda x,y,z : x + y + z
print(adding(2,5,9))


def makeitopposite(s):
    return s[::-1]
print(makeitopposite("servet"))

mio = lambda s : s[::-1]
print(mio("arzu"))



####################################################################EXAMPLE16####################################################################


### ASIL SAYI MI?

print(""""""****************
Bir sayının asal olup olmadığını bulma

Programdan çıkmak için 'q' ya basın.
****************
"""""")
def asal_mi(sayi):
    for i in range(2,sayi):
        if (sayi % i == 0 ):
            return False
    return True


while True:
    sayi = input("Sayı:")
    if (sayi == "q"):
        print("Programdan Çıkılıyor...")
        break
    sayi = int(sayi)
    if (sayi == 1):
        print(sayi, "asal bir sayı değildir.")
    elif (sayi == 2):
        print(sayi, "asal bir sayıdır.")
    else:
        if (asal_mi(sayi)):
            print(sayi,"asal bir sayıdır.")
        else:
            print(sayi,"asal bir sayı değildir.")



print(""""""****************
Bir sayının bölenlerini bulma

Programdan çıkmak için 'q' ya basın.
****************
"""""")

def bolenleri_bul(sayi):
    bolen_listesi = []
    for i in range(1,sayi+1):
        if (sayi % i == 0):
            bolen_listesi.append(i)
    return bolen_listesi

while True:
    sayi = input("Sayı:")
    if (sayi == "q"):
        print("Programdan Çıkılıyor...")
        break
    else:
        sayi = int(sayi)
        print(bolenleri_bul(sayi))

## 1 to 10000 , wonderful numbers

def mukemmel(sayi):

    toplam = 0

    for i in range(1,sayi):

        if (sayi % i == 0):
            toplam += i

    return toplam == sayi

for i in range(1,10000):
    if mukemmel(i):
        print("Mukemmel Sayi: ",i)


## https://nbviewer.jupyter.org/github/mustafamuratcoskun/Sifirdan-Ileri-Seviyeye-Python-Programlama/blob/master/Fonksiyonlar/Fonksiyonlar%20-%20%20%C3%96dev%20ve%20%C3%87%C3%B6z%C3%BCmleri/Programlama%20%C3%96devi%20-%20Fonksiyonlar.ipynb

## https://nbviewer.jupyter.org/github/mustafamuratcoskun/Sifirdan-Ileri-Seviyeye-Python-Programlama/blob/master/Fonksiyonlar/Fonksiyonlar%20-%20%20%C3%96dev%20ve%20%C3%87%C3%B6z%C3%BCmleri/Programlama%20%C3%96devi%20%20%C3%87%C3%B6z%C3%BCmleri%20-%20Fonksiyonlar.ipynb

def ebob_bulma(sayı1,sayı2):

    i = 1
    ebob = 1
    while (i <= sayı1 and i <= sayı2 ):

        if ( not (sayı1 % i) and not (sayı2 % i)):
            ebob = i
        i += 1
    return ebob
sayı1 = int(input("Sayı-1:"))
sayı2 = int(input("Sayı-2:"))

print("Ebob:",ebob_bulma(sayı1,sayı2))


def ebob_bulma(sayı1,sayı2):

    i = 1
    ebob = 1
    while (i <= sayı1 and i <= sayı2 ):

        if ( not (sayı1 % i) and not (sayı2 % i)):
            print("S: ",sayı1 % i)
            print("A: ",sayı2 % i)
            ebob = i
        i += 1
    return ebob

print("Ebob:",ebob_bulma(sayı1,sayı2))


birler =  ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]
yüzler=["","yüz","İkiyüz","Üçyüz","Dörtyüz","Beşyüz","Altıyüz","Yediyüz","Sekizyüz","Dokuzyüz"]
binler=["","Bin","İkibin","Üçbin","Dörtbin","Beşbin","Altıbin","Yedibin","Sekizbin","Dokuzbin"]

def okunus(sayı):
    birinci = sayı % 10
    ikinci = (sayı % 100) // 10
    üçüncü= (sayı % 1000) // 100
    dördüncü = sayı // 1000

    return binler[dördüncü] + " " +  yüzler[üçüncü] + " " +  onlar[ikinci] + " " + birler[birinci]


sayı =  int(input("Sayı:"))

print(okunus(sayı))


####################################################################EXAMPLE17####################################################################

## Sayi tahmin oyunu


import time
import random
print(""""""****************************

Sayı Tahmin Oyununa Hoşgeldiniz

1 ile 100 arasında(1 ve 100 dahil) rastgele tahmin edin.
****************************""""""


while True:
    tahmin =  int(input("Tahmininiz:"))
    tahmin_hakkı = 7
    rastgele_sayı = random.randint(1,100)

    if (tahmin == rastgele_sayı):
        print("Sayı Sorgulanıyor....")
        time.sleep(1)
        print("Tebrikler!")
        print("Sayı",rastgele_sayı)
        break
    elif(tahmin < rastgele_sayı):
        print("Sayı Sorgulanıyor....")
        time.sleep(1)
        tahmin_hakkı -= 1
        print("Lütfen daha yüksek bir sayı söyleyin.")
        print("Tahmin Hakkı:",tahmin_hakkı)
    else:
        print("Sayı Sorgulanıyor....")
        time.sleep(1)
        tahmin_hakkı -= 1
        print("Lütfen daha düşük bir sayı söyleyin.")
        print("Tahmin Hakkı:",tahmin_hakkı)
    if (tahmin_hakkı == 0 ):
        print("Tahmin Hakkınız Bitti. Üzgünüz")
        print("Sayımız:",rastgele_sayı)
        break




####################################################################EXAMPLE18####################################################################

class developer():

    def __init__(self,name,surname,number,salary,languages):
        self.name = name
        self.surname = surname
        self.number = number
        self.salary = salary
        self.languages = languages
    def showinfo(self):
        print(""""""
        The details of develover object

        Name: {}

        Surname: {}

        Number: {}

        Salary: {}

        Languages: {}

        """""".format(self.name,self.surname,self.number,self.salary,self.languages))

developer1 = developer("Servet","INCE",12345,5000,["Python","Bash"])

print(developer1)



#  Yeni bir Araba veri tipi oluşturuyoruz.
class Araba():
    model =  "Renault Megane"
    renk = "Gümüş"            # Sınıfımızın özellikleri (attributes)
    beygir_gücü = 110
    silindir = 4

araba1 =  Araba()

type(araba1)

print(araba1.model,"/",araba1.renk)




class Yazılımcı():

    def __init__(self,isim,soyisim,numara,maaş,diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.maaş = maaş
        self.diller = diller
    def bilgilerigöster(self):
        print(""""""
        Yazılımcı objesinin özellikleri

        İsim : {}

        Soyisim : {}

        Numara: {}

        Maaş : {}

        Bildiği Diller : {}

        """""".format(self.isim,self.soyisim,self.numara,self.maaş,self.diller))
    def zam_yap(self,zam_miktarı):
        print("Zam yapılıyor...")

        self.maaş += zam_miktarı
    def dil_ekle(self,yeni_dil):
        print("Dil ekleniyor.....")
        self.diller.append(yeni_dil)

yazılımcı = Yazılımcı("Mustafa Murat","Coşkun",12345,3000,["Python","Java","C","Javascript"])

yazılımcı.bilgilerigöster()

yazılımcı.dil_ekle("GoLang")

yazılımcı.bilgilerigöster()

yazılımcı.zam_yap(500)

yazılımcı.bilgilerigöster()



class Çalışan():

    def __init__(self,isim,maaş,departman):
        print("Çalışan sınıfının init fonksiyonu")

        self.isim = isim
        self.maaş = maaş
        self.departman = departman
    def bilgilerigöster(self):
        print("Çalışan sınıfının bilgileri .....")

        print("İsim : {}\nMaaş : {} \nDepartman: {}\n ".format(self.isim,self.maaş,self.departman))

    def departman_değiştir(self,yeni_departman):
        self.departman = yeni_departman




class Yönetici(Çalışan):
    pass

    def zam_yap(self,zam_miktari):
        self.maaş += zam_miktari

yönetici = Yönetici("Mustafa Murat Coşkun",3000,"Bilişim")

yönetici.bilgilerigöster()

yönetici.departman_değiştir("İnsan Kaynakları")

yönetici.bilgilerigöster()

yönetici.zam_yap(1000)

yönetici.bilgilerigöster()

print(dir(yönetici))

Çalışan = Çalışan("Servet INCE",2800,"Bilişim")

print(dir(Çalışan))

Çalışan.zam_yap(1000)

print(dir(Çalışan))



####################################################################EXAMPLE19####################################################################

class Kitap():
    pass

kitap1 = Kitap()

len(kitap1)

print(kitap1)




####################################################################EXAMPLE20####################################################################

try:
    a = int("sdasdasd324324234324")
    print("Program burada")
except:
    print("Bir hata oluştu!")
print("Bloklar sona erdi!")


try:
    a = int("23")
    print("Program burada")
except:
    print("Bir hata oluştu!")
print("Bloklar sona erdi!")


try:
    a = int(input("Sayı1:"))
    b = int(input("Sayı2:"))
    print(a / b)
except ValueError:
    print("Lütfen inputu doğru girin.")
except ZeroDivisionError:
    print("Bir sayı 0'a bölünemez.")
print("Bloklar sona erdi...")


try:
    a = int(input("Sayı1:"))
    b = int(input("Sayı2:"))
    print(a / b)
except ValueError:
    print("Lütfen inputu doğru girin.")
except ZeroDivisionError:
    print("Bir sayı 0'a bölünemez.")
print("Bloklar sona erdi...")


try:
    a = int(input("Sayı1:"))
    b = int(input("Sayı2:"))
    print(a / b)
except ValueError:
    print("Lütfen inputu doğru girin.")
except ZeroDivisionError:
    print("Bir sayı 0'a bölünemez.")
finally:
    print("Burası çalıştı.")
print("Bloklar sona erdi...")


def terscevir(s):
    if (type(s) != str):
        raise ValueError("Lütfen string bir değer gönderin.")
    else:
        return s[::-1]



####################################################################EXAMPLE21####################################################################

liste = ["345","sadas","324a","14","kemal"]

for eleman in liste:

    try:
        eleman = int(eleman) # Eğer hata ile karşılaşırsak burası hata verecek ve print çalışmayacak.
        print(eleman)
    except:
        pass # pass deyimi bir blokun hiçbir şey yapmadığı anlamına geliyor. Python'ın hata vermemesi için kullanabi



def çift_mi(sayı):

    if (sayı % 2 == 0):
        return sayı
    else:
        raise ValueError
liste = [34,23,25,43,56,493939,40955,200293,9399394,933,2,1,3,33,100,61,1800]

for i in liste:
    try:
        print(çift_mi(i))
    except ValueError:
        pass

"""
