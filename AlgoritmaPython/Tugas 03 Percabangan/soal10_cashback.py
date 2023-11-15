#input dan casting
p1 = int(input("Poin 1: "))
p2 = int(input("Poin 2: "))
p3 = int(input("Poin 3: "))
p4 = int(input("Poin 4: "))
p5 = int(input("Poin 5: "))

cashback = (p1 + p2 + p3) == (p3 + p4 + p5)
diskon =((p2 + p3 + p4) % (p1 + p5)) == 0


#percabangan
if cashback and diskon:
    print("cashback\ndiskon")
else:
    if cashback:
        print("cashback")
    elif diskon:
        print("diskon")