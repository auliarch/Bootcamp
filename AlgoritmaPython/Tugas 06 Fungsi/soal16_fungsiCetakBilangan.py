def cetak_barisan_bilangan(angka1, angka2):
    for angka in range(angka1, angka2+1):
        print(angka, end=' ')

# Contoh pemanggilan fungsi
a = int(input())
b = int(input())
cetak_barisan_bilangan(a, b)