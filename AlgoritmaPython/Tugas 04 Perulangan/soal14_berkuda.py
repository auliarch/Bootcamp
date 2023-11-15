n = int(input())

total = 0

for i in range(n):
    waktu = int(input())
    total += waktu

rata_rata = total / n

print(total)
print('{:.2f}'.format(rata_rata))