#input dan split
teks = str(input().split())

#inisialisasi variabel
jumlah = 0

#perulangan for
for kata in teks:
    if kata.isnumeric():
        jumlah += int(kata)

#output
print(jumlah)