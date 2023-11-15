#input
kata = input()

#menghilangkan spasi
kata = kata.replace(" ", "")

#inisialisasi
panjang_kata = len(kata)
is_palindrom = True

#perulangan untuk memeriksa karakter pertama dan terakhir
for i in range(panjang_kata // 2):
    if kata[i] != kata[panjang_kata - i - 1]:
        is_palindrom = False
        break

#output
print(is_palindrom)