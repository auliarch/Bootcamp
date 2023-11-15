class Bus:
    def __init__(self, k, jp):
        self.kapasitas = k
        self.jumlah_penumpang = jp

    def berangkat(self):
        persen = self.jumlah_penumpang / self.kapasitas
        if persen >= 0.5 and persen <= 0.75:
            return f'berangkat'
        else:
            return f'tidak berangkat'
        
bus007 = Bus(40, 20)
bus008 = Bus(40, 30)
bus009 = Bus(40, 19)
bus010 = Bus(40, 31)

assert bus007.berangkat() == "berangkat"
assert bus008.berangkat() == "berangkat"
assert bus009.berangkat() == "tidak berangkat"
assert bus010.berangkat() == "tidak berangkat"