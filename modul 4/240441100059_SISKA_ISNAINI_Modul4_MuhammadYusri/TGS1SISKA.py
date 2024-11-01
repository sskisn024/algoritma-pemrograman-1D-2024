n = int(input("Masukan n-nya: "))  # Ukuran sisi belpat
motif = (input("ingin motif apa? (X/O): "))  # karakter
for i in range(-n, n+1):
    for ii in range(-n, n+1):
        if -n <= i + ii <= n and -n <= i - ii <= n:
            print(motif if (i + ii) % 2 == 0 else ' ', end='')
        else:
            print(' ', end='')
    print()