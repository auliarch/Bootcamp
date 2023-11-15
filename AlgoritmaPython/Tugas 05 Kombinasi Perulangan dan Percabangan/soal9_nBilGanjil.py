#input dan casting
n = int(input())

#inisialisasi
jumlah = 0
i = 0
bilangan = 1

#perulangan
while i < n:
    jumlah = jumlah + bilangan
    bilangan = bilangan + 2
    i = i + 1

#output
print(jumlah)