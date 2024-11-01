n = int(input("Masukkan bilangan desimal: "))
biner = ''
angka = n
while angka > 0:
    biner = str(angka % 2) + biner
    angka = angka // 2
# Segitiga
panjang = len(biner)
for i in range(1, panjang + 1):
    print(biner[:i])
    