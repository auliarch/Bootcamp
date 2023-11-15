#pendefinisian fungsi sapa nama
def sapa_nama(kata):
    return "Halo, " + kata

#pendefinisian program utama
def main():
    #input
    nama = str(input())
    
    #pemanggilan fungsi
    hasil = sapa_nama(nama)
    
    #output
    print(hasil)

#pemanggilan program utama
if __name__ == '__main__':
    main()