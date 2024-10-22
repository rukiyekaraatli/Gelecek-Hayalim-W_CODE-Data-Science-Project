# Gerekli kütüphaneleri içe aktar
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#dosya yolu
artists_df = pd.read_csv('E:/python/WCode-Gelecek-Hayalim-Data-Science/WCode-Gelecek-Hayalim-Data-Science/week8/artists.csv')

# Veri seti hakkında genel bilgi edinme
print(artists_df.info())  
print(artists_df.describe())  
print(artists_df.head())

# Eksik verileri kontrol etme
print(artists_df.isnull().sum())

# sütunların isimlerini yazdırma
print(artists_df.columns)

#Görselleştirme---------------------------------------------------------------------------!!!

# Ülkelere göre sanatçı sayısını hesaplayalım
nationality_counts = artists_df['nationality'].value_counts()

# Çubuk grafik oluşturalım
plt.figure(figsize=(10,6))
sns.barplot(x=nationality_counts.index, y=nationality_counts.values, palette="magma")
plt.title('Ülkelere Göre Sanatçı Sayısı',pad=20)
plt.xticks(rotation=90)
plt.xlabel('Ülkeler', labelpad=20)
plt.ylabel('Sanatçı Sayısı')
plt.show()

genre_counts = artists_df['genre'].value_counts()

# Çubuk grafik
plt.figure(figsize=(10,6))
sns.barplot(x=genre_counts.index, y=genre_counts.values, palette="coolwarm")
plt.title('Sanat Tarzlarına Göre Sanatçı Sayısı',pad=20)
plt.xticks(rotation=90)
plt.xlabel('Sanat Tarzları',labelpad=20)
plt.ylabel('Sanatçı Sayısı',labelpad=20)
plt.show()

# Eser sayısına göre sanatçıları analiz edelim
plt.figure(figsize=(10,6))
sns.histplot(artists_df['paintings'], bins=20, kde=True)
plt.title('Sanatçıların Eser Sayısına Göre Dağılımı',pad=20)
plt.xlabel('Eser Sayısı')
plt.ylabel('Sanatçı Sayısı')
plt.show()



