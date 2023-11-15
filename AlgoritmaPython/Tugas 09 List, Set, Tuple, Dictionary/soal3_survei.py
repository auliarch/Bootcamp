def survei_buah():
    nama_buah = input().split()
    
    banyak_buah = {}
    for buah in nama_buah:
        banyak_buah[buah] = banyak_buah.get(buah, 0) + 1

    banyak_muncul = max(banyak_buah.values())

    buah_terbanyak = []
    for buah, muncul in banyak_buah.items():
        if muncul == banyak_muncul:
            buah_terbanyak.append(buah)

    if len(buah_terbanyak) == 1:
        return buah_terbanyak[0]
    else:
        return ""

def main():
    print(survei_buah())

if __name__ == "__main__":
    main()