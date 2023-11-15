def diskon(total_belanja):
    if total_belanja >= 250000:
        return total_belanja * 0.15
    else:
        return 0
    
tb = int(input())

print(diskon(tb))