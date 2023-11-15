def penjumlahan_lewat_100(bilangan2):
    jumlah = 0
    total_jumlah = 0

    for angka in bilangan2:
        jumlah += angka
        total_jumlah += 1

        if jumlah > 100:
            break

    hasil = jumlah, total_jumlah
    return ' '.join(str(x) for x in hasil)

bilangan = list(map(int, input().split()))
print(penjumlahan_lewat_100(bilangan))