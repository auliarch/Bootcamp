#pendefinisian fungsi validasi
def validasi(n):
    return 0 <= n <= 100 

#pendefinisian program utama
def main():
    #input dan casting
    nilai = float(input())

    #pemanggilan fungsi
    if validasi(nilai):
        print("valid")
    else:
        print("tidak valid")

#pemanggilan program utama
if __name__ == '__main__':
    main()