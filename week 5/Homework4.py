#Ödev-4:Doğum yılı ve isim bilgisi verilen fonksiyon kişinin emekli olup olmadığını söylesin.(Kişi 65 yaşında ise emekli olur.) Burada yaş hesabını yukarıdaki örnekteki fonksiyonu kullanarak yapsın.(Yani fonksiyon içinde fonksiyon kullanmanızı istiyorum :)) Kişi 65 yaşında ya da daha fazlaysa "Emekli oldunuz" yanıtını, 65 yaşından küçükse emekliliğine kaç yıl kaldığını da hesaplayarak "(isim) emekliliğine (yıl) kaldı." yanıtını versin.

from datetime import datetime

isim = input("Adınızı girin: ")
dogumYili = int(input("Doğum yılınızı girin: "))

def emeklilikDurumu(isim, dogumYili):

    # Yaş hesaplama fonksiyonu
    def yasHesapla(dogumYili):
        mevcutYil = datetime.now().year
        yas = mevcutYil - dogumYili
        return yas
    
    yas = yasHesapla(dogumYili)
    
    if yas >= 65:
        print("Emekli oldunuz.")
    else:
        kalanYil = 65 - yas
        print(f"{isim}, emekliliğinize {kalanYil} yıl kaldı.")


emeklilikDurumu(isim, dogumYili)