class Penghasilan:
    def __init__(self, bulan):
        self.banyak_bulan = bulan

    def honor(self):
        total = 3 * 12000000
        penalti = (self.banyak_bulan - 3) * total * 0.3

        if self.banyak_bulan > 3:
            return total - penalti
        elif self.banyak_bulan == 3:
            return total
        else:
            return self.banyak_bulan * 12000000
        
honor01 = Penghasilan(3)
honor02 = Penghasilan(4)
honor03 = Penghasilan(5)

assert honor01.honor() == 36000000
assert honor02.honor() == 25200000.0
assert honor03.honor() == 14400000.0