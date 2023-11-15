#input
fisik_sehat = input("Apakah kondisi fisik sehat? (ya atau tidak): ")
cukup_bekal = input("Apakah cukup bekal? (ya atau tidak): ")
cuaca_bagus = input("Apakah cuaca terlihat bagus? (ya atau tidak): ")

#if statement untuk memeriksa kondisi
if fisik_sehat == "ya" and cukup_bekal == "ya" and cuaca_bagus == "ya":
    print("berkemah")
else:
    print("tidak berkemah")