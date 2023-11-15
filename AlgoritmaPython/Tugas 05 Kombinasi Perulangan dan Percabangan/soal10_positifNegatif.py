#inisialisasi variabel nomor
nomor = 1

#inisialisasi
banyak_bil_pos = 0
banyak_bil_neg = 0

#perulangan untuk membaca input dan mencacah banyak bilangan positif & negatif
while nomor <= 10:
    #input dan casting
    bilangan = int(input())
    #memeriksa bilangan bulat positif
    if bilangan > 0:
        banyak_bil_pos += 1
    elif bilangan < 0:
        banyak_bil_neg += 1
    nomor += 1

#output
print(banyak_bil_pos)
print(banyak_bil_neg)