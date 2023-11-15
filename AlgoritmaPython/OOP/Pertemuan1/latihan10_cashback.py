class Swalayan:
    def __init__(self, p1, p2, p3, p4, p5):
        self.poin1 = p1
        self.poin2 = p2
        self.poin3 = p3
        self.poin4 = p4
        self.poin5 = p5

    def promo(self):
        cashback = (self.poin1 + self.poin2 + self.poin3) == (self.poin3 + self.poin4 + self.poin5)
        diskon = ((self.poin2 + self.poin3 + self.poin4) % (self.poin1 + self.poin5)) == 0

        if cashback and diskon:
            return "cashback\ndiskon"
        else:
            if cashback:
                return "cashback"
            elif diskon:
                return "diskon"
            
pembeli01 = Swalayan(3, 4, 5, 2, 5)
pembeli02 = Swalayan(2, 2, 2, 4, 2)
pembeli03 = Swalayan(2, 7, 6, 5, 4)

assert pembeli01.promo() == "cashback"
assert pembeli02.promo() == "diskon"
assert pembeli03.promo() == "cashback\ndiskon"