def total_uang_parkir(motor, mobil):
    if jenis_kendaraan == 'motor':
        motor = 2000 + ((jam - 1) * 500)
        return motor
    elif jenis_kendaraan == 'mobil':
        mobil = 3000 + ((jam - 1) * 1000)
        return mobil
    
jenis_kendaraan, jam = map(str, input().split())

jam = int(jam)

print(total_uang_parkir(jenis_kendaraan, jam))