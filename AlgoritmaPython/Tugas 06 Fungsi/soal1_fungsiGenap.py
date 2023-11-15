#pendefinisian fungsi genap
def genap(angka):
    return angka % 2 == 0

#pendefinisian program utama
def main():
    #input dan casting
    bil = int(input())

    #pemangilan fungsi dan pencetakan hasil
    if genap(bil):
        print("bilangan genap")
    else:
        print("bukan bilangan genap")

#pemanggilan program utama
main()