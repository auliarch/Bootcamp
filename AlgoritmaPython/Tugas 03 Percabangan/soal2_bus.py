#input
kapasitas_bus = int(input("Masukkan jumlah kapasitas: "))
jumlah_penumpang = int(input("Masukkan jumlah penumpang: "))

#menghitung persentase penumpang
persentase = ( jumlah_penumpang / kapasitas_bus ) * 100

#percabangan untuk memeriksa kondisi
if persentase >= 50 and persentase <= 75:
    print("berangkat")
else:
    print("tidak berangkat")