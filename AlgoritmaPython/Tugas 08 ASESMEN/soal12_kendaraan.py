def sewa(kapasitas):
    kapasitas_bus = 40
    kapasitas_mobil1 = 6
    kapasitas_mobil2 = 3
    # kapasitas_motor = 1
    harga_bus = 1000000
    harga_mobil1 = 300000
    harga_mobil2 = 200000
    harga_motor = 50000

    bus = kapasitas // kapasitas_bus
    sisa = kapasitas % kapasitas_bus

    mobil1 = sisa // kapasitas_mobil1
    sisa = sisa % kapasitas_mobil1

    mobil2 = sisa // kapasitas_mobil2
    sisa = sisa % kapasitas_mobil2

    motor = sisa

    jumlah_sewa = (bus * harga_bus) + (mobil1 * harga_mobil1) + (mobil2 * harga_mobil2) + (motor * harga_motor)

    return bus, mobil1, mobil2, motor, jumlah_sewa
    
orang = int(input())
buss, mobill1, mobill2, motorr, jumlah_sewaa = sewa(orang)
print(f'Kendaraan yang akan disewa adalah: {buss} bus, {mobill1} mobil1, {mobill2} mobil2, {motorr} motor dengan total sewa Rp {jumlah_sewaa}')