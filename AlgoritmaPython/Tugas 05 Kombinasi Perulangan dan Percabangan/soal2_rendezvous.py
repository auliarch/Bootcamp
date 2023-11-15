#input dan casting
x = int(input())
y = int(input())

#inisialisasi variabel jumlah pertemuan rahasia
jumlah_pertemuan = 0

#perulangan for
for hari in range(1, 361):
    #memeriksa kondisi yang memenuhi syarat pertemuan rahasia
    if hari % x == 0 and hari % y != 0:
        #menjumlahkan pertemuan rahasia
        jumlah_pertemuan += 1

#cetak jumlah pertemuan rahasia
print(jumlah_pertemuan)