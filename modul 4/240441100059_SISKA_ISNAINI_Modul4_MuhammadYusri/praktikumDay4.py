for i in range(4):
    print(f"Loop luar i = {i}")
    for x in range (4):
        print(f"Loop dalam x = {x}")

angka1 = int(input('Masukan angka pertama :'))
angka2 = int(input('Masukan angka kedua :'))

if(angka1 < 0 or angka2 < 0):
    print('angka bukanlah bilangan positif')
else:
    while angka2 != 0:
        angka1, angka2 = angka2, angka1%angka2
print(f'FPB nya adalah {angka1}')