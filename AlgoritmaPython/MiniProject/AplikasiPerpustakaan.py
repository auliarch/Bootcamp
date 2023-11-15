import datetime

def baca_data_buku():
    """
    Fungsi untuk membaca data buku.

    Parameters:
    data_buku = list() untuk menyimpan list
    """
    with open('E:\\BOOTCAMP\\AlgoritmaPython\\MiniProject\\dataBuku.txt') as f:
        data_buku = list()
        for line in f:
            kode_buku, judul, penulis, tahun_terbit, qty, crd, upd = line.split('|')
            data_buku.append([kode_buku, judul, penulis, int(tahun_terbit), int(qty), crd, upd])
        return data_buku

def baca_data_member():
    """
    Fungsi untuk membaca data member.

    Parameters:
    data_member = list() untuk menyimpan list
    """
    with open('E:\\BOOTCAMP\\AlgoritmaPython\\MiniProject\\dataMember.txt') as f:
        data_member = list()
        for line in f:
            kode_member, nama, usia, alamat, kota, crd, upd = line.split('|')
            data_member.append([kode_member, nama, usia, alamat, kota, crd, upd])
        return data_member

def baca_data_peminjaman():
    """
    Fungsi untuk membaca data peminjaman.

    Parameters:
    data_pinjam = list() untuk menyimpan list
    """
    with open('E:\\BOOTCAMP\\AlgoritmaPython\\MiniProject\\dataPeminjaman.txt') as f:
        data_pinjam = list()
        for line in f:
            kode_pinjam, kode_buku, kode_member, nama, usia, qty, tgl_pinjam, tgl_kembali, status, biaya = line.split('|')
            data_pinjam.append([kode_pinjam, kode_buku, kode_member, nama, usia, int(qty), tgl_pinjam, tgl_kembali, status, int(biaya)])
        return data_pinjam

def tulis_data_buku(data_buku):
    """
    Fungsi untuk menulis data buku ke dalam file teks.

    Parameters:
    data_buku = list() : Data buku yang akan ditulis ke dalam file.
    """
    with open('E:\\BOOTCAMP\\AlgoritmaPython\\MiniProject\\dataBuku.txt', 'w') as f:
        for item in data_buku:
            f.write('|'.join(str(i).strip() for i in item) + '\n')

def tulis_data_member(data_member):
    """
    Fungsi untuk menulis data member ke dalam file teks.

    Parameters:
    data_member = list() : Data member yang akan ditulis ke dalam file.
    """
    with open('E:\\BOOTCAMP\\AlgoritmaPython\\MiniProject\\dataMember.txt', 'w') as f:
        for item in data_member:
            f.write('|'.join(str(i).strip() for i in item) + '\n')

def tulis_data_peminjaman(data_pinjam):
    """
    Fungsi untuk menulis data peminjaman ke dalam file teks.

    Parameters:
    data_pinjam = list() : Data peminjaman yang akan ditulis ke dalam file.
    """
    with open('E:\\BOOTCAMP\\AlgoritmaPython\\MiniProject\\dataPeminjaman.txt', 'w') as f:
        for item in data_pinjam:
            f.write('|'.join(str(i).strip() for i in item) + '\n')

def menu_aksi():
    """
    Fungsi untuk menampilkan menu aksi aplikasi perpustakaan.
    """
    print("------------------------------------------------------------------------------------------------------------------------------------")
    print("|                                                              MENU AKSI                                                           |")
    print("------------------------------------------------------------------------------------------------------------------------------------")
    print("|  1  | Tampil Data Buku                                                                                                           |")
    print("|  2  | Tambah Data Buku                                                                                                           |")
    print("|  3  | Ubah Data Buku                                                                                                             |")
    print("|  4  | Hapus Data Buku                                                                                                            |")
    print("|  5  | Tampil Data Member                                                                                                         |")
    print("|  6  | Tambah Data Member                                                                                                         |")
    print("|  7  | Ubah Data Member                                                                                                           |")
    print("|  8  | Hapus Data Member                                                                                                          |")
    print("|  9  | Tampil Data Peminjaman Buku                                                                                                |")
    print("| 10  | Tambah Data Peminjaman Buku                                                                                                |")
    print("| 11  | Ubah Data Peminjaman Buku                                                                                                  |")
    print("| 12  | Hapus Data Peminjaman Buku                                                                                                 |")
    print("| 13  | Cari Buku                                                                                                                  |")
    print("| 14  | Pengembalian Buku                                                                                                          |")
    print("| 15  | Keluar                                                                                                                     |")
    print("------------------------------------------------------------------------------------------------------------------------------------")
    print("Masukkan pilihan Anda (1 - 15):", end=" ")

def cetak_tabel_buku(data_buku):
    """
    Fungsi untuk menampilkan daftar buku dalam bentuk tabel.

    Parameters:
    data_buku (list) : Data buku yang akan ditampilkan.
    """
    while True:
        print("------------------------------------------------------------------------------------------------------------------------------------")
        print("|                                                           DAFTAR BUKU                                                            |")
        print("------------------------------------------------------------------------------------------------------------------------------------")
        print("| Kode Buku |          Judul          |          Penulis          | Tahun Terbit | Qty |    Created Date     |     Updated Date    |")
        print("------------------------------------------------------------------------------------------------------------------------------------")

        for data in data_buku:
            kode_buku, judul, penulis, tahun_terbit, qty, crd, upd = data
            print("|{:^11}| {:<23} | {:<25} |{:^14}|{:^5}|{:^21}|{:^21}|".format(
                kode_buku, judul, penulis, tahun_terbit, qty, crd, upd[:19]))
        print("------------------------------------------------------------------------------------------------------------------------------------")

        urutkan_buku = input("Urutkan buku? (y/n): ")
        if urutkan_buku.lower() == 'y':
            print("Pilih Kategori:")
            print("1. Kode Buku / 2. Judul / 3. Penulis / 4. Tahun Terbit")
            kategori = input("Masukkan pilihan (1-4): ")
            data_buku_terurut(data_buku, kategori)

            ulang = input("Kembali ke menu aksi? (y/n): ")
            if ulang.lower() == 'y':
                break
        break

def data_buku_terurut(data_buku, kategori):
    """
    Fungsi untuk mengurutkan data buku berdasarkan kategori tertentu.

    Parameters:
    data_buku (list) : Data buku yang akan diurutkan.
    kategori (str) : Pilihan kategori berdasarkan buku yang akan diurutkan.
    """
    if kategori == '1':
        urutan = lambda buku: buku[0]
    elif kategori == '2':
        urutan = lambda buku: buku[1]
    elif kategori == '3':
        urutan = lambda buku: buku[2]
    elif kategori == '4':
        urutan = lambda buku: buku[3]
    else:
        print("Pilihan tidak valid")
        return
    
    data_buku.sort(key=urutan)
    cetak_tabel_buku(data_buku)

def buku_terfavorit(data_pinjam, data_buku):
    """
    Fungsi untuk menampilkan 5 buku terfavorit berdasarkan jumlah peminjaman.

    Parameters:
    data_pinjam (list) : Data peminjaman buku.
    data_buku (list) : Data buku.
    """
    data_peminjaman_buku = dict()

    for pinjam in data_pinjam:
        kode_buku = pinjam[1]
        if kode_buku in data_peminjaman_buku:
            data_peminjaman_buku[kode_buku] += 1
        else:
            data_peminjaman_buku[kode_buku] = 1

    terfavorit = sorted(data_peminjaman_buku.items(), key=lambda x: x[1], reverse=True)[:5]

    print("------------------------------------------------------------------------------------------------------------------------------------")
    print("|                                                          5 BUKU TERFAVORIT                                                       |")
    print("------------------------------------------------------------------------------------------------------------------------------------")
    print("| Kode Buku |                  Judul                  |                  Penulis                  | Tahun Terbit | Jumlah Peminjam |")
    print("------------------------------------------------------------------------------------------------------------------------------------")
    for kode_buku, jumlah_pinjam in terfavorit:
        buku = next((i for i in data_buku if i[0] == kode_buku), None)
        if buku:
            kode_buku, judul, penulis, tahun_terbit, qty, crd, upd = buku
            print("|{:^11}| {:<39} | {:<41} |{:^14}|{:^17}|".format(kode_buku, judul, penulis, tahun_terbit, jumlah_pinjam))
    print("------------------------------------------------------------------------------------------------------------------------------------")

def cetak_tabel_member(data_member):
    """
    Fungsi untuk menampilkan daftar member dalam bentuk tabel.

    Parameters:
    data_member (list) : Data member yang akan ditampilkan.
    """
    while True:
        print("------------------------------------------------------------------------------------------------------------------------------------")
        print("|                                                          DAFTAR MEMBER                                                           |")
        print("------------------------------------------------------------------------------------------------------------------------------------")
        print("| Kode Member |           Nama           | Usia |        Alamat        |      Kota     |    Created Date     |     Updated Date    |")
        print("------------------------------------------------------------------------------------------------------------------------------------")

        for data in data_member:
            kode_member, nama, usia, alamat, kota, crd, upd = data
            print("|{:^13}| {:<24} |{:^6}| {:^20} | {:^13} |{:^21}|{:^21}|".format(
                kode_member, nama, usia, alamat, kota, crd, upd[:19]))
        print("------------------------------------------------------------------------------------------------------------------------------------")

        ulang = input("Pilih aksi lagi? (y): ")
        if ulang.lower() == 'y':
            break
        break

def cetak_tabel_peminjaman(data_pinjam, data_buku):
    """
    Fungsi untuk menampilkan daftar peminjaman buku dalam bentuk tabel.

    Parameters:
    data_pinjam (list) : Data peminjaman buku.
    data_buku (list) : Data buku.
    """
    while True:
        print("------------------------------------------------------------------------------------------------------------------------------------")
        print("|                                                        DAFTAR PEMINJAMAN                                                         |")
        print("------------------------------------------------------------------------------------------------------------------------------------")
        print("| Kode P | Kode BK |  Kode M  |           Nama           | Usia | Jumlah |  Tanggal Pinjam  | Tanggal Kembali |  Status  |  Biaya  |")
        print("------------------------------------------------------------------------------------------------------------------------------------")

        for data in data_pinjam:
            kode_pinjam, kode_buku, kode_member, nama, usia, qty, tgl_pinjam, tgl_kembali, status, biaya = data
            print("|{:^8}|{:^9}|{:^10}| {:<24} |{:^6}|{:^8}|{:^18}|{:^17}|{:^10}|{:^9}|".format(
                kode_pinjam, kode_buku, kode_member, nama, usia, qty, tgl_pinjam, tgl_kembali, status, biaya))
        print("------------------------------------------------------------------------------------------------------------------------------------")

        print("Pilih Aksi:")
        print("1. Tampil Data Buku / 2. 5 Buku Terfavorit / 3. Kembali ke menu")
        pilihan = input("Masukkan pilihan (1-3): ")
        if pilihan == '1':
            print("------------------------------------------------------------------------------------------------------------------------------------")
            print("|                                                           DAFTAR BUKU                                                            |")
            print("------------------------------------------------------------------------------------------------------------------------------------")
            print("| Kode Buku |          Judul          |          Penulis          | Tahun Terbit | Qty |    Created Date     |     Updated Date    |")
            print("------------------------------------------------------------------------------------------------------------------------------------")

            for data in data_buku:
                kode_buku, judul, penulis, tahun_terbit, qty, crd, upd = data
                print("|{:^11}| {:<23} | {:<25} |{:^14}|{:^5}|{:^21}|{:^21}|".format(
                    kode_buku, judul, penulis, tahun_terbit, qty, crd, upd[:19]))
            print("------------------------------------------------------------------------------------------------------------------------------------")
        elif pilihan == '2':
            buku_terfavorit(data_pinjam, data_buku)
        elif pilihan == '3':
            break
        else:
            print("Pilihan tidak valid")
            return
        
        ulang = input("Pilih aksi lagi? (y/n): ")
        if ulang.lower() != 'y':
            break
    
def validasi_kode_buku(data_buku, kode_buku):
    """
    Fungsi untuk memvalidasi kode buku apakah kosong dan sudah ada dalam data buku atau tidak.

    Parameters:
    data_buku (list) : Data buku yang ada.
    kode_buku (str) : Kode buku yang akan divalidasi.
    """
    while kode_buku == "" or kode_buku in [data[0] for data in data_buku]:
        if kode_buku == "":
            print("Isi kode buku")
        else:
            print("Kode tersedia. Masukkan kode lain")
        kode_buku = input("Masukkan Kode Buku: ")
        
    return kode_buku

def validasi_kode_member(data_member, kode_member):
    """
    Fungsi untuk memvalidasi kode member apakah kosong atau sudah ada dalam data member atau tidak.

    Parameters:
    data_member (list) : Data member yang ada.
    kode_member (str) : Kode member yang akan divalidasi.
    """
    while kode_member == "" or kode_member in [data[0] for data in data_member]:
        if kode_member == "":
            print("Isi kode member")
        else:
            print("Kode tersedia. Masukkan kode lain")
        kode_member = input("Masukkan Kode Member: ")
    return kode_member

def validasi_kode_pinjam(data_pinjam, kode_pinjam):
    """
    Fungsi untuk memvalidasi kode peminjaman apakah kosong atau sudah ada dalam data peminjaman atau tidak.

    Parameters:
    data_pinjam (list) : Data peminjaman yang ada.
    kode_pinjam (str) : Kode peminjaman yang akan divalidasi.
    """
    while kode_pinjam == "" or kode_pinjam in [data[0] for data in data_pinjam]:
        if kode_pinjam == "":
            print("Isi kode peminjaman")
        else:
            print("Kode tersedia. Masukkan kode lain")
        kode_pinjam = input("Masukkan Kode Peminjaman: ")
    return kode_pinjam

def validasi_nama(nama):
    """
    Fungsi untuk memvalidasi nama apakah telah diisi atau tidak.

    Parameters:
    nama (str) : Nama yang akan divalidasi.
    """
    while nama == "":
        print("Isi nama")
        nama = input("Masukkan Nama: ")
    return nama

def validasi_judul(judul):
    """
    Fungsi untuk memvalidasi judul apakah telah diisi atau tidak.

    Parameters:
    judul (str) : Judul yang akan divalidasi.
    """
    while judul == "":
        print("Isi judul")
        judul = input("Masukkan Judul Buku: ")
    return judul

def validasi_penulis(penulis):
    """
    Fungsi untuk memvalidasi penulis apakah telah diisi atau tidak.

    Parameters:
    penulis (str) : Penulis yang akan divalidasi.
    """
    while penulis == "":
        print("Isi penulis")
        penulis = input("Masukkan Penulis: ")
    return penulis

def validasi_tahun_terbit(tahun_terbit):
    """
    Fungsi untuk memvalidasi tahun terbit apakah telah diisi dan berupa angka atau bukan.

    Parameters:
    tahun_terbit (str) : Tahun terbit buku yang akan divalidasi.
    """
    while tahun_terbit == "" or not tahun_terbit.isdigit():
        if tahun_terbit == "":
            print("Isi tahun terbit")
        else:
            print("Tahun terbit harus berupa angka")
        tahun_terbit = input("Masukkan Tahun Terbit: ")
    return tahun_terbit

def validasi_qty(qty):
    """
    Fungsi untuk memvalidasi qty apakah telah diisi dan berupa angka atau bukan.

    Parameters:
    qty (str) : Jumlah buku yang akan divalidasi.
    """
    while qty == "" or not qty.isdigit():
        if qty == "":
            print("Isi jumlah")
        else:
            print("Jumlah harus berupa angka")
        qty = input("Masukkan Jumlah Buku: ")
    return int(qty)

def validasi_usia(usia):
    """
    Fungsi untuk memvalidasi usia apakah telah diisi dan berupa angka atau bukan.

    Parameters:
    usia (str) : Usia yang akan divalidasi.
    """
    while usia == "" or not usia.isdigit():
        if usia == "":
            print("Isi usia")
        else:
            print("Usia harus berupa angka")
        usia = input("Masukkan Usia: ")
    return usia

def validasi_alamat(alamat):
    """
    Fungsi untuk memvalidasi alamat apakah telah diisi atau tidak.

    Parameters:
    alamat (str) : Alamat yang akan divalidasi.
    """
    while alamat == "":
        print("Isi alamat")
        alamat = input("Masukkan Alamat: ")
    return alamat

def validasi_kota(kota):
    """
    Fungsi untuk memvalidasi kota apakah telah diisi atau tidak.

    Parameters:
    kota (str) : Kota yang akan divalidasi.
    """
    while kota == "":
        print("Isi alamat")
        kota = input("Masukkan Kota: ")
    return kota

def tambah_data_buku(data_buku):
    """
    Fungsi untuk menambah data buku ke dalam daftar buku.

    Parameters:
    data_buku (list) : Daftar data buku yang ada.
    """
    while True:
        kode_buku = input("Masukkan Kode Buku: ")
        kode_buku = validasi_kode_buku(data_buku, kode_buku)
        if ")" in kode_buku:
            print("Dibatalkan")
            break

        judul = validasi_judul(input("Masukkan Judul Buku: "))
        if ")" in judul:
            print("Dibatalkan")
            break

        penulis = validasi_penulis(input("Masukkan Penulis: "))
        if ")" in penulis:
            print("Dibatalkan")
            break

        tahun_terbit = validasi_tahun_terbit(input("Masukkan Tahun Terbit: "))
        if ")" in tahun_terbit:
            print("Dibatalkan")
            break

        qty = validasi_qty(input("Masukkan Jumlah Buku: "))

        crd = datetime.datetime.now().strftime("%Y-%m-%d/%H:%M:%S")
        upd = datetime.datetime.now().strftime("%Y-%m-%d/%H:%M:%S")

        data_buku.append([kode_buku, judul, penulis, int(tahun_terbit), int(qty), crd, upd])
        tulis_data_buku(data_buku)

        print("Berhasil ditambah")

        ulang = input("Lakukan penambahan lagi? (y/n): ")
        if ulang.lower() != 'y':
            break

        return data_buku

def tambah_data_member(data_member):
    """
    Fungsi untuk menambah data member ke dalam daftar member.

    Parameters:
    data_member (list) : Daftar data member yang ada.
    """
    while True:
        kode_member = input("Masukkan Kode Member: ")
        kode_member = validasi_kode_member(data_member, kode_member)
        if ")" in kode_member:
            print("Dibatalkan")
            break

        nama = validasi_nama(input("Masukkan Nama Member: "))
        if ")" in nama:
            print("Dibatalkan")
            break

        usia = validasi_usia(input("Masukkan Usia Member: "))
        if ")" in usia:
            print("Dibatalkan")
            break

        alamat = validasi_alamat(input("Masukkan Alamat: "))
        if ")" in alamat:
            print("Dibatalkan")
            break

        kota = validasi_kota(input("Masukkan Kota: "))
        if ")" in kota:
            print("Dibatalkan")
            break

        crd = datetime.datetime.now().strftime("%Y-%m-%d/%H:%M:%S")
        upd = datetime.datetime.now().strftime("%Y-%m-%d/%H:%M:%S")

        data_member.append([kode_member, nama, usia, alamat, kota, crd, upd])
        tulis_data_member(data_member)

        print("Berhasil ditambah")

        ulang = input("Lakukan penambahan lagi? (y/n): ")
        if ulang.lower() == 'y':
            continue
        else:
            break

    return data_member

def tambah_data_peminjam(data_pinjam, data_buku, data_member):
    """
    Fungsi untuk menambah data peminjaman ke dalam daftar peminjaman.

    Parameters:
    data_pinjam (list) : Daftar data peminjam yang ada.
    data_buku (list) : Daftar data buku yang ada.
    data_member (list) : Daftar data member yang ada.
    """
    while True:
        member = input("Apakah Anda member? (y/n): ")
        if ")" in member:
            print("Dibatalkan")
            break
        if member.lower() == 'y':
            kode_member = input("Masukkan Kode Member: ")
            if ")" in kode_member:
                print("Dibatalkan")
                break
            if kode_member == "":
                print("Isi kode")
                continue

            member_tersedia = False
            for member_data in data_member:
                if member_data[0] == kode_member:
                    member_tersedia = True
                    break

            if not member_tersedia:
                print("Kode member tidak tersedia")
                continue

            biaya = 0
            nama = member_data[1]
            usia = member_data[2]
        elif member.lower() == 'n':
            kode_member = 'non-member'
            biaya = 1000
            nama = validasi_nama(input("Masukkan Nama Peminjam: "))
            if ")" in nama:
                print("Dibatalkan")
                break
            usia = validasi_usia(input("Masukkan Usia Peminjam: "))
            if ")" in usia:
                print("Dibatalkan")
                break
        else:
            print("Pilihan tidak valid. Masukkan pilihan yang benar")
            continue

        kode_pinjam = input("Masukkan Kode Peminjam: ")
        kode_pinjam = validasi_kode_pinjam(data_pinjam, kode_pinjam)
        if ")" in kode_pinjam:
            print("Dibatalkan")
            break

        while True:
            kode_buku = input("Masukkan Kode Buku yang dipinjam: ")
            if kode_buku == "":
                print("Isi kode buku")
                continue
            if ")" in kode_buku:
                print("Dibatalkan")
                break

            buku = next((i for i in data_buku if i[0] == kode_buku), None)
            if buku is None:
                print("Buku  tidak ditemukan")
                continue
            
            while True:
                qty = validasi_qty(input("Masukkan Jumlah Buku: "))
                if buku[4] == 0:
                    print("Stok buku kosong")
                elif buku[4] < qty:
                    print("Jumlah buku yang tersedia tidak mencukupi")
                else:
                    break
            break

        index_buku = next((i for i, data in enumerate(data_buku) if data[0] == kode_buku), None)
        if index_buku is not None:
            data_buku[index_buku][4] -= qty
            tulis_data_buku(data_buku)
        else:
            print("Buku tidak ditemukan")

        tgl_pinjam = datetime.datetime.now().strftime("%Y-%m-%d")
        tgl_kembali = "-"
        status = "Dipinjam"
        biaya = 0

        data_pinjam.append([kode_pinjam, kode_buku, kode_member, nama, usia, int(qty), tgl_pinjam, tgl_kembali, status, int(biaya)])
        tulis_data_peminjaman(data_pinjam)

        print("Berhasil ditambah")

        ulang = input("Lakukan penambahan lagi? (y/n): ")
        if ulang.lower() == 'y':
            continue
        else:
            break

    return data_pinjam

def ubah_data_buku(data_buku):
    """
    Fungsi untuk mengubah data buku yang ada dalam daftar buku.

    Parameters:
    data_buku (list) : Daftar data buku yang ada.
    """
    while True:
        kode_buku = input("Masukkan kode buku yang akan diubah: ")
        if ")" in kode_buku:
            print("Dibatalkan")
            break
        elif kode_buku == "":
            print("Kode buku kosong. Silakan isi kode buku")
            continue

        index = None
        for i, data in enumerate(data_buku):
            if data[0] == kode_buku:
                index = i
                break
        
        if index is None:
            print("Kode buku tidak ditemukan")
            continue
        
        while True:
            print("Pilih data yang ingin diubah:")
            print("1. Judul / 2. Penulis / 3. Tahun Terbit / 4. Qty / 5. Kembali ke menu")

            pilihan = input("Masukkan pilihan (1-5): ")

            if pilihan == '1':
                judul_baru = validasi_judul(input("Masukkan judul baru: "))
                data_buku[index][1] = judul_baru
            elif pilihan == '2':
                penulis_baru = validasi_penulis(input("Masukkan penulis baru: "))
                data_buku[index][2] = penulis_baru
            elif pilihan == '3':
                tahun_terbit_baru = validasi_tahun_terbit(input("Masukkan tahun terbit baru: "))
                data_buku[index][3] = tahun_terbit_baru
            elif pilihan == '4':
                qty_baru = validasi_qty(input("Masukkan jumlah buku baru: "))
                data_buku[index][4] = qty_baru
            elif pilihan == '5':
                break
            else:
                print("Pilihan tidak valid")
                continue

            data_buku[index][6] = datetime.datetime.now().strftime("%Y-%m-%d/%H:%M:%S")

            tulis_data_buku(data_buku)

            print("Berhasil diubah")

            ulang = input("Lakukan perubahan lagi? (y/n): ")
            if ulang.lower() != 'y':
                break
        if ulang.lower() != 'y':
                break

def ubah_data_member(data_member):
    """
    Fungsi untuk mengubah data member yang ada dalam daftar member.

    Parameters:
    data_member (list) : Daftar data member yang ada.
    """
    while True:
        kode_member = input("Masukkan kode member yang akan diubah: ")
        if ")" in kode_member:
            print("Dibatalkan")
            break
        elif kode_member == "":
            print("Kode peminjaman kosong. Silakan isi kode kembali")
            continue

        index = None
        for i, data in enumerate(data_member):
            if data[0] == kode_member:
                index = i
                break

        if index is None:
            print("Kode member tidak ditemukan")
            continue

        while True:
            print("Pilih data yang ingin diubah:")
            print("1. Nama / 2. Usia / 3. Alamat / 4. Kota / 5. Kembali ke menu")

            pilihan = input("Masukkan pilihan (1-5): ")

            if pilihan == '1':
                nama_baru = validasi_nama(input("Masukkan nama baru: "))
                data_member[index][1] = nama_baru
            elif pilihan == '2':
                usia_baru = validasi_usia(input("Masukkan usia baru: "))
                data_member[index][2] = usia_baru
            elif pilihan == '3':
                alamat_baru = validasi_alamat(input("Masukkan alamat baru: "))
                data_member[index][3] = alamat_baru
            elif pilihan == '4':
                kota_baru = validasi_kota(input("Masukkan kota baru: "))
                data_member[index][4] = kota_baru
            elif pilihan == '5':
                break
            else:
                print("Pilihan tidak valid")

            data_member[index][6] = datetime.datetime.now().strftime("%Y-%m-%d/%H:%M:%S")

            tulis_data_member(data_member)

            print("Berhasil diubah")

            ulang = input("Lakukan perubahan lagi? (y/n): ")
            if ulang.lower() != 'y':
                break
        if ulang.lower() != 'y':
                break

def ubah_data_peminjaman(data_pinjam):
    """
    Fungsi untuk mengubah data peminjaman yang ada dalam daftar peminjaman.

    Parameters:
    data_pinjam (list) : Daftar data peminjaman yang ada.
    """
    while True:
        kode_pinjam = input("Masukkan kode peminjaman yang akan diubah: ")
        if ")" in kode_pinjam:
            print("Dibatalkan")
            break
        elif kode_pinjam == "":
            print("Kode peminjaman kosong. Silakan isi kode kembali")
            continue

        index = None
        for i, data in enumerate(data_pinjam):
            if data[0] == kode_pinjam:
                index = i
                break
        
        if index is None:
            print("Kode peminjam tidak ditemukan")
            continue
        
        while True:
            print("Pilih data yang ingin diubah:")
            print("1. Nama / 2. Usia / 3. Qty / 4. Kembali ke menu")

            pilihan = input("Masukkan pilihan (1-4): ")

            if pilihan == '1':
                nama_baru = validasi_judul(input("Masukkan nama baru: "))
                data_pinjam[index][3] = nama_baru
            elif pilihan == '2':
                usia_baru = validasi_penulis(input("Masukkan usia baru: "))
                data_pinjam[index][4] = usia_baru
            elif pilihan == '3':
                qty_baru = validasi_qty(input("Masukkan jumlah buku baru: "))
                data_pinjam[index][5] = qty_baru
            elif pilihan == '4':
                break
            else:
                print("Pilihan tidak valid")

            data_pinjam[index][7] = datetime.datetime.now().strftime("%Y-%m-%d")

            tulis_data_buku(data_pinjam)

            print("Berhasil diubah")

            ulang = input("Lakukan perubahan lagi? (y/n): ")
            if ulang.lower() != 'y':
                break
        if ulang.lower() != 'y':
                break

def hapus_data_buku(data_buku, data_pinjam):
    """
    Fungsi untuk menghapus data buku dari daftar buku. Jika buku sedang dipinjam, 
    data peminjam terkait akan dihapus terlebih dahulu.

    Parameters:
    data_buku (list) : Daftar data buku yang ada.
    data_pinjam (list) : Daftar data peminjaman yang ada.
    """
    while True:
        kode_buku = input("Masukkan kode buku yang akan dihapus: ")
        if ")" in kode_buku:
            print("Dibatalkan")
            break
        elif kode_buku == "":
            print("Kode buku kosong. Silakan isi kode buku")
            continue

        index = None
        for i, data in enumerate(data_buku):
            if data[0] == kode_buku:
                index = i
                break

        if index is None:
            print("Kode buku tidak ditemukan")
            continue

        data_peminjaman = [data for data in data_pinjam if data[1] == kode_buku]

        if data_peminjaman:
            print("Buku ini sedang dipinjam. Data peminjaman akan dihapus lebih dulu")
            for peminjam in data_peminjaman:
                data_pinjam.remove(peminjam)
            print("Data peminjaman terkait telah dihapus")
            tulis_data_peminjaman(data_pinjam)

        konfirmasi = input("Yakin akan dihapus? (y/n): ")

        if konfirmasi.lower() == 'y':
            del data_buku[index]
            tulis_data_buku(data_buku)
            print("Data buku telah dihapus")
        else:
            print("Penghapusan data dibatalkan")

        ulang = input("Lakukan penghapusan lagi? (y/n): ")
        if ulang.lower() != 'y':
            break

def hapus_data_member(data_member, data_pinjam, data_buku):
    """
    Fungsi untuk menghapus data member dari daftar member. Jika member memiliki peminjaman buku, 
    data peminjaman terkait juga akan dihapus.

    Parameters:
    data_member (list) : Daftar data member yang ada.
    data_pinjam (list) : Daftar data peminjaman yang ada.
    data_buku (list) : Daftar data buku yang ada.
    """
    while True:
        kode_member = input("Masukkan kode member yang akan dihapus: ")
        if ")" in kode_member:
            print("Dibatalkan")
            break
        elif kode_member == "":
            print("Kode kosong. Silakan isi kode member")
            continue

        index_member = None
        for i, data in enumerate(data_member):
            if data[0] == kode_member:
                index_member = i
                break

        if index_member is None:
            print("Kode member tidak ditemukan")
            continue

        data_peminjaman_member = [data for data in data_pinjam if data[2] == kode_member]

        if data_peminjaman_member:
            print("Member masih meminjam buku. Data peminjaman akan dihapus lebih dulu")
            for peminjaman in data_peminjaman_member:
                kode_pinjam = peminjaman[0]
                index_pinjam = next((i for i, data in enumerate(data_pinjam) if data[0] == kode_pinjam), None)
                if index_pinjam is not None:
                    kode_buku = data_pinjam[index_pinjam][1]
                    qty = data_pinjam[index_pinjam][4]
                    index_buku = next((i for i, data in enumerate(data_buku) if data[0] == kode_buku), None)
                    if index_buku is not None:
                        data_buku[index_buku][4] += qty
                    else:
                        print("Kode buku tidak ditemukan")
                    del data_pinjam[index_pinjam]
                else:
                    print("Kode peminjaman tidak ditemukan")
            print("Data peminjaman terkait telah dihapus")

        konfirmasi = input("Yakin akan menghapus data member ini beserta data peminjamannya? (y/n): ")

        if konfirmasi.lower() == 'y':
            del data_member[index_member]
            tulis_data_member(data_member)
            tulis_data_peminjaman(data_pinjam)
            tulis_data_buku(data_buku)
            print("Data member beserta data peminjamannya telah dihapus")
        else:
            print("Penghapusan gagal")

        ulang = input("Lakukan penghapusan lagi? (y/n): ")
        if ulang.lower() != 'y':
            break

def hapus_data_peminjaman(data_pinjam, data_buku):
    """
    Fungsi untuk menghapus data peminjaman dari daftar peminjaman. Jumlah buku yang  dipinjam
    akan dikembalikan ke stok buku awal pada daftar buku.

    Parameters:
    data_pinjam (list) : Daftar data peminjaman yang ada.
    data_buku (list) : Daftar data buku yang ada.
    """
    while True:
        kode_pinjam = input("Masukkan kode peminjaman yang akan dihapus: ")
        if kode_pinjam == "":
            print("Kode peminjaman kosong. Silakan isi kode kembali")
            continue

        index = None
        for i, data in enumerate(data_pinjam):
            if data[0] == kode_pinjam:
                index = i
                break
        
        if index is None:
            print("Kode peminjam tidak ditemukan")
            continue

        kode_buku = data_pinjam[index][1]
        qty = data_pinjam[index][5]
        index_buku = next((i for i, data in enumerate(data_buku) if data[0] == kode_buku), None)
        if index_buku is not None:
            data_buku[index][4] += qty
            tulis_data_buku(data_buku)
        else:
            print("Kode buku tidak ditemukan")

        konfirmasi = input("Yakin akan menghapus data peminjaman ini? (y/n): ")

        if konfirmasi.lower() == 'y':
            del data_pinjam[index]
            tulis_data_peminjaman(data_pinjam)
            print("Data peminjaman telah dihapus")
        else:
            print("Penghapusan data dibatalkan")

        ulang = input("Lakukan penghapusan lagi? (y/n): ")
        if ulang.lower() != 'y':
            break

def pengembalian_buku(data_buku, data_pinjam):
    """
    Fungsi untuk melakukan pengelolaan pengembalian buku.
    Mengubah status peminjaman menjadi "Selesai" dan menghitung tarif serta denda jika ada.

    Parameters:
    data_buku (list) : Daftar data buku yang ada.
    data_pinjam (list) : Daftar data peminjaman yang ada.
    """
    while True:
        kode_pinjam = input("Masukkan kode peminjaman yang akan dikembalikan: ")
        if ")" in kode_pinjam:
            print("Dibatalkan")
            break
        elif kode_pinjam == "":
            print("Kode peminjaman kosong. Silakan isi kode kembali")
            continue

        index_pinjam = None
        for i, data in enumerate(data_pinjam):
            if data[0] == kode_pinjam:
                index_pinjam = i
                break
        
        if index_pinjam is None:
            print("Kode peminjaman tidak ditemukan")
            continue
        
        if data_pinjam[index_pinjam][8].strip() == "Dipinjam":
            kode_buku = data_pinjam[index_pinjam][1]
            qty = data_pinjam[index_pinjam][5]
            tgl_pinjam = datetime.datetime.strptime(data_pinjam[index_pinjam][6], "%Y-%m-%d")
            tgl_kembali = datetime.datetime.now()

            index_buku = next((i for i, data in enumerate(data_buku) if data[0] == kode_buku), None)
            if index_buku is not None:
                data_buku[index_buku][4] += qty

                keterlambatan = (tgl_kembali - tgl_pinjam).days
                biaya = 0

                if keterlambatan >= 4:
                    if data_pinjam[index_pinjam][2].lower() != 'non-member':
                        terlambat = keterlambatan - 3
                        biaya = terlambat * 1000
                        print(f"Terlambat {terlambat} hari. Dikenakan biaya sebesar Rp {biaya}")
                elif keterlambatan >= 4:
                    if data_pinjam[index_pinjam][2].lower() == 'non-member':
                        terlambat = keterlambatan - 3
                        biaya = terlambat * 1000
                        total = keterlambatan * 1000
                        print(f"Terlambat {terlambat} hari. Dikenakan denda Rp {biaya}. Total bayar Rp {total}")
                else:
                    if data_pinjam[index_pinjam][2].lower() == 'non-member':
                        if keterlambatan != 0:
                            biaya = keterlambatan * 1000
                            print(f"Total bayar Rp {biaya}")
                        else:
                            biaya = 1000
                            print(f"Total bayar Rp {biaya}")

            data_pinjam[index_pinjam][7] = datetime.datetime.now().strftime("%Y-%m-%d")
            data_pinjam[index_pinjam][8] = "Selesai"
            data_pinjam[index_pinjam][9] = biaya
            print("Buku telah dikembalikan")
            tulis_data_buku(data_buku)
        else:
            print("Buku telah dikembalikan sebelumnya")
        
        tulis_data_peminjaman(data_pinjam)

        ulang = input("Lakukan pengembalian lagi? (y/n): ")
        if ulang.lower() != 'y':
            break

def cari_buku(data_buku):
    """
    Fungsi untuk mencari buku berdasarkan kata kunci pada judul, penulis, atau kode buku.

    Parameters:
    data_buku (list) : Daftar data buku yang ada.
    """
    while True:
        kata_kunci = input("Masukkan kata kunci untuk pencarian: ").lower()
        if kata_kunci == "":
            print("Kata kunci kosong")
            continue

        hasil_pencarian = list()
        for buku in data_buku:
            if kata_kunci in buku[0].lower() or kata_kunci in buku[1].lower() or kata_kunci in buku[2].lower():
                hasil_pencarian.append(buku)

        if not hasil_pencarian:
            print("Kata kunci tidak ada dalam data buku")
        else:
            print("------------------------------------------------------------------------------------------------------------------------------------")
            print("|                                                           DAFTAR BUKU                                                            |")
            print("------------------------------------------------------------------------------------------------------------------------------------")
            print("| Kode Buku |          Judul          |          Penulis          | Tahun Terbit | Qty |    Created Date     |     Updated Date    |")
            print("------------------------------------------------------------------------------------------------------------------------------------")
            for kode_buku, judul, penulis, tahun_terbit, qty, crd, upd in hasil_pencarian:
                print("|{:^11}| {:<23} | {:<25} |{:^14}|{:^5}|{:^21}|{:^21}|".format(kode_buku, judul, penulis, tahun_terbit, qty, crd, upd[:19]))
            print("------------------------------------------------------------------------------------------------------------------------------------")

        ulang = input("Lakukan pencarian lagi? (y/n): ")
        if ulang.lower() != 'y':
            break

def main():
    """
    Fungsi utama untuk menjalankan aplikasi perpustakaan.
    """
    data_buku = baca_data_buku()
    data_pinjam = baca_data_peminjaman()
    data_member = baca_data_member()

    print("====================================================================================================================================")
    print("|                                                          APLIKASI PERPUSTAKAAN                                                   |")
    print("====================================================================================================================================")

    while True:
        try:
            menu_aksi()
            pilihan = int(input())
        except ValueError:
            print("Pilihan tidak ditemukan")
            continue

        match pilihan:
            case 1: cetak_tabel_buku(data_buku)
            case 2: tambah_data_buku(data_buku)
            case 3: ubah_data_buku(data_buku)
            case 4: hapus_data_buku(data_buku, data_pinjam)
            case 5: cetak_tabel_member(data_member)
            case 6: tambah_data_member(data_member)
            case 7: ubah_data_member(data_member)
            case 8: hapus_data_member(data_member, data_pinjam, data_buku)
            case 9: cetak_tabel_peminjaman(data_pinjam, data_buku)
            case 10: tambah_data_peminjam(data_pinjam, data_buku, data_member)
            case 11: ubah_data_peminjaman(data_pinjam)
            case 12: hapus_data_peminjaman(data_pinjam, data_buku)
            case 13: cari_buku(data_buku)
            case 14: pengembalian_buku(data_buku, data_pinjam)
            case 15: print("Terima kasih, silakan datang kembali")
            case _: print("Ulangi lagi")
        if pilihan == 15:
            break

if __name__ == '__main__':
    main()