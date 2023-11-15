#pendefinisian fungsi perkalian
def perkalian(bilangan_1, bilangan_2):
    return bilangan_1 * bilangan_2

#pendefinisian program utama
def main():
    #input dan casting
    bil1 = float(input())
    bil2 = float(input())

    #pemanggilan fungsi
    hasil_perkalian = perkalian(bil1, bil2)

    #pencetakan hasil perkalian
    print(round(hasil_perkalian, 2))

#pemanggilan program utama
if __name__ == '__main__':
    main()