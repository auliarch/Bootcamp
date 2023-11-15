#input dan casting
bilangan = int(input())

#inisialiasi variabel jumlah
jumlah = 0

#perulangan untuk membaca input dan menjumlahkan bilangan ganjil kelipatan 3
while bilangan >= 0:
    #memeriksa bilangan ganjil dan kelipatan 3
    if bilangan % 2 != 0 and bilangan % 3 == 0:
        #penjumlahan
        jumlah += bilangan
    #input dan casting
    bilangan = int(input())

#output
print(jumlah)