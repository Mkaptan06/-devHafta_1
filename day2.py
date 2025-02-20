#Birinci video

print("kodlamaio")
baslik = "Taşıt Kredisi"
print(baslik)
baslik ="İhtiyaç Kredisi"
print(baslik)

vade=36
ekVade = 6
vade2= "36"

aylikodeme = 200.50

yukselistemi = False

print(5+5)
print(vade + 12)
print(vade + ekVade)
print(36+6)

print(5-5)
print(vade - 12)
print(vade - ekVade)
print(36 - 6)

yeniVade= vade /2
fiyat=100
indirimliFİyat = fiyat-20

print(yeniVade)
print(indirimliFİyat)

print(10%2)
print(vade % 5)
print(vade % ekVade)
print(30%10)

print(1 == 1)
print(1 == 2)

print(1 > 3)
print(3 > 1)
print(1 > 1)
print(1 >= 1)

print(1 < 2)
print(3 < 1)
print(1 < 1)
print(1 <= 1)

print(1 != 1)
print(1 != 2)

print(1 > 1 or 5 > 2)
print(1 > 2 and 5 > 2)
print(1 > 2 or 5 > 2 and 3 > 2)

print(1 > 2 and 5 > 2 and 3 > 2)

print(2 > 1 or 1 > 2 and 3 > 2)

sayi1=10
sayi2=15

if sayi1 < sayi2:
    print("Sayı 1 sayı 2 den küçüktür")
elif sayi1==sayi2:
    print("İki sayı eşittir")
else:
    print("Sayı 1 sayı 2 den büyüktür")


if sayi1 < sayi2:
    print("Sayı 1 sayı 2 den küçüktür")
if sayi1==sayi2:
    print("İki sayı eşittir")
else:
    print("Sayı 1 sayı 2 den büyüktür")

#İkinci video

faiz= 1.59
vade = "36"
krediAdi = "İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))

print(int(vade)+12)
faiz = str(faiz)
print(type(faiz))

vade = 36 #int(input("Lütfen istediğiniz vade sayısını giriniz: "))
print(type(vade))
vade = vade + 12


print("Seçtiğiniz vade sonucu ortaya çıkan vade: " + str(vade))
print("Seçtiğiniz vade sonucu ortaya çıkan vade: {vadeSayisi}"  .format(vadeSayisi=vade))


isim = "Halit" 
metin = "Merhaba {}".format(isim)
print(metin)


metin =f"Hoşgeldiniz {1+1}"
print(metin)

dizi = ["İhtiyaç Kredisi",10 , 5.2 , True ]
print(dizi)

krediler = ["İhtiyaç Kredisi" , "Taşıt Kredisi" , "Konut Kredisi"]
print(type(krediler))

print(krediler[0])
print(len(krediler))
#print(krediler[3])

krediler.append("Özel Kredi")
print(krediler)

krediler.append("X Kredisi")
print(krediler)

krediler.pop(0)
print(krediler)

krediler.append("Taşıt Kredisi")
print(krediler)

krediler.remove("Taşıt Kredisi")
print(krediler)

krediler.extend(["Y Kredisi ", "Z Kredisi"])
print(krediler)

for i in range(10):
    print("xx")
    print(i)
print("************")

for i in range(5,11):
    print(i)
print("************")

for i in range(0,51,10):
    print(i)
print("***********")
krediler = ["İhtiyaç Kredisi" , "Taşıt Kredisi" , "Konut Kredisi"]
for kredi in krediler:
    print(kredi)
print("*************")
for i in range (len(krediler)):
    print(krediler[i])
print("*************")

i = 0
while i < 10 :
    print("x")
    i+=1
print("y")

print("*************")

while True:
    print("x")
    break
print("*************")

i = 0
while i < len(krediler):
    i += 1
    print(krediler[i])
    if krediler[i] == "Konut Kredisi":
        break

fiyat = 100
indirim = 20

def calculate():
    print(100-20)

def calculateWithParams(fiyat,indirim):
    print(fiyat-indirim)

def sayHello(name):
    print(f"Merhaba {name}")


calculate()
calculateWithParams(50,10)
calculateWithParams(100,30)
sayHello("Mustafa")

def calculateAndReturn(prica,discount):
    return prica-discount
yeniFiyat = calculateAndReturn(200,50)
print(yeniFiyat)

def calculatePrice(price,discount):
    print(price-discount)

def calculatePriceAndReturn(price,discount):
    return price-discount

# print("*************")
# fonk1 = calculatePrice(100-50)
# fonk2 = calculatePriceAndReturn(300-100)
# print(f"212. Satır {fonk1}")
# print(f"213. Satır {fonk2}")
# print("*************")

#Üçüncü video

class Human:
    #built-in
    #consturctur = yapıcı blok
    #initialize
    def __init__(self,name):
        self.name =name
    def __str__(self):
        return f"STR fonksiyonundan dönen değer: {self.name}"
    def talk(self,sentence):
        print(f"{self.name}: {sentence}")
    def walk(self):
        print(f"{self.name} is walking.")
    
human1 = Human("Mustafa")
human1.talk("Merhaba")
human1.walk()
print(human1)


human2 = Human("Kaptan")
human2.name = "Kaptan"
human2.talk("Selam")
human2.walk()
print(human2)


# def topla(a,b):
#     return a+b
# def bol(a,b):
#     return a/b


# import matematik as m
# from day2 import sayHello,Human

# import random

# print(m.topla(10,20))
# print(random.randint(0,100))
# print(sayHello("as"))

# human1 = Human("Mustafa")
# human1.talk("Merhaba")