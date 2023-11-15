# input jari-jari bola
r = input()

# type casting ke float
r = float(r)

# deklarasi variabel phi
phi = 3.14

# hitung volume bola
volume = 4 / 3 * phi * r ** 3

# output dengan pembulatan 2 digit di belakang koma
print("{:.2f}".format(volume))