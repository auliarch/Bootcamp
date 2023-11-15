# Input
suwir_ayam = input("Suwir ayam [True/False]: ")
cakue = input("Cakue [True/False]: ")
ati_ampela = input("Ati Ampela [True/False]: ")
telur = input("Telur [True/False]: ")

harga_dasar = 6000

# Konversi input menjadi bool
suwir_ayam = suwir_ayam == "True"
cakue = cakue == "True"
ati_ampela = ati_ampela == "True"
telur = telur == "True"

# Percabangan
if suwir_ayam:
    harga_dasar += 3000

if cakue:
    harga_dasar += 1500

if ati_ampela:
    harga_dasar += 4500

if telur:
    harga_dasar += 4000

print(harga_dasar)