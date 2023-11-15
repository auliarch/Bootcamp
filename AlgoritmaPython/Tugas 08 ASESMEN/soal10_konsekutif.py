def bil_konsekutif(angka):
    angka_str = str(angka)
    n = len(angka_str)

    for i in range(1, n):
        selisih = int(angka_str[i]) - int(angka_str[i - 1])
        if selisih != 1 and selisih != -1:
            return 'false'
        
    return 'true'

x = int(input())
print(bil_konsekutif(x))