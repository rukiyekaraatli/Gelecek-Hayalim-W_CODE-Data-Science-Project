 #Ödev-1: 
 #1.Sayılardan oluşan bir boyutlu array oluşturulur. Arrayi oluştururken sayıların veri tipini integer olarak belirtilir. Oluşturulan arrayin boyut, eleman sayısı bilgilerine bakılır. 

 #Ödev-2:
 #2.İki ve üç boyutlu arrayler oluşturulur. Bu arraylerin boyut, eleman sayısı, satır, sütun bilgilerine ulaşılır. Arrayler üzerinde indexleme ve dilimleme(slicing) işlemi yapılır. 

 #Ödev-3:
 #3.Numpy fonksiyonu kullanarak bir, iki ve üç boyutlu arrayler oluşturulur. Arrayler üzerinde indexleme ve dilimleme(slicing) işlemi yapılır.

 #Ödev-4: 
 #4.Sıfırlardan oluşan ve birlerden oluşan iki tane iki boyutlu array oluşturulur. Bu arrayler satır ve sütun bazında birleştirilir. 


import numpy as np

#1.örnek
array_1d = np.array([1, 2, 3, 4, 5], dtype=int)
print("Bir boyutlu array:", array_1d)
print("Array'in boyutu:", array_1d.ndim)
print("Array'in eleman sayısı:", array_1d.size)
print("Array'in şekli:", array_1d.shape)

#2.örnek
array_2d = np.array([[1, 2, 3], [4, 5, 6]], dtype=int)
print("\nİki boyutlu array:")
print(array_2d)
print("Array'in boyutu:", array_2d.ndim)
print("Array'in eleman sayısı:", array_2d.size)
print("Array'in şekli:", array_2d.shape)  
array_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]], dtype=int)
print("\nÜç boyutlu array:")
print(array_3d)
print("Array'in boyutu:", array_3d.ndim)
print("Array'in eleman sayısı:", array_3d.size)
print("Array'in şekli:", array_3d.shape)  

#3.örnek
print("\nİki boyutlu array üzerinde indexleme:")
print("array_2d[0, 1] =", array_2d[0, 1]) 
print("\nÜç boyutlu array üzerinde indexleme:")
print("array_3d[1, 0, 2] =", array_3d[1, 0, 2]) 
print("\nİki boyutlu array üzerinde dilimleme:")
print("array_2d[:, 1:] =\n", array_2d[:, 1:])  
print("\nÜç boyutlu array üzerinde dilimleme:")
print("array_3d[1, :, :2] =\n", array_3d[1, :, :2]) 

#4.örnek
zeros_array = np.zeros((2, 3), dtype=int)
print("\nSıfırlardan oluşan array:")
print(zeros_array)
ones_array = np.ones((2, 3), dtype=int)
print("\nBirlerden oluşan array:")
print(ones_array)
combined_v = np.vstack((zeros_array, ones_array))
print("\nSatır bazında birleştirilmiş array (vstack):")
print(combined_v)
combined_h = np.hstack((zeros_array, ones_array))
print("\nSütun bazında birleştirilmiş array (hstack):")
print(combined_h)

