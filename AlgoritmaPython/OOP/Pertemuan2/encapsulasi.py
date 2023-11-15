# ENCAPSULASI
class Manusia:          # class parent

    def __init__(self, n, jk):
        self.__nama = n         # self.nama (public) | self._nama (protected) | self.__nama (private)
        self.__jk = jk

    def set_nama(self, n):      # setter
        if len(n) != 0:
            self.__nama = n
    
    def set_jk(self, jk):
        self.__jk = jk
    
    def get_nama(self):         # getter
        return self.__nama
    
    def get_jk(self):
        return self.__jk

    def bekerja(self):
        return f'{self.__nama} {self.__jk} bekerja'

# class Guru(Manusia):    # class anak

#     def __init__(self, n, jk, NIP):
#         Manusia.__init__(self, n, jk)
#         self.NIP = NIP

#     def bekerja(self):  # masuk ke polymorphism
#         return f'{self.nama} {self.NIP} mengajar'

# m01 = Manusia('Alex', 'm')    # cara pertama
# m01.__nama = 'Blek'
# m01.__jk = 'f'
# print(m01.bekerja())

m01 = Manusia('Alex', 'm')    # cara kedua (setter|getter)
m01.set_nama("Leni")
m01.set_jk("f")
print(m01.bekerja())
print(m01.get_nama())

# g01 = Guru('Barry', 'm', '102')
# print(g01.bekerja())