keanggotaan = input("Jenis keanggotaanya(gold/silver/bronze): ")
total_belanja = int(input("Total belanja: "))

def calculate_discount(total_belanja, keanggotaan):
    if total_belanja > 1000000:
        return 5
    if keanggotaan == "gold":
        return 15
    elif keanggotaan == "silver":
        return 10
    elif keanggotaan == "bronze":
        return 5
    else:
        return 0

diskon_persen = calculate_discount(total_belanja, keanggotaan)
total_diskon = (diskon_persen / 100) * total_belanja
total_setelah_diskon = total_belanja - total_diskon
 
print(f"Diskon yang didapat: Rp.{total_diskon: }")  
print(f"Total setelah diskon: Rp.{total_setelah_diskon: }")



























keanggotan = ("bronze/silver/gold")
total = int()