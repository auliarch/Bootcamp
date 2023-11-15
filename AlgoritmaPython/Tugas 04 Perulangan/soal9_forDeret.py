# input dan casting
n = int(input())

# inisialisasi
jumlah = 1.0

# perulangan
for i in range(1, n+1):      
    jumlah = jumlah + 1 / (2**i)

# output
print('{:.5f}'.format(jumlah))