class Bola:

    PHI = 3.14

    def __init__(self, r):
        assert r > 0
        self.jari_jari = r

    def volume_bola(self):
        return round(4/3 * Bola.PHI * self.jari_jari ** 2, 2)

    def luas_permukaan_bola(self):
        return round(4 * Bola.PHI * self.jari_jari ** 2, 4)

bola01 = Bola(5.5)
print(bola01.volume_bola())

bola02 = Bola(12.5)
print(bola02.volume_bola())

bola03 = Bola(12.0034)
print(bola03.luas_permukaan_bola())

bola04 = Bola(5.5123)
print(bola04.luas_permukaan_bola())