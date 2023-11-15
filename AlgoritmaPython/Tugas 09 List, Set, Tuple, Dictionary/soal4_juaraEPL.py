def klasemen_epl():
    n = int(input())
    klasemen = {}
    for _ in range(n):
        nk, ma, me, dr, kl, gm, gk = input().split()
        klasemen[nk] = [int(ma), int(me), int(dr), int(kl), int(gm), int(gk)]
    return klasemen

def hitung_point(a):
    for k, v in a.items():
        point = v[1] * 3 + v[2]
        v.append(point)
        a.update({k: v})
    return a

def juara(b):
    max_point = 0
    klub_juara = ""
    for k, v in b.items():
        if v[6] > max_point:
            max_point = v[6]
            klub_juara = k
    return klub_juara

def main():
    standing = klasemen_epl()
    standing = hitung_point(standing)
    print(juara(standing))

if __name__ == "__main__":
    main()