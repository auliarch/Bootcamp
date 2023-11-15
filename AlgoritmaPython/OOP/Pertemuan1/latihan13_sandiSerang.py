class SandiSerang:
    def __init__(self, a, b, c, d, e, f):
        self.kata1 = a
        self.kata2 = b
        self.kata3 = c
        self.kata4 = d
        self.kata5 = e
        self.kata6 = f

    def serang(self):
        if self.kata1[0] == "s" and self.kata2[0] == "e" and self.kata3[0] == "r" and self.kata4[0] == "a" and self.kata5[0] == "n" and self.kata6[0] == "g":
            return "serang"
        else:
            return "tidak serang"
        
sandi01 = SandiSerang("sayang", "engkau", "rugi", "andaikan", "nggak", "gerak")
sandi02 = SandiSerang("maaf", "udah", "ninggalin", "dikau", "untuk", "rembulan")

assert sandi01.serang() == "serang"
assert sandi02.serang() == "tidak serang"