# INHERITANCE (Pewarisan)
class Manusia:          # class parent

    def __init__(self, n, jk):
        self.nama = n
        self.jk = jk

    def bekerja(self):
        return f'{self.nama} bekerja'

class Guru(Manusia):    # class anak

    def __init__(self, n, jk, NIP):
        Manusia.__init__(self, n, jk)
        self.NIP = NIP

    def bekerja(self):  # masuk ke polymorphism
        return f'{self.nama} {self.NIP} mengajar'

m01 = Manusia('Alex', 'm')
print(m01.bekerja())

g01 = Guru('Barry', 'm', '102')
print(g01.bekerja())