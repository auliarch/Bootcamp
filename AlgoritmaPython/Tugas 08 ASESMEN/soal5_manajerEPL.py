def pemecatan():
    if hasil_pertandingan.count('kalah') == 5:
        return 'dipecat'
    elif hasil_pertandingan.count('menang') >= 1:
        return 'tidak dipecat'
    else:
        return 'tidak dipecat'
    
hasil_pertandingan = str(input().split())

print(pemecatan())