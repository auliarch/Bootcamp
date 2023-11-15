def hitung_tebakan(angka, angka_tebakan):
    total = 0
    while True:
        angka = str(angka)
        angka_tebakan = str(angka_tebakan)
        if angka_tebakan in angka or angka_tebakan in angka[-1] or angka_tebakan in angka[0]:
            total += 1
            break

        angka_tebakan = int(input())
        total += 1
    
    return total

angka_yang_ditebak = int(input())
tebakan = int(input())

print(hitung_tebakan(angka_yang_ditebak, tebakan))