#input
teks = str(input())

#inisialisasi
jumlah = 0

#perulangan
for k in teks:
    #untuk memeriksa
    if k in 'bcdfghjklmnpqrstvwxyz':
        jumlah += 1

#output
print(jumlah)