#input dan casting
teks = int(input())

#inisialisasi
jumlah = 0

#perulangan
for t in str(teks):
    if t == '0':
        jumlah += 1

#output
print(jumlah)