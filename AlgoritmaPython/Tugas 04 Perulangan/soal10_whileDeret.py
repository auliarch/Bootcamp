#input dan casting
n = int(input())

#inisialisasi
jumlah = 1.0
i = 1

#perulangan
while i <= n:
    jumlah = jumlah + 1 / (2**i)
    i = i + 1

#output
print('{:.5f}'.format(jumlah))