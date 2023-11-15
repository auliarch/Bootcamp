#input
angka = int(input("Masukkan sebuah angka: "))

#proses
if angka > 0 or angka % 3 == 0:
    print(f"{angka} lebih besar dari 0 atau kelipatan dari 3")
else:
    print(f"{angka} tidak lebih besar dari 0 atau kelipatan dari 3")