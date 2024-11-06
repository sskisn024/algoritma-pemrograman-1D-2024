# # kalimat = input("masukan kalimat: ")
# # kalimatkedua = ""

# # for i in range (len(kalimat) -1, -1, -1):
# #     kalimatkedua += kalimat [i]

# # if (kalimat == kalimatkedua):
# #     print(f"{kalimat} ini adalah kata pelindrom")
# # else:
# #     print(f"{kalimat} ini bukan kata palindrom")



# kata = "katak"
# tampung = ""

# def kalimat (kata,tampung):
#     for i in range (len(kalimat)-1,-1,-1):
#         tampung += kata [i]
#     if (kata == tampung):
#         print ("ini pelindrom")
#     else:
#         print("bukan")

# hasil = kalimat(kata, tampung)
# print(f"{hasil}")

kata = input("Maasukan kata atau kalimat: ")
def kalimat (kata):
    balik = ""
    for i in range (len(kata)-1,-1,-1):
        balik += kata [i]
    return kata == balik

hasil = kalimat(kata)

if hasil:
    print(f"{kata} ini adalah kata pelindrom")

else:
    print(f"{kata} ini bukan kata palindrom")
