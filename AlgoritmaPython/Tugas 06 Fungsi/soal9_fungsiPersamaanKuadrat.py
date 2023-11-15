#pendefinisian fungsi
def akar_pers_kuadrat(a, b, c):
    D = b ** 2 - 4 * a * c 
    if D < 0:
        return "Tidak ada akar nyata"
    elif D == 0:
        x = -b / (2 * a)
        return "Ada akar nyata, x = " + str(x)
    else:
        x1 = (-b + (D ** 0.5)) / (2 * a)
        x2 = (-b + (D ** 0.5)) / (2 * a)
        return "Ada akar nyata, x1 = " + str(x1) + " x2 = " + str(x2)
    
#input dan casting
nilai1 = int(input())
nilai2 = int(input())
nilai3 = int(input())

hasil = akar_pers_kuadrat(nilai1, nilai2, nilai3)

print(hasil)