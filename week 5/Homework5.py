#Ödev-5:
#1.Aşağıdaki işlemleri indexing ve slicing kullanarak liste üzerinde uygulayın.

        #liste = ["Python",True,9,"3",8.4,"Hi-Kod","False",4.7]

        #"3" değerine ulaşmak için indexleme yapın.

        #"Hi-Kod" değerine ulaşmak için indexleme yapın.

        #4.7 değerine ulaşmak için indexleme yapın.

        #9,"3",8.4,"Hi-Kod" değerlerine ulaşmak için slicing yapın.

        #8.4,"Hi-Kod","False",4.7 değerlerine ulaşmak için slicing yapın.

#2.Verilen listede bulunan string veri tipindeki öğeleri yeni_liste isimli listeye eklenir.

        #liste = ["Python",True,9,"3",8.4,"Hi-Kod","False",4.7]


liste = ["Python", True, 9, "3", 8.4, "Hi-Kod", "False", 4.7]
print(liste[3])
print(liste[5])
print(liste[7]) 
print(liste[2:6])
print(liste[4:8])
yeniListe = [item for item in liste if isinstance(item, str)]
print(yeniListe)

