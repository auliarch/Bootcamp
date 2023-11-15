#input dan casting
jumlah_pelanggan = int(input("Jumlah pelanggan: "))
waktu_tontonan = int(input("Waktu tontonan dalam 12 bulan terakhir: "))

#percabangan dan output
if jumlah_pelanggan >= 1000 and waktu_tontonan >= 4000:
    print("sudah dapat dimonetisasi")
else:
    print("belum dapat dimonetisasi")