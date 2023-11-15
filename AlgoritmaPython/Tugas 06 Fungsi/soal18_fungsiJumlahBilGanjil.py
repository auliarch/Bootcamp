def jumlah_ganjil(angka1, angka2):
    jumlah = 0

    for angka in range(angka1, angka2 + 1):
        if angka % 2 != 0:
            jumlah += angka
    
    return jumlah

print(jumlah_ganjil(1, 5))

n = 3
m = 4
print(jumlah_ganjil(n, m))