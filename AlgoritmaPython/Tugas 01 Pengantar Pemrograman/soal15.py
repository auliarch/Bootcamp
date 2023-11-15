nominal = input()

nominal = int(nominal)

ribuan = nominal // 1000
sisa = nominal % 1000

print(f"Uang tersebut mengandung pecahan seribu sebanyak {ribuan} "
      f"dan sisa uang sebanyak {sisa}")