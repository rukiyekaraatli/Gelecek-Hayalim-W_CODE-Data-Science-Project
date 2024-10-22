#Ödev-2:Faktöriyel adında fonksiyon oluşturulur. Döngü kullanarak parametre olarak girilen sayının faktöriyeli hesaplanır. Format metodunu kullanılarak ekrana yazdırılır.

sayi = int(input("Faktöriyelini almak istediğiniz sayıyı girin: "))

def faktoriyel(n):
    sonuc = 1
    for i in range(1, n + 1):
        sonuc *= i
    return sonuc

print("Faktöriyel: {}".format(faktoriyel(sayi)))