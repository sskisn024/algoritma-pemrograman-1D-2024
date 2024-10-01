#Soal Nomor 1
#Tulis Ukuran Balok
panjang = int(input("Masukkan panjang balok: "))
lebar = int(input("Masukkan lebar balok: "))
tinggi = int(input("Masukkan tinggi balok: "))
#Hasil Perhitungan Volume Balok
Volume_balok = panjang * lebar * tinggi
print("Hasil dari perhitungan volume balok adalah", Volume_balok)
#Tulis Ukuran Tabung
diameter = int(input("Masukkan diameter tabung: "))
radius = int(input("Masukkan radius tabung: "))
luas_selimut = int(input("Masukkan luas selimut tabung: "))
tinggi_tabung = int(input("Masukkan tinggi tabung: "))
#Hasil Perhitungan Volume Tabung
Volume_tabung = 22/7 * radius * radius * tinggi
print("Hasil dari perhitungan volume tabung adalah", Volume_tabung)