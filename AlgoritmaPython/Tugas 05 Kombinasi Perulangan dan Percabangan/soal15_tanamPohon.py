#inisialisasi
total_waktu = 0
jumlah_hari = 0

#percabangan
while True:
    #input dan casting
    waktu = int(input())
    #periksa waktu negatif atau tidak
    if waktu < 0:
        break
    #menghitung total waktu
    total_waktu += waktu
    jumlah_hari += 1

#menghitung rata-rata
rata_rata = total_waktu / jumlah_hari

#output
print('{:.2f}'.format(rata_rata))