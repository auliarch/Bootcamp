#input
kata = str(input())

#percabangan
if kata == "genap":
    for i in range(1, 11):
        if i % 2 == 0:
            print(i, end=' ')
elif kata == "ganjil":
    for i in range(1, 11):
        if i % 2 != 0:
            print(i, end=' ')