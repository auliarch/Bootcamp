def data_pemain_catur(n):
    data_pemain = []
    for _ in range(n):
        nama, rk, rr, rs = input().split()
        rk, rr, rs = int(rk), int(rr), int(rs)
        data_pemain.append((nama, rk, rr, rs))
    return data_pemain

def hitung_rata_rata(data):
    total_rk, total_rr, total_rs = 0, 0, 0
    for pemain in data:
        total_rk += pemain[1]
        total_rr += pemain[2]
        total_rs += pemain[3]

    rata_rata_rk = total_rk // len(data)
    rata_rata_rr = total_rr // len(data)
    rata_rata_rs = total_rs // len(data)

    return rata_rata_rk, rata_rata_rr, rata_rata_rs

def main():
    n = int(input())
    data_pemain = data_pemain_catur(n)
    rk, rr, rs = hitung_rata_rata(data_pemain)
    print(rk, rr, rs)
    
if __name__ == "__main__":
    main()