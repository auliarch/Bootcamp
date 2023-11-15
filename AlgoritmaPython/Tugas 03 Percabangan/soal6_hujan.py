#input
hujan = str(input("Apakah hujan turun? [ya/tidak] "))
payung = str(input("Punya payung? [ya/tidak] "))

#if statement
if hujan == "tidak" or payung == "ya":
   print("berangkat")
else:
   print("diam di rumah")