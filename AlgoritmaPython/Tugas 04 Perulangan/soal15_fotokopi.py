h = int(input("jumlah ktp: "))
k = int(input("maksimal fotokopi: "))

jumlah = 0

for i in range(h):
    total = int(input())

    if jumlah + total <= k:
        jumlah += total
    else:
        jumlah = k

print(f'Hasil ktp yang bisa di fotokopi sebanyak {jumlah}')