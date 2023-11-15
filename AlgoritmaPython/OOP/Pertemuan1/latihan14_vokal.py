class Vokal:
    def __init__(self, kata):
        self.kata = kata

    def cek_vokal(self):
        if "a" in self.kata or "i" in self.kata or "u" in self.kata or "e" in self.kata or "o" in self.kata:
            return "ya"
        else:
            return "tidak"
        
kata01 = Vokal("makan")
kata02 = Vokal("aeuei")
kata03 = Vokal("xyztx")

assert kata01.cek_vokal() == "ya"
assert kata02.cek_vokal() == "ya"
assert kata03.cek_vokal() == "tidak"