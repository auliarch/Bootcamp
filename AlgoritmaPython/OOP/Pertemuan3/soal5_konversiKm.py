class Konversi:

    def __init__(self, kecepatan_km_per_jam):
        self.kecepatan_km_per_jam = kecepatan_km_per_jam

    def konversi_kecepatan(self):
        kecepatan_m_per_detik = self.kecepatan_km_per_jam * 0.277778
        return round(kecepatan_m_per_detik, 2)

kecepatan01 = Konversi(50.0)
print(kecepatan01.konversi_kecepatan())

kecepatan02 = Konversi(35.33)
print(kecepatan02.konversi_kecepatan())
