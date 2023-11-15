#pendefinisian fungsi penjumlahan
def penjumlahan(a, b):
    return a + b

#pendefinisian program utama
def main():
    #input dan casting
    bil1 = int(input())
    bil2 = int(input())

    #pemanggilan fungsi
    hasil_penjumlahan = penjumlahan(bil1, bil2)

    #pencetakan hasil penjumlahan
    print(hasil_penjumlahan)

#pemanggilan program utama
if __name__ == '__main__':
    main()