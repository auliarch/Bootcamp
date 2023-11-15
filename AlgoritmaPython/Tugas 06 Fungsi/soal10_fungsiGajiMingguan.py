def gaji_mingguan(total_jam_kerja, jenis_pegawai):
    lembur = 48
    if total_jam_kerja >= lembur and jenis_pegawai == "A":
        return 1200000 + ((total_jam_kerja - lembur) * 20000)
    elif total_jam_kerja >= lembur and jenis_pegawai == "B":
        return 1000000 + ((total_jam_kerja - lembur) * 15000)
    
tj = int(input())
jp = input()

print(gaji_mingguan(tj, jp))