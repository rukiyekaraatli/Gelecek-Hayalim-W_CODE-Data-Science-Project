#Ödev-2: İsimlerden oluşan üç değişkene yaş değerleri atanır. Belirlenen üç değişken birbiriyle karşılaştırma operatörleri ile karşılaştırılır. Bu karşılaştırmalara mantıksal operatörler de eklenir.

#üç değişkene yaş değerleri atama
merveAge = 26
melikeAge = 24
muratAge = 30

#Karşılaştırma
print(merveAge > muratAge)  
print(muratAge > melikeAge)   
print(merveAge == melikeAge)   
result = (melikeAge < merveAge) and (muratAge > merveAge)
print(f"Melike'nin yaşı Merve'den küçük ve Murat'ın yaşı Merve'den büyük mü? {result}")