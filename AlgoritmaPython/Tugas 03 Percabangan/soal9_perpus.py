#input dan casting
jumlah_hari_terlambat = int(input())

#percabangan
if jumlah_hari_terlambat <= 5:
    print(jumlah_hari_terlambat * 1000)
elif 5 <= jumlah_hari_terlambat <= 10:
    print(jumlah_hari_terlambat * 2000)
else:
    print("cabut keanggotaan")