#Ödev-3: Kullanıcıdan iki değer girmesini istenir. Girilen değerlerin toplama, çıkarma, çarpma, bölme sonuçlarını yazdırılır.

# Kullanıcıdan iki değer girmesini isteme
sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))

# Dört işlem sonuçları
toplama = sayi1 + sayi2
cikarma = sayi1 - sayi2
carpma = sayi1 * sayi2
bolme = sayi1 / sayi2 if sayi2 != 0 else "Bölme işlemi yapılamaz."
print(f"Toplama: {toplama}")
print(f"Çıkarma: {cikarma}")
print(f"Çarpma: {carpma}")
print(f"Bölme: {bolme}")