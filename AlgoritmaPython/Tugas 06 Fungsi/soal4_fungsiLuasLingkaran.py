#pendefinisian fungsi luas_lingkaran
def luas_lingkaran(angka):
    return 3.14 * angka ** 2

#pendefinisian program utama
def main():
    #input dan casting
    bil = float(input())

    #pemanggilan fungsi
    hasil = luas_lingkaran(bil)

    #pencetakan hasil luas_lingkaran
    print(round(hasil, 2))

#pemanggilan program utama
if __name__ == '__main__':
    main()