def validasi_email(kata):
    if kata.count('@') == 1:
        return True
    else:
        return False
    
email = input()

print(validasi_email(email))
print(validasi_email('@admin@wkwkwk.com'))
print(validasi_email('admin@wkwkwk.com'))
print(validasi_email('adminwkwkwk.com'))