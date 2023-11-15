#input dan casting dan split
gol_per_hari = input().split()

#inisialisasi
total_gol = 0

#perulangan for untuk menjumlahkan total gol
for gol in gol_per_hari:
    total_gol += int(gol)

#cek dan output
if total_gol >= 10:
    print("diberi hadiah")
else:
    print("tidak diberi hadiah")