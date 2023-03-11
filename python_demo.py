#ÖRNEK 1 - Giriş İçin Kullanılan Karar Yapısı 

#kullanıcı mail ve şifresi 
kullanici_email = "12345@gmail.com"
kullanici_password = "12345"

#kullanıcıdan giriş için mail ve şifresi istenir
email = input("E-mail giriniz:")
password = input("Şifre giriniz:")

#karar yapıları kullanılarak bilgilerin kontrolü sağlanır
if email == kullanici_email:
    if password == kullanici_password:
      print("Giriş Başarılı")
    else:
       print("Parola Hatalı!")  
else:
    print("Giriş Başarısız!")

print("**********************************")

#ÖRNEK 2 - Ödev Tamamlanmasıyla Kurs Bitirme Oranının Artış Karar Yapısı

#ödevin yapılma durumu false olarak atanmıştır
odev = False

#ödevin yapılıp yapılmadığı sorgulanr
print("Ödevi Bitir ve Devam Et?")

#alınan yanıta göre ödevin yapılma durumu değişir
yanit = input("Evet İçin 1, Hayır İçin 2: ")
if yanit == "1":
   odev = True
else:
   odev = False

#ödevin yapılma durumuna göre tamamlanma oranı değşikliği yapılır
if odev == True:
   print("Tamamlanma Yüzdeniz Arttı")
else:
   print("Tamamlanma Yüzdeniz Değişmedi.")
   