#Ödev-1:Kullanıcıdan pi değeri ve yarıçap bilgisi alarak dairenin alanını hesaplayan bir fonksiyon oluşturulur.

import math

pi = float(input("Pi değerini girin: "))
yaricap = float(input("Yarıçapı girin: "))

def daireAlan(piDegeri, yaricap):
    alan = piDegeri * (yaricap ** 2)
    return alan

alan = daireAlan(pi, yaricap)
print(f"Dairenin alanı: {alan}")