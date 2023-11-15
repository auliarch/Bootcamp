class CurahHujan:
    def __init__(self, ch):
        self.curah_hujan = ch

    def kondisi(self):
        if self.curah_hujan == "sangat tinggi":
            return "macet"
        else:
            return "tidak macet"
        
kondisi01 = CurahHujan("sangat tinggi")
kondisi02 = CurahHujan("tidak sangat tinggi")

assert kondisi01.kondisi() == "macet"
assert kondisi02.kondisi() == "tidak macet"