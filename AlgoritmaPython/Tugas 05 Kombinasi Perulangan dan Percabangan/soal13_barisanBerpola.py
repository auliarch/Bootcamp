#input dan casting
n = int(input())
m = int(input())

#inisialisasi
suku = n
barisan = ""

#perulangan while-do untuk mencetak barisan bilangan
while suku <= m:
    #pengecekan suku adalah bilangan ganjil atau genap
    if suku % 2 == 1:
        barisan += '{:.1f}'.format(2 ** suku)
    else:
        barisan += '{:.1f}'.format(2 ** (-suku))

    #tambahkan spasi jika suku belum mencapai m
    if suku < m:
        barisan += ' '
    #tambahkan 1 setiap mencetak suku berikutnya 
    suku += 1

#output
print(barisan)