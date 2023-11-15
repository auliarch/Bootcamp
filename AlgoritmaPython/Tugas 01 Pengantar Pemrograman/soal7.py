# input jari-jari bola
r = input()

# type casting ke float
r = float(r)

# deklarasi variabel phi
phi = 3.14

# hitung luas permukaan bola
luas = 4 * phi * r ** 2

# output dengan pembulatan 4 digit di belakang koma
print("{:.4f}".format(luas))