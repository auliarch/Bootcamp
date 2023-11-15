def banyak_huruf_hidup(kata):
    vokal = 'aiueo'
    jumlah = 0

    for i in kata:
        if i in vokal:
            jumlah += 1

    return jumlah

print(banyak_huruf_hidup("bermain"))

string = "hello, world"
print(banyak_huruf_hidup(string))