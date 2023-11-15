a, b, c, d = map(float, input().split())

berat_kiri = a + d
berat_kanan = b + c

if berat_kiri == berat_kanan:
    print('Ember seimbang? True')
else:
    print('Ember seimbang? False')