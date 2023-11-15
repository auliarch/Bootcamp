# Buat kelas Lingkaran, memiliki 2 konstruktor, 
# fungsi hitung_luas dan hitung_keliling, 
# gunakan encapsulasi, gunakan setter dan getter

class Lingkaran:

    PI = 3.14

    def __init__(self, r=0):
        self.__radius = r

    def hitung_luas(self):
        return Lingkaran.PI * self.__radius ** 2

    def hitung_keliling(self):
        return Lingkaran.PI * self.__radius * 2

    def set_radius(self, r):
        if r > 0:
            self.__radius = r

    def get_radius(self):
        return self.__radius

l01 = Lingkaran(10.5)
print(l01.get_radius())
print(l01.hitung_luas())
print(l01.hitung_keliling())

l02 = Lingkaran(23.4)
print(l02.get_radius())
print(l02.hitung_luas())
print(l02.hitung_keliling())

l03 = Lingkaran()
l03.set_radius(10)          # set digunakan ketika inputan kosong/tidak diisi
print(l03.hitung_luas())
print(l03.hitung_keliling())
