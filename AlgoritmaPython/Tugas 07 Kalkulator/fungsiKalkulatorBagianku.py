def menu_utama():
    print("---------------------------------")
    print("KALKULATOR SEDERHANA")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Luas Lingkaran")
    print("6. Keliling Lingkaran")
    print("7. Luas Persegi")
    print("8. Keliling Persegi")
    print("9. Luas Segitiga")
    print("10. Keliling Segitiga")
    print("11. Luas Persegi Panjang")
    print("12. Keliling Persegi Panjang")
    print("13. Volume Kerucut")
    print("14. Volume Tabung")
    print("15. Konversi Suhu")
    print("16. Konversi Angka ke Biner")
    print("17. Konversi Jarak Km ke M")
    print("18. Konversi Kg ke Gram")
    print("19. Deret Bilangan Prima")
    print("20. Faktorial")
    print("21. Exit")
    print("---------------------------------")
    print("Pilihan Anda (1-21): ", end = " ")

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

def pengurangan():
    """
    Fungsi untuk menghitung pengurangan dari 2 bilangan.

    Parameters:
    a (integer) : bilangan pertama
    b (integer) : bilangan kedua

    Output:
    Hasil bilangan pertama - bilangan kedua adalah: hasil
    """
    while True:
        a = int(input("Masukkan bilangan pertama: "))
        b = int(input("Masukkan bilangan kedua: "))
        hasil = a - b
        print(f'Hasil {a} - {b} adalah: {hasil}')
        selesai = input("Selesai (y/n)? ")
        if selesai== 'y':
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

def pembagian():
    """
    Fungsi untuk menghitung pembagian dari 2 bilangan.

    Parameters:
    a (integer) : bilangan pertama
    b (integer) : bilangan kedua

    Output:
    Hasil bilangan pertama / bilangan kedua adalah: hasil
    """
    while True:
        a = int(input("Masukkan bilangan pertama: "))
        b = int(input("Masukkan bilangan kedua: "))
        hasil = a / b
        print(f'Hasil {a} / {b} adalah: {hasil}')
        selesai = input("Selesai (y/n)? ")
        if selesai== 'y':
            break

def luas_lingkaran():
    """
    Fungsi untuk menghitung luas lingkaran.

    Parameters:
    r (integer) : jari-jari

    Output:
    Luas lingkaran: hasil
    """
    while True:
        r = int(input("Masukkan jari-jari: "))
        PI = 3.14
        hasil = PI * r * r
        print(f'Luas lingkaran: {hasil}')
        selesai = input("Selesai (y/n)? ")
        if selesai== 'y':
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

def luas_segitiga():
    """
    Fungsi untuk menghitung luas segitiga.

    Parameters:
    a (integer) : alas
    t (integer) : tinggi

    Output:
    Luas segitiga: hasil
    """
    while True:
        a = int(input("Masukkan alas: "))
        t = int(input("Masukkan tinggi: "))
        hasil = 0.5 * a * t
        print(f'Luas segitiga: {hasil}')
        selesai = input("Selesai (y/n)? ")
        if selesai== 'y':
            break

def keliling_segitiga():
    """
    Fungsi untuk menghitung keliling segitiga.

    Parameters:
    sisi1 (integer) : sisi ke-1
    sisi2 (integer) : sisi ke-2
    sisi3 (integer) : sisi ke-3

    Output:
    Keliling segitiga: hasil
    """
    while True:
        sisi1 = int(input("Masukkan sisi ke-1: "))
        sisi2 = int(input("Masukkan sisi ke-2: "))
        sisi3 = int(input("Masukkan sisi ke-3: "))
        hasil = sisi1 + sisi2 + sisi3
        print(f'Keliling segitiga: {hasil}')
        selesai = input("Selesai (y/n)? ")
        if selesai== 'y':
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

def luas_persegi_panjang():
    """
    Fungsi untuk menghitung luas persegi panjang.

    Parameters:
    p (integer) : panjang sisi
    l (integer) : lebar sisi

    Output:
    Luas persegi panjang: hasil
    """
    while True:
        p = int(input("Masukkan panjang: "))
        l = int(input("Masukkan lebar: "))
        hasil = p * l
        print(f'Luas persegi panjang: {hasil}')
        selesai = input("Selesai (y/n)? ")
        if selesai== 'y':
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

def volume_tabung():
    """
    Fungsi untuk menghitung volume tabung.

    Parameters:
    r (integer) : jari-jari
    t (integer) : tinggi

    Output:
    Volume tabung: hasil
    """
    while True:
        r = int(input("Masukkan jari-jari: "))
        t = int(input("Masukkan tinggi: "))
        PI = 3.14
        hasil = PI * r * r * t
        print(f'Volume tabung: {hasil}')
        selesai = input("Selesai (y/n)? ")
        if selesai== 'y':
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

def konversi_km_m():
    """
    Fungsi untuk mengkonversi km ke m.

    Parameters:
    a (integer) : Bilangan yang akan dikonversi

    Output:
    Hasil konversi: hasil
    """
    while True:
        a = int(input("Masukkan angka: "))
        hasil = a * 1000
        print(f'Hasil konversi: {hasil}m')
        selesai = input("Selesai (y/n)? ")
        if selesai== 'y':
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

def deret_bil_prima():
    """
    Fungsi untuk menampilkan deret bilangan prima.

    Parameters:
    a (integer) : bilangan pertama
    b (integer) : bilangan kedua

    Output:
    Deret bilangan prima: hasil
    """
    while True:
        a = int(input("Masukkan bilangan pertama: "))
        b = int(input("Masukkan bilangan terakhir: "))
    
        deret = []

        for i in range(a, b+1):
            if i > 1:
                is_prima = True
                for j in range(2, int(i ** 0.5)+1):
                    if i % j == 0:
                        is_prima = False
                        break

                if is_prima:
                    deret.append(i)

        print(f'Deret bilangan prima: {deret}')

        selesai = input("Selesai (y/n)? ")
        if selesai== 'y':
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

def main():
    while True:
        menu_utama()
        pilihan = int(input())
        match pilihan:
            case 1: menu_penjumlahan()
            case 2: pengurangan()
            case 3: menu_perkalian()
            case 4: pembagian()
            case 5: luas_lingkaran()
            case 6: keliling_lingkaran()
            case 7: menu_luas_persegi()
            case 8: keliling_persegi()
            case 9: luas_segitiga()
            case 10: keliling_segitiga()
            case 11: luas_persegi_panjang()
            case 12: keliling_persegi_panjang()
            case 13: volume_kerucut()
            case 14: volume_tabung()
            case 15: menu_konversi_suhu()
            case 16: konversi_angka_ke_biner()
            case 17: konversi_km_m()
            case 18: koversi_kg_g()
            case 19: deret_bil_prima()
            case 20: faktorial()
            case 21: print("bye")
            case _: print("Ulang lagi")
        if pilihan == 21:
            break

if __name__ == "__main__":
    main()