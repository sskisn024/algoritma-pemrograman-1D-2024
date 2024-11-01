# Data variabel 
gaji_harian = 100000
total_gaji_reguler = gaji_harian * 7
total_gaji_lembur = 0
total_jam_lembur = 0

# Input jam lembur per hari selama 7 hari
jam_lembur_per_hari = [0] * 7  # Membuat list dengan 7 elemen awalnya 0
for i in range(7):
    jam = int(input(f"Masukkan jam lembur hari ke-{i + 1}: "))
    jam_lembur_per_hari[i] = jam  
print()

# Menghitung gaji mingguan termasuk lembur
for i in range(7):
    jam_lembur = jam_lembur_per_hari[i]
    if jam_lembur > 8:
        print(f"Lembur hari ke-{i + 1}: {jam_lembur} jam, Lembur melebihi batas, tidak dihitung.")
        lembur_hari_ini = 0
    elif total_jam_lembur + jam_lembur > 40:
        print(f"Lembur hari ke-{i + 1}: {jam_lembur} jam, Total jam lembur dalam seminggu sudah mencapai batas, lembur dihentikan.")
        lembur_hari_ini = 0
    else:
        total_jam_lembur += jam_lembur
        if jam_lembur == 0:
            lembur_hari_ini = 0
        elif 1 <= jam_lembur <= 3:
            lembur_hari_ini = jam_lembur * 25000
        elif jam_lembur == 4:
            lembur_hari_ini = 100000
        elif jam_lembur == 6:
            lembur_hari_ini = 200000
        elif jam_lembur == 8:
            lembur_hari_ini = 300000
        else:
            lembur_hari_ini = 0  # Jika lebih dari 8 jam, tidak dihitung
    total_gaji_lembur += lembur_hari_ini
    print(f"Lembur hari ke-{i + 1}: {jam_lembur} jam, Gaji lembur hari ini: Rp{lembur_hari_ini}")
print()
# Total
total_gaji_mingguan =  total_gaji_reguler + total_gaji_lembur
# Hasilnya
print(f"Total jam lembur selama satu minggu: {total_jam_lembur} jam")
print(f"Total gaji lembur: Rp{total_gaji_lembur}")
print(f"Total gaji mingguan tanpa lembur: Rp{total_gaji_reguler}")
print(f"Total gaji mingguan termasuk lembur: Rp{total_gaji_mingguan}")
