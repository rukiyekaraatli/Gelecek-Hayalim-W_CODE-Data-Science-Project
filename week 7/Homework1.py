#sozluk = {"Kategori": ["Giyim","Giyim", "Ayakkabı","Aksesuar","Ayakkabı","Giyim","Aksesuar","Aksesuar","Ayakkabı","Giyim"],
    #"Ürün" : ["Kazak","T-shirt","Sandalet","Küpe","Spor Ayakkabı","Pantolon","Kolye","Yüzük","Çizme","Ceket"],
    #"Fiyat" : [300,180,450,50,700,400,150,80,850,900]}

#Yukarıdaki sözlük DataFrame’e dönüştürülür. 

    #Yukarıdaki DataFrame için 
        #2.indexte bulunan kategori bulunur. (Sadece kategori bilgisi) 
        #2. indexte bulunan ürün bulunur. (Sadece ürün bilgisi) 
        #4.indexten 9.indexe kadar olan veriler bulunur. (Kategori,ürün,fiyat bilgisi beraber) 
        #1.indexten 6.indexe kadar olan ürünler bulunur. (Sadece ürün bilgisi) 

    #Yukarıdaki DataFrame için 
        #Giyim kategorisinde bulunan ürünler gösterilir. 
        #Ayakkabı kategorisinde bulunan ürünler gösterilir. 
        #Aksesuar kategorisinde bulunan ürünler gösterilir. 

    #Yukarıdaki DataFrame için 
        #Giyim kategorisinde fiyatı 300'den fazla olan ürünler gösterilir. 
        #Ayakkabı kategorisinde fiyatı 600'den az olan ürünler gösterilir. 
        #Aksesuar kategorisinde fiyatı 100'den fazla olan aksesuar gösterilir. 


import pandas as pd

sozluk = {
    "Kategori": ["Giyim", "Giyim", "Ayakkabı", "Aksesuar", "Ayakkabı", "Giyim", "Aksesuar", "Aksesuar", "Ayakkabı", "Giyim"],
    "Ürün": ["Kazak", "T-shirt", "Sandalet", "Küpe", "Spor Ayakkabı", "Pantolon", "Kolye", "Yüzük", "Çizme", "Ceket"],
    "Fiyat": [300, 180, 450, 50, 700, 400, 150, 80, 850, 900]
}
#DataFrame oluşturma
df = pd.DataFrame(sozluk)
print("Oluşturulan DataFrame:\n", df)

kategori_2 = df.loc[2, "Kategori"]
print("\n2. index'teki kategori:", kategori_2)

urun_2 = df.loc[2, "Ürün"]
print("\n2. index'teki ürün:", urun_2)

veriler_4_9 = df.loc[4:9]
print("\n4. index'ten 9. index'e kadar olan veriler:\n", veriler_4_9)

urunler_1_6 = df.loc[1:6, "Ürün"]
print("\n1. index'ten 6. index'e kadar olan ürünler:\n", urunler_1_6)

giyim_urunleri = df[df["Kategori"] == "Giyim"]
print("\nGiyim kategorisinde bulunan ürünler:\n", giyim_urunleri)

ayakkabi_urunleri = df[df["Kategori"] == "Ayakkabı"]
print("\nAyakkabı kategorisinde bulunan ürünler:\n", ayakkabi_urunleri)

aksesuar_urunleri = df[df["Kategori"] == "Aksesuar"]
print("\nAksesuar kategorisinde bulunan ürünler:\n", aksesuar_urunleri)

#Fiyat bazında filtreleme
giyim_fiyat_300 = df[(df["Kategori"] == "Giyim") & (df["Fiyat"] > 300)]
print("\nGiyim kategorisinde fiyatı 300'den fazla olan ürünler:\n", giyim_fiyat_300)

ayakkabi_fiyat_600 = df[(df["Kategori"] == "Ayakkabı") & (df["Fiyat"] < 600)]
print("\nAyakkabı kategorisinde fiyatı 600'den az olan ürünler:\n", ayakkabi_fiyat_600)

aksesuar_fiyat_100 = df[(df["Kategori"] == "Aksesuar") & (df["Fiyat"] > 100)]
print("\nAksesuar kategorisinde fiyatı 100'den fazla olan ürünler:\n", aksesuar_fiyat_100)