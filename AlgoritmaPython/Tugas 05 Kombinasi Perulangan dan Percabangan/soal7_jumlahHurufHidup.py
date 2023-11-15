#input dan casting tolist
teks = list(input())

#inisialisasi variabel
jumlah = 0

#perulangan for
for karakter in teks:
    if karakter in 'aiueo':
        jumlah += 1

#output
print(jumlah)