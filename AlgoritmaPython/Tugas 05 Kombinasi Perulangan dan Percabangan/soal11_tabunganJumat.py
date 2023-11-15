tabungan = int(input())
jumat = int(input())

jumlah = 0

for i in range(jumat):
    jumlah += tabungan
    tabungan += 1000

print(jumlah)