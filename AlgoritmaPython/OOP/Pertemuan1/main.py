# Penjelasan 1
# Pembuatan class
# class Manusia:
#     nama = ""
#     umur = 0

# orang01 = Manusia() # <= Konstruktor
# orang01.nama = "Aulia"
# orang01.umur = 19

# print(orang01.nama)
# print(orang01.umur)

# Penjelasan 2
# Pembuatan kelas
class Manusia:

    def __init__(self, nm = "Anonim", um = 5): # <= Memberi nilai default
        self.nama = nm
        self.umur = um

    def makan(self):
        return f'{self.nama} makan'
    
    def berjalan(self):
        return f'{self.nama} berjalan'
    
    def belajar(self):
        return f'{self.nama} belajar'

# Pembuatan objek/instance
orang01 = Manusia("Aulia", 19)
print(orang01.nama, orang01.umur, orang01.makan(), orang01.berjalan(), orang01.belajar())

# orang02 = Manusia("Nanda", 18)
# print(orang02.nama, orang02.umur)

# orang03 = Manusia("Rizky", 19)
# print(orang03.nama, orang03.umur)

# orang04 = Manusia("Naufal", 21)
# print(orang04.nama, orang04.umur)

# orang05 = Manusia("Azim", 21)
# print(orang05.nama, orang05.umur)

# orang06 = Manusia()
# print(orang06.nama, orang06.umur) # <= Jika kosong maka akan print nilai default