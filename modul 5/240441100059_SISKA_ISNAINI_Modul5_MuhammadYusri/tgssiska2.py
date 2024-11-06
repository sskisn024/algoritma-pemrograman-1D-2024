n = int(input('masukan angka deret fibinoacci: '))
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

hasil = fibonacci(n)
print(f"Bilangan Fibonacci ke-{n} adalah {hasil}")
