#input
angka1 = int(input())
angka2 = int(input())

#proses
if angka1 > 0 or angka2 < 100:
    print(f"{angka1} lebih besar dari 0 dan {angka2} kurang dari 100")
else:
    print(f"Bilangan tidak memenuhi syarat")