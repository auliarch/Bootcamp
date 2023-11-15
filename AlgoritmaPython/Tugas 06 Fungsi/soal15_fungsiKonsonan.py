def banyak_konsonan(kata):
    konsonan = 'bcdfghjklmnpqrstvwxyz'
    jumlah = 0

    for i in kata:
        if i in konsonan:
            jumlah += 1

    return jumlah

print(banyak_konsonan("bermain"))

string = "hello, world"
print(banyak_konsonan(string))