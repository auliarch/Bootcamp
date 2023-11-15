def penumpang_ilegal():
    kapasitas = int(input())
    penumpang = list(map(int, input().split()))
    total = 0
    for penumpang_per_gerbong in penumpang:
        if penumpang_per_gerbong > kapasitas:
            total += penumpang_per_gerbong - kapasitas
    return total

def main():
    print(penumpang_ilegal())

if __name__ == "__main__":
    main()