# #Soal Nomor 1
# #Tulis Ukuran Balok
# panjang = int(input("Masukkan panjang balok: "))
# lebar = int(input("Masukkan lebar balok: "))
# tinggi = int(input("Masukkan tinggi balok: "))
# #Hasil Perhitungan Volume Balok
# Volume_balok = panjang * lebar * tinggi
# print("Hasil dari perhitungan volume balok adalah", Volume_balok)
# #Tulis Ukuran Tabung
# diameter = int(input("Masukkan diameter tabung: "))
# radius = int(input("Masukkan radius tabung: "))
# luas_selimut = int(input("Masukkan luas selimut tabung: "))
# tinggi_tabung = int(input("Masukkan tinggi tabung: "))
# #Hasil Perhitungan Volume Tabung
# Volume_tabung = 22/7 * radius * radius * tinggi
print("Hasil dari perhitungan volume tabung adalah", Volume_tabung)

#Soal Nomor 2
#Diketahui Suku Ke-5
u5 = 11
#Jumlah Suku Ke-8 dan Ke-12
jumlah_u8_u12 = 52
#Menghitung Beda 
b = (jumlah_u8_u12 - 2 * u5) / 10
#Menghitung Suku Pertama (a1)
a1 = u5 - 4 * b
#Menghitung Jumlah dari 8 Suku Pertama (S8)
n = 8 
S8 = (n / 2) * (2 * a1 + (n - 1) * b)
#Hasil Perhitungan
print(f"Bedanya (b) adalah: {b}")
print(f"Suku pertama (a1) adalah: {a1}")
print(f"Jumlah dari 8 suku pertama (S8) adalah: {S8}")

#Soal Nomor 3
#Diketahui
uang_us = 35
kurs_Indonesia = 15000
#Hitung Nominal dengan Mata uang Negaranya
nominal = uang_us * kurs_Indonesia
print("Nominal uang yang didapatkan Suraji dengan mata uang negaranya yaitu", nominal)

#Soal Nomor 4
#Rumus yang Digunakan yaitu c(n, r) = n! / r! (n - r)!
#c(7, 4) = 7! / 4! (7 - 4)!
#c(7, 4) = 7! / 4! * 3!
n = 7 * 6 * 5
r = 3 * 2
#Hasil Perhitungan
hasil = n * r
print("Banyak cara Darsono untuk membentuk tim yaitu", hasil)