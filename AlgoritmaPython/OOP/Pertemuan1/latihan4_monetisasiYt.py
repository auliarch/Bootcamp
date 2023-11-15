class Monetisasi:
    def __init__(self, jp, wt):
        self.jumlah_penonton = jp
        self.waktu_tontonan = wt

    def hasil(self):
        if self.jumlah_penonton >= 1000 and self.waktu_tontonan >= 4000:
            return "sudah dapat dimonetisasi"
        else:
            return "belum dapat dimonetisasi"
        
monetisasi01 = Monetisasi(1000, 4000)
monetisasi02 = Monetisasi(1000, 3000)
monetisasi03 = Monetisasi(999, 2000)

assert monetisasi01.hasil() == "sudah dapat dimonetisasi"
assert monetisasi02.hasil() == "belum dapat dimonetisasi"
assert monetisasi03.hasil() == "belum dapat dimonetisasi"