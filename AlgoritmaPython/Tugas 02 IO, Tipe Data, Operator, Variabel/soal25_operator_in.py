daftar_angka = [1, 2, 5, 7, 9]

#input
angka = int(input("Masukkan angka: "))

#proses
if angka in daftar_angka:
    print(f"{angka} ada dalam daftar angka")
else:
    print(f"{angka} tidak ada dalam daftar angka")