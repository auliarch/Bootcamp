def luas_segitiga(alas, tinggi):
    return alas * tinggi / 2

def sama_luas(luas1, luas2):
    if luas1 == luas2:
        hasil = True
    else:
        hasil = False

    return hasil

a1, a2, a3, a4 = map(int, input().split())

hasil_luas1 = luas_segitiga(a1, a2)
hasil_luas2 = luas_segitiga(a3, a4)

print(sama_luas(hasil_luas1, hasil_luas2))