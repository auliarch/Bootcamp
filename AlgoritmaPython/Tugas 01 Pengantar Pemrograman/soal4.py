#input
n = input()

#type casting ke float
n = float(n)

#proses perhitungan
Fx = (n + 1 / n) ** 2

#output pembulatan 1 digit di belakang koma
print("{:.1f}".format(Fx))