#pendefinisian fungsi keliling_lingkaran
def keliling_lingkaran(angka):
    return 2 * 3.14 * angka

#pendefinisian program utama
def main():
    #input dan casting
    bil = float(input())

    #pemanggilan fungsi
    hasil = keliling_lingkaran(bil)

    #pencetakan hasil keliling_lingkaran
    print(round(hasil, 2))

#pemanggilan program utama
if __name__ == '__main__':
    main()