def dec_to_base_x(num, base):
    result = []

    while num:
        result.append(num%base)
        num //= base
    
    return ''.join(map(str, result[::-1]))
    
num = 19

print(dec_to_base_x(num, 2))
print(dec_to_base_x(num, 3))
print(dec_to_base_x(num, 8))
print(dec_to_base_x(num, 16))

