class Perpustakaan:
    def __init__(self, hk):
        self.hari_keterlambatan = hk

    def denda(self):
        if self.hari_keterlambatan <= 5:
            return self.hari_keterlambatan * 1000
        elif 5 <= self.hari_keterlambatan <= 10:
            return self.hari_keterlambatan * 2000
        else:
            return "cabut keanggotaan"
        
peminjam01 = Perpustakaan(3)
peminjam02 = Perpustakaan(5)
peminjam03 = Perpustakaan(6)
peminjam04 = Perpustakaan(25)

assert peminjam01.denda() == 3000
assert peminjam02.denda() == 5000
assert peminjam03.denda() == 12000
assert peminjam04.denda() == "cabut keanggotaan"