harga_makanan = int(input())
harga_minuman = int(input())
tip = input()

total_bayar = harga_makanan + harga_minuman

if tip == 'false':
    print(total_bayar)
elif tip == 'true':
    print(total_bayar + 5000)