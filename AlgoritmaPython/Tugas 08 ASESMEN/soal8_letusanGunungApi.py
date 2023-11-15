def jumlah_letusan(x_tahun, y_tahun, n_tahun):
    jumlah = 0
    tahun_awal = x_tahun

    while tahun_awal < n_tahun:
        jumlah += 2
        tahun_awal += x_tahun + y_tahun

    return jumlah

x, y, n = map(int, input().split())
print(jumlah_letusan(x, y, n))