#Kaggle’dan bulunan bir veri seti üzerinde analiz ve görselleştirme çalışmaları yapılır.
#Turkish Poems - data set

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dosyayolu=r"E:\python\WCode-Gelecek-Hayalim-Data-Science\week7\all_poems.csv"
df = pd.read_csv(dosyayolu)
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
df.dropna(inplace=True) 

#Görselleştirme
poet_counts = df['poet_name'].value_counts()  

#Çubuk grafiği 
plt.figure(figsize=(14, 8))
sns.barplot(x=poet_counts.index, y=poet_counts.values)
plt.xticks(rotation=90)
plt.title('Şair Başına Düşen Şiir Sayısı')
plt.xlabel('Şiir')
plt.ylabel('Şiir Sayısı')
plt.subplots_adjust(bottom=0.25) #alt boşluk için
plt.show()

