def pengambilan_barang():
    lemari = list(map(str, input().split()))
    barang_diambil = str(input())
    if barang_diambil in lemari:
        lemari.remove(barang_diambil)
    return lemari

def main():
    hasil = pengambilan_barang()
    print(' '.join(hasil))

if __name__ == "__main__":
    main()