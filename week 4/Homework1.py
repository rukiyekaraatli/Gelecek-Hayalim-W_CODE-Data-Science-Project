#Ödev-1: Kullanıcıdan maaş bilgisini istenir ve bu bilgiye göre maaşından ne kadar vergi kesileceğini hesaplanır. Kullanıcının geliri;
 #1.10000 ve altındaysa maaşından %5 kesinti olur. 
 #2.25000 ve altındaysa maaşından %10 kesinti olur. 
 #3.45000 ve altındaysa maaşından %25 kesinti olur. 
 #4.Diğer koşullarda %30 kesinti olur. 
#Bu durumlara göre kullanıcının yeni maaşı yazdırılır.

# Kullanıcıdan maaş bilgisi isteme
maas = float(input("Lütfen, Maaşınızı Giriniz: "))

# Vergi oranlarına göre maaş kesintisi
if maas <= 10000:
    vergiOrani = 0.05
elif maas <= 25000:
    vergiOrani = 0.10
elif maas <= 45000:
    vergiOrani = 0.25
else:
    vergiOrani = 0.30

# Vergi miktarı ve yeni maaş hesaplama
vergiMiktari = maas * vergiOrani
yeniMaas = maas - vergiMiktari

print(f"Maaşınıza uygulanan vergi oranı: %{vergiOrani * 100}")
print(f"Kesilen vergi miktarı: {vergiMiktari} TL")
print(f"Yeni Maaşınız: {yeniMaas} TL")

