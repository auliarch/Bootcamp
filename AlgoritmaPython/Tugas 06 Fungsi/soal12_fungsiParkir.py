def biaya_parkir(jenis_kendaraan, lama_parkir):
    jam_pertama_mobil = 5000
    jam_pertama_motor = 2500

    if jenis_kendaraan == "mobil":
        if lama_parkir == 1:
            return jam_pertama_mobil
        elif lama_parkir > 1:
            return jam_pertama_mobil + (3500 * (lama_parkir - 1))
    elif jenis_kendaraan == "sepeda motor":
        if lama_parkir == 1:
            return jam_pertama_motor
        elif lama_parkir > 1:
            return jam_pertama_motor + (1000 * (lama_parkir - 1))

jk = input()
lp = int(input())

print(biaya_parkir(jk, lp))