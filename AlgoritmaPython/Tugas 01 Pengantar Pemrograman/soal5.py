# input besaran kecepatan dalam km / jam
km = input()

# type casting ke float
km = float(km)

# proses konversi kecepatan dari km / jam ke meter / detik
hasil = km * 0.277778

# output dengan pembulatan 2 digit di belakang koma
print("{:.2f}".format(hasil))