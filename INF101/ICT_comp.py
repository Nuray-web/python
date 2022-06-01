def decompress(data):
    decomp = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decomp += char * int(count)
            count = ''
    return decomp

print("Decompressed version of your matrix: ")
decomp_val1 = decompress('2w2b2w')
print(('\n' + decomp_val1) *2)

decomp_val2 = decompress('0w6b')
print(decomp_val2)
print(decomp_val2)

decomp_val3 = decompress('2w2b2w')
print((decomp_val3 + '\n') *2)


def compress(data):
    comp = ''
    prev_char = ''
    count = 1
    if not data: return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                comp += str(count) + ' '
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        comp += str(count) + ' '
        return comp

print("Compressed version of your text: ")
comp_val = compress(decomp_val1)
print(('\n' + comp_val) *2)
comp_val = compress(decomp_val2)
print((comp_val))
print((comp_val))
comp_val = compress(decomp_val3)
print((comp_val + '\n') *2)
