#input dan casting
p1 = float(input("Review 1: "))
p2 = float(input("Review 2: "))
p3 = float(input("Review 3: "))
p4 = float(input("Review 4: "))

#hitung nilai rata-rata review
rata = ( p1 + p2 + p3 + p4 ) / 4

# percabangan
if rata >= 3.50:
    print("bagus")
elif rata <= 1.50:
    print("kurang")
else:
    print("sedang")