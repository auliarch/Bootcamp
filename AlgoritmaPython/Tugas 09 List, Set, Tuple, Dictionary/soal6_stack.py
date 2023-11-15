def tambah_barang(lemari, barang):
    lemari.append(barang)

def ambil_barang(lemari):
    if lemari:
        lemari.pop()

def cetak_isi_lemari(lemari):
    print("Cetak isi lemari:", " ".join(lemari))

def main():
    lemari = []
    for _ in range(3):
        barang = input("Masukkan barang: ")
        tambah_barang(lemari, barang)

    cetak_isi_lemari(lemari)
    print("Ambil barang.")
    ambil_barang(lemari)
    cetak_isi_lemari(lemari)

    barang = input("Masukkan barang: ")
    tambah_barang(lemari, barang)

    cetak_isi_lemari(lemari)

if __name__ == "__main__":
    main()