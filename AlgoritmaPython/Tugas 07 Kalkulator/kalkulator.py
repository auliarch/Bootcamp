def menu_penjumlahan():
    """
    Fungsi menjumlahkan 2 bilangan

    Args:
        a (integer): bilangan pertama
        b (integer): bilangan kedua
        print : jumlah dari a dan b
    """
    while True:
        a = int(input("Masukkan bilangan pertama: "))
        b = int(input("Masukkan bilangan kedua: "))
        hasil = a + b
        print("Hasil Penjumlahan dari {} + {} = {}".format(a,b,hasil))
        selesai = input("Selesai (y/n)? ")
        if selesai == 'y':
            break

def menu_perkalian():
    """
    Fungsi perkalian 2 bilangan

    Args:
        a (integer): bilangan pertama
        b (integer): bilangan kedua
        print : perkalian dari a dan b
    """
    while True:
        a = int(input("Masukkan bilangan pertama: "))
        b = int(input("Masukkan bilangan kedua: "))
        hasil = a * b
        print("Hasil Perkalian dari bilangan {} x {} = {}".format(a,b,hasil))
        selesai = input("Selesai (y/n)? ")
        if selesai == 'y':
            break
        
def menu_konversi_suhu():
    """
    Fungsi konversi suhu celcius ke fahrenheit, kelvin dan reamur

    Args:
        a (float): suhu dalam celcius
        print : hasil konversi celcius ke fahrenheit, kelvin dan reamur
    """
    while True:
        celcius = float(input("Masukkan suhu dalam celcius : "))
        fahrenheit = (celcius * 9/5)+ 32
        kelvin = celcius + 273.15
        reamur = 4/5 * celcius
        print("Suhu dalam Fahrenheit adalah", fahrenheit)
        print("Suhu dalam Kelvin adalah", kelvin)
        print("Suhu dalam Reamur adalah", reamur)
        selesai = input("Selesai (y/n)? ")
        if selesai == 'y':
            break
        
def menu_luas_persegi():
    """
    Fungsi menghitung luas persegi

    Args:
        sisi (integer): panjang sisi persegi
        print : luas dari persegi
    """
    while True:
        sisi = int(input("Masukkan panjang sisi : "))
        hasil = sisi * sisi
        print("Luas Persegi : ", hasil)
        selesai = input("Selesai (y/n)? ")
        if selesai == 'y':
            break
        
def volume_kerucut():
    """
    Fungsi menghitung volume kerucut

    Args:
        r (integer): jari - jari
        t (integer): tinggi
        print : Volume Kerucut
    """
    while True:
        PI = 3.14
        r = int(input("Masukkan Jari - Jari : "))
        t = int(input("Masukkan Tinggi : "))
        volume = 1/3 * PI * r * r * t
        print("Volume Kerucut : ", volume)
        selesai = input("Selesai (y/n)? ")
        if selesai == 'y':
            break

def konversi_angka_ke_biner(): 
    """
    Fungsi konversi angka ke biner

    Args:
        a (integer): bilangan yang akan dikonversi
        print : bilangan biner dari angka yang diinputkan
    """
    while True:
        a = int(input("Masukkan Angka : "))
        biner = ""
        while a > 0 :
            sisa = a % 2
            biner = str(sisa) + biner
            a = a//2
        print("Bilangan biner : {}".format(biner))
        selesai = input("Selesai (y/n)? ")
        if selesai == 'y':
            break

def koversi_kg_g():
    """
    Fungsi Konversi Kilogram ke gram

    Args:
        a (integer): bilangan dalam kilogram
        print : bilangan dalam gram
    """
    while True:
        a = int(input("Masukkan (kg) : "))
        gram = a * 1000
        print("Konversi {} kg adalah {} gr".format(a, gram))
        selesai = input("Selesai (y/n)? ")
        if selesai == 'y':
            break

def faktorial():
    """
    Fungsi faktorial suatu bilangan

    Args:
        a (integer): bilangan yang akan di faktorial
        print : faktorial dari bilangan a
    """
    while True:
        a = int(input("Masukkan Angka : "))
        faktorial = 1
        for i in range(1, a+1) :
            faktorial *= i
        print("Faktorial dari {} : {}".format(a, faktorial))
        selesai = input("Selesai (y/n)? ")
        if selesai == 'y':
            break

def keliling_lingkaran():
    """
    Fungsi untuk menghitung keliling lingkaran.

    Args : 
        r (integer) : jari - jari
        print : keliling lingkaran
    """
    while True:
        r = int(input("Masukkan jari - jari : "))
        PI = 3.14
        hasil = 2 * PI * r
        print(f'Keliling lingkaran: {hasil}')
        selesai = input("Selesai (y/n)? ")
        if selesai== 'y':
            break

def keliling_persegi() :
    """
    Fungsi menghitung keliling persegi

    Args:
        sisi (integer): panjang sisi persegi
        print : keliling persegi
    """
    while True:
        sisi = int(input("Masukkan panjang sisi : "))
        hasil = 4 * sisi
        print("Keliling Persegi : ", hasil)
        selesai = input("Selesai (y/n)? ")
        if selesai == 'y':
            break
        
def keliling_persegi_panjang() :
    """
    Fungsi menghitung keliling persegi panjang

    Args:
        panjang (integer): panjang persegi panjang
        lebar (integer) : lebar persegi panjang
        print : keliling persegi panjang
    """
    while True:
        panjang = int(input("Masukkan panjang persegi panjang : "))
        lebar = int(input("Masukkan lebar persegi panjang : "))
        hasil = 2 * (panjang + lebar )
        print("Keliling Persegi Panjang : ", hasil)
        selesai = input("Selesai (y/n)? ")
        if selesai == 'y':
            break