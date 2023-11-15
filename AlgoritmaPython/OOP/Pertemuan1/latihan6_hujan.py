class Hujan:
    def __init__(self, h, p):
        self.hujan_turun = h
        self.punya_payung = p

    def kondisi(self):
        if self.hujan_turun == "tidak" or self.punya_payung == "ya":
            return "berangkat"
        else:
            return "diam di rumah"
        
kondisi01 = Hujan("tidak", "ya")
kondisi02 = Hujan("tidak", "tidak")
kondisi03 = Hujan("ya", "tidak")

assert kondisi01.kondisi() == "berangkat"
assert kondisi02.kondisi() == "berangkat"
assert kondisi03.kondisi() == "diam di rumah"