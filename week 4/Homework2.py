#Ödev-2: Kullanıcıdan kullanıcı adı ve şifre oluşturmasını istenir. Şifrenin uzunluğu altı haneye ulaşmışsa hesabınız oluşturuldu mesajı alınır, altı haneden azsa altı haneli şifre oluşturması gerektiğinin mesajı alınır. (Sadece koşul kullanılması yeterli.)

kullaniciAdi = input("Kullanıcı adınızı oluşturunuz: ")
sifre = input("Şifrenizi oluşturunuz: ")

if len(sifre) >= 6:
    print("Hesabınız başarıyla oluşturuldu.")
else:
    print("Şifreniz en az 6 haneli olmak zorundadır. Lütfen tekrar deneyiniz.")