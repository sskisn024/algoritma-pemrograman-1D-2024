nilai = int(input("masukan nilai: "))
def faktorial(nilai):
    hasil = 1
    for i in range(1, nilai+1):
        hasil *= i
        if i == nilai:
            print(i, end=" = ")
        else:
            print(i, end=" * ")
    return hasil
hasilfaktorial = faktorial (nilai)
print(f"{nilai}! {hasilfaktorial}")