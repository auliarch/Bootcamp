# class Apel:

#     def __init__(self, jumlah):
#         self.jumlah = jumlah

# class Manusia:

#     def __init__(self, joko, icha, ratna):
#         self.apel_joko = Apel(joko)
#         self.apel_icha = Apel(icha)
#         self.apel_ratna = Apel(ratna)

#     def hitung_jumlah_apel(self):
#         return self.apel_joko.jumlah + self.apel_icha.jumlah + self.apel_ratna.jumlah

# hasil = Manusia(3, 5, 6)
# print(hasil.hitung_jumlah_apel())


# Coding Bapa Contoh 1
# class Apel:
#     def __init__(self, jumlah):
#         self.jumlah = jumlah

# class Manusia:
#     def __init__(self, nama, banyak_apel):
#         self.nama = nama
#         apel = Apel(banyak_apel)
#         self.banyak_apel = apel.jumlah

# orang01 = Manusia("Joko", 3)
# orang02 = Manusia("Icha", 5)
# orang03 = Manusia("Ratna", 6)

# print(orang01.banyak_apel + orang02.banyak_apel + orang03.banyak_apel)

# Contoh 2
class Apel:
    def __init__(self, jumlah):
        self.jumlah = jumlah

class Manusia:
    jumlah_apel = 0
    def __init__(self, nama, banyak_apel):
        self.nama = nama
        apel = Apel(banyak_apel)
        self.banyak_apel = apel.jumlah
        Manusia.jumlah_apel += self.banyak_apel

orang01 = Manusia("Joko", 3)
orang02 = Manusia("Icha", 5)
orang03 = Manusia("Ratna", 6)

print(Manusia.jumlah_apel)