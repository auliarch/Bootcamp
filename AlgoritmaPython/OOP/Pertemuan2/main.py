class Lingkaran:

    PI = 3.14       # atribut level kelas(class)
    counter = 0
    data = list()

    def __init__(self, radius):
        self.radius = radius # atribut level instance
        Lingkaran.counter = Lingkaran.counter + 1 # ambil class
        Lingkaran.data.append(self.hitung_luas())

    def hitung_luas(self):
        return Lingkaran.PI * self.radius ** 2
    
    @classmethod         # milik class
    def cetak(cls):
        return 'hello'
    
l01 = Lingkaran(10)
print(l01.hitung_luas())
print(Lingkaran.counter) # bisa dipanggil dengan "print(l01.counter)"
print(Lingkaran.data)    # bisa dipanggil dengan "print(l01.data)"

l02 = Lingkaran(20)
print(l02.hitung_luas())
print(Lingkaran.counter)
print(Lingkaran.data)

l03 = Lingkaran(30)
print(l03.hitung_luas())
print(Lingkaran.counter)
print(Lingkaran.data)

print(Lingkaran.cetak()) # jadi dipanggilnya "Lingkaran.cetak()"

# Contoh Penggunaan '@classmethod'
class Bilangan:

    @classmethod
    def jumlah(cls, a, b):
        return a + b
    
b1 = int(input())
b2 = int(input())

print(Bilangan.jumlah(b1, b2))

# Contoh lagi
class BilanganLagi:
    @classmethod
    def jumlah(cls):
        jumlah = 0
        for i in range(1, 101):
            jumlah = jumlah + i
        return jumlah

print(BilanganLagi.jumlah())