def balik_susunan(angka):
    nilai = str(angka)
    balik = nilai[::-1]
    hasil = ' '.join(balik)
    
    return hasil

x = int(input())

print(balik_susunan(x))