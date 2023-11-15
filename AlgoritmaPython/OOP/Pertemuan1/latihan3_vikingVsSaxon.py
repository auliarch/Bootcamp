# class Pasukan:
#     def __init__(self, prajurit):
#         self.prajurit = prajurit

#     def jumlah_prajurit(self):
#         return self.prajurit

class Pertempuran:
    def __init__(self, v, s):
        self.viking = v
        self.saxon = s

    def pemenang(self):
        if self.viking * 4 > self.saxon:
            return f'viking menang'
        elif self.viking * 4 < self.saxon:
            return f'saxon menang'
        else:
            return f'imbang'

pertempuran01 = Pertempuran(5, 18)
pertempuran02 = Pertempuran(10, 41)
pertempuran03 = Pertempuran(1, 4)

assert pertempuran01.pemenang() == "viking menang"
assert pertempuran02.pemenang() == "saxon menang"
assert pertempuran03.pemenang() == "imbang"