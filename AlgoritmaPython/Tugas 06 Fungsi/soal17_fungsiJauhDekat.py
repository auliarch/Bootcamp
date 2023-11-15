def apakah_dekat(x1, y1, x2, y2):
    jarak = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

    if jarak <= 1:
        return 'dekat'
    else:
        return 'jauh'
    
a1 = float(input())
b1 = float(input())
a2 = float(input())
b2 = float(input())

print(apakah_dekat(a1, b1, a2, b2))