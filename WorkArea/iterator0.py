"""

Program 1¶
"Kareler" isminde bir tane sınıf tanımlayın ve bu sınıfı iterable bir sınıf yapmaya çalışın. Bu sınıfın init fonksiyonu maksimum isimli bir tane parametre alsın ve her next işleminde ekrana üzerinde bulunduğunuz sayının karesi yazdırılsın. StopIteration hatası ekrana maksimum sayıyı geçtiğiniz zaman fırlatılsın.

"""

"""
class Kuvvet2():
    def __init__(self,max = 0):

        self.max = max
        self.kuvvet = 1

    def __iter__(self):

        return self
    def __next__(self):
        if (self.kuvvet <= self.max):
            sonuc = self.kuvvet ** 2

            self.kuvvet += 1

            return sonuc
        else:
            self.kuvvet = 0
            raise StopIteration


kuvvet = Kuvvet2(10)

for i in kuvvet:
    print(i)


"""


"""
Program 2
1'den 1000'e kadar olan sayılardan asal sayıları üreten generator bir fonksiyon yazın.



def asal_mı(sayı):
    i =  2

    while i < sayı:
        if (sayı % i == 0):
            return False
        i += 1
    return True
def asal_generator():
    i =  2
    while True:
        if (asal_mı(i)):
            yield i
        i += 1

for sayı in asal_generator():
    if (sayı > 1000):
        break
    print(sayı)

"""
