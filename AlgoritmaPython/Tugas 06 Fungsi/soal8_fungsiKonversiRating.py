def konversi_rating(n):
    if n == 1:
        return "kurang sekali"
    elif n == 2:
        return "kurang"
    elif n == 3:
        return "sedang"
    elif n == 4:
        return "bagus"
    elif n == 5:
        return "bagus sekali"
    else:
        return "invalid"

nilai = 2
h = konversi_rating(nilai)
print(h)