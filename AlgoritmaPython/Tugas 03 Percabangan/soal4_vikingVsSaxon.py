#input dan casting
pasukan_viking = int(input("Jumlah pasukan Viking: "))
pasukan_saxon = int(input("Jumlah pasukan Saxon: "))

#percabangan dan output
if ( pasukan_viking * 4 ) > pasukan_saxon:
    print("viking menang")
elif pasukan_saxon > ( pasukan_viking * 4 ):
    print("saxon menang")
else:
    print("imbang")