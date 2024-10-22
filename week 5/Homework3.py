#Ödev-3:Kişinin fonksiyona doğum yılını vererek kaç yaşında olduğunu hesaplayan bir fonksiyon oluşturun. 

from datetime import datetime

dogumYili = int(input("Doğum yılınızı girin: "))

def yasHesapla(dogum_yili):
    mevcutYil = datetime.now().year
    yas = mevcutYil - dogumYili
    return yas

yas = yasHesapla(dogumYili)
print(f"Yaşınız: {yas}")