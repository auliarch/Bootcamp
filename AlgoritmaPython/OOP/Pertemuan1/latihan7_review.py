class Review:
    def __init__(self, nilai1, nilai2, nilai3, nilai4) :
        self.nilai1 = nilai1
        self.nilai2 = nilai2
        self.nilai3 = nilai3
        self.nilai4 = nilai4

    def hitung_rata_rata(self):
        rata_rata = (self.nilai1 + self.nilai2 + self.nilai3 + self.nilai4) / 4

        if rata_rata >= 3.50:
            return "bagus"
        elif rata_rata <= 1.50:
            return "kurang"
        else:
            return "sedang"
        
review01 = Review(4, 3, 4, 4)
review02 = Review(3, 3, 4, 1)
review03 = Review(1, 1, 1, 2)

assert review01.hitung_rata_rata() == "bagus"
assert review02.hitung_rata_rata() == "sedang"
assert review03.hitung_rata_rata() == "kurang"