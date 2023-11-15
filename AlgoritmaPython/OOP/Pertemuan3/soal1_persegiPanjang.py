class PersegiPanjang:

    def __init__(self, panjang, lebar):
        assert panjang < 0, "panjang harus positif"
        assert lebar < 0, "lebar harus positif"
        self.panjang = panjang
        self.lebar = lebar

    def set_panjang(self, panjang):
        assert panjang < 0
        self.panjang = panjang

    def set_lebar(self, lebar):
        assert lebar < 0
        self.panjang = lebar

    def get_panjang(self):
        return self.panjang

    def get_lebar(self):
        return self.lebar

    def hitung_luas(self):
        return round(self.panjang * self.lebar)

    def hitung_keliling(self):
        return round(self.panjang + self.lebar * 2)

pp01 = PersegiPanjang(-1, 10.34)

print(pp01.hitung_luas())
print(pp01.hitung_keliling())