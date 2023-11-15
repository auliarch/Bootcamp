#input
bil1 = int(input())
bil2 = int(input())
bil3 = int(input())

#percabangan
if bil1 <= bil2 and bil1 <= bil3:
    if bil2 <= bil3:
        hasil = (bil1, bil2, bil3)
    else:
        hasil = (bil1, bil3, bil2)
elif bil2 <= bil1 and bil2 <= bil3:
    if bil1 <= bil3:
        hasil = (bil2, bil1, bil3)
    else:
        hasil = (bil2, bil3, bil1)
else:
    if bil1 <= bil2:
        hasil = (bil3, bil1, bil2)
    else:
        hasil = (bil3, bil2, bil1)

print(hasil)