#Ödev-1:
#Bir sözlük oluşturulur ve bu sözlükte öğrencilerin isimleri ve Matematik, Fizik, Kimya notları tutulur. Kullanıcıdan isim ve ders ismi(Matematik, Fizik, Kimya) istenir ve bu bilgilere göre çıktı verilir.

#Sözlük üzerinde değerleri değiştirme, yeni değer ekleme, kullanıcıya ulaşmak istediği bilgileri sorma gibi uygulamalar yapın.


StudentNotes = {
    "Merve": {"Matematik": 100, "Fizik": 100, "Kimya": 95},
    "Melike": {"Matematik": 75, "Fizik": 55, "Kimya": 100},
    "Murat": {"Matematik": 65, "Fizik": 50, "Kimya": 80}
}

isim = input("Öğrencinin ismini giriniz: ")
dersAdi = input("Ders ismini giriniz(Matematik, Fizik, Kimya): ")

if isim in StudentNotes:
    if dersAdi in StudentNotes[isim]:
        print(f"{isim}'in {dersAdi} notu: {StudentNotes[isim][dersAdi]}")
    else:
        print(f"{isim} isimli öğrencinin {dersAdi} notu bulunamadı.")
else:
    print(f"{isim} isimli öğrenci bulunamadı.")


#Değerleri değiştirme 
isim = input("Notunu güncellemek istediğiniz öğrencinin ismini girin: ")
ders = input("Notunu güncellemek istediğiniz ders ismini girin (Matematik, Fizik, Kimya): ")
yeni_not = int(input(f"{isim}'in {ders} için yeni notunu girin: "))

#Öğrencinin ders notunu güncelle
if isim in StudentNotes:
    if ders in StudentNotes[isim]:
        StudentNotes[isim][ders] = yeni_not
        print(f"{isim}'in {ders} notu güncellendi: {StudentNotes[isim][ders]}")
    else:
        print(f"{isim} isimli öğrencinin {ders} dersi bulunamadı.")
else:
    print(f"{isim} isimli öğrenci bulunamadı.")

#Yeni öğrenci eklemek için isim ve not bilgilerini alalım
isim = input("Yeni öğrencinin ismini girin: ")
matematik_notu = int(input(f"{isim}'in Matematik notunu girin: "))
fizik_notu = int(input(f"{isim}'in Fizik notunu girin: "))
kimya_notu = int(input(f"{isim}'in Kimya notunu girin: "))

#Yeni öğrenciyi sözlüğe ekleme
StudentNotes[isim] = {
    "Matematik": matematik_notu,
    "Fizik": fizik_notu,
    "Kimya": kimya_notu
}
print(f"{isim} isimli öğrenci başarıyla eklendi.")


#Tüm öğrencilerin notlarını yazdırma
for ogrenci, notlar in StudentNotes.items():
    print(f"{ogrenci}:")
    for ders, notu in notlar.items():
        print(f"  {ders}: {notu}")