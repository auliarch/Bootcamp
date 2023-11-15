# input nilai mil dan kilomter
mil = input()
kilometer = input()

# type casting menjadi int
mil = int(mil)
kilometer = int(kilometer)

# menghitung konversi mil menjadi kilometer dan kilometer menjadi mil
mil_ke_kilometer =  mil * 1.61
kilometer_ke_mil = kilometer / 1.61

# output dengan pembulatan 2 digit di belakang koma
print("{:.2f}".format(mil_ke_kilometer))
print("{:.2f}".format(kilometer_ke_mil))