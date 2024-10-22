#Ödev-4: Kullanıcıdan isim ve şifre isteyeceğiz ve şifre girişi için üç hak verilir.
 #1.Eğer önceden tanımlı şifre ile kullanıcıdan gelen şifre aynıysa "Giriş yapıldı." yazar. 
 #2.Şifre girişi yanlışsa "Yanlış şifre girildi!" uyarısı verilsin ve üç yanlış denemede program biter. 
 #3.Tercihe göre kalan hak bilgisi verilir. 


isim = input("İsminizi giriniz: ")
hak = 3
dogruSifre = "123456"

while hak > 0:
    sifre = input("Şifrenizi giriniz: ")

    if sifre == dogruSifre:
        print("Giriş yapıldı.")
        break
    else:
        hak -= 1
        print(f"Yanlış şifre girdiniz.Kalan deneme hakkınız: {hak}")
        if hak == 0:
            print("3 kez yanlış şifre girdiniz. Giriş hakkınız bitti.")