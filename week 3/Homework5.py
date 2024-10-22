#Ödev-5: "Hi-Kod Veri Bilimi Atölyesi" ifadesini bir değişkene tanımlanır.

#İfadedeki her bir kelimeyi ("Gelecek Hayalim: W-Code", "Veri", "Bilimi", "Atölyesi") değişken içinden seçilir.

#İfadeyi hepsini büyük harf olacak hale çevrilir. ("GELECEK HAYALİM: W-CODE VERİ BİLİMİ ATÖLYESİ")

#İfadeyi hepsini büyük harf olacak hale çevrilir.("gelecek hayalim: w-code veri bilimi atölyesi")

#"0123456789" ifadesindeki yalnızca çift sayıları ve yalnızca tek sayıları seçilir. ("02468", "13579")

# Verilen ifadeyi değişkene atama
ifade = "Hi-Kod Veri Bilimi Atölyesi"

# İfadeden kelimeleri ayır
hi_kod = ifade.split()[0]  # "Hi-Kod"
veri = ifade.split()[1]    # "Veri"
bilimi = ifade.split()[2]  # "Bilimi"
atolyesi = ifade.split()[3]  # "Atölyesi"

# İfadeyi büyük harfe çevir
upper_case_ifade = ifade.upper()
print(f"Büyük harf hali: {upper_case_ifade}")

# İfadeyi küçük harfe çevir
lower_case_ifade = ifade.lower()
print(f"Küçük harf hali: {lower_case_ifade}")

# Çift ve tek sayıları seç
numbers = "0123456789"
tek_sayilar = numbers[1::2]  # "13579"
cift_sayilar = numbers[::2]  # "02468"

print(f"Tek sayılar: {tek_sayilar}")
print(f"Çift sayılar: {cift_sayilar}")
