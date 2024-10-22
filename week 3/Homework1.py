#Ödev-1: Değişkenlere atanmış değerlerin veri tipleri arasında dönüşüm yapılır.

a = 10      # integer
b = 8.15   # float
c = "123"  # string

# Veri tipleri arasında dönüşüm
a_to_float = float(a)  
b_to_int = int(b)      
c_to_int = int(c)      

# Sonuçları yazdırma
print(f"{a} -> float: {a_to_float}")
print(f"{b} -> int: {b_to_int}")
print(f"'{c}' -> int: {c_to_int}")

