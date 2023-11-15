class HitungHargaBubur:
    def __init__(self, sw, c, aa, t):
        self.suwir_ayam = sw
        self.cakue = c
        self.ati_ampela = aa
        self.telur = t

    def total_harga(self):
        harga_dasar = 6000

        if self.suwir_ayam:
            harga_dasar += 3000
        if self.cakue:
            harga_dasar += 1500
        if self.ati_ampela:
            harga_dasar += 4500
        if self.telur:
            harga_dasar += 4000

        return harga_dasar
    
pembeli01 = HitungHargaBubur(True, True, True, True)
pembeli02 = HitungHargaBubur(True, True, True, False)

assert pembeli01.total_harga() == 19000
assert pembeli02.total_harga() == 15000