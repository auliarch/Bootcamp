class Cuaca:
    def __init__(self, s):
        self.status = s

class Mahasiswa:
    def __init__(self, fs, bc, s):
        self.fisik = fs
        self.bekal = bc
        self.status = Cuaca(s) # Pembuatan objek dalam sebuah kelas
    def berkemah(self):
        if self.fisik and self.bekal and self.status :
            return f'berkemah'
        else:
            return f'tidak berkemah'
        
mhs01 = Mahasiswa(True, True, True)
print(mhs01.berkemah())

mhs02 = Mahasiswa(False, True, True)
print(mhs02.berkemah())

mhs03 = Mahasiswa(True, False, True)
print(mhs03.berkemah())