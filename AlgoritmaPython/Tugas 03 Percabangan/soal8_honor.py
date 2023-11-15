#input dan casting
banyak_bulan = int(input())

#total casting
total = 3 * 12000000
penalti = (banyak_bulan - 3) * total * 0.3

#percabangan
if banyak_bulan > 3:
    print(total - penalti)
elif banyak_bulan == 3:
    print(total)
else:
    print(banyak_bulan * 12000000)