from collections import defaultdict
import json

def freq_analysis(ciphertxt):
    freq = defaultdict(int)
    cnt = 0

    for char in ciphertxt.lower():
        if 0 <= ord(char) - ord('a') < 26:
            cnt += 1
            freq[char] += 1

    for key , val in freq.items():
        freq[key] = round(val / cnt * 100, 1)

    freq = dict(sorted(freq.items(), key = lambda item: item[1], reverse=True))
    
    return freq

def decrypt(ciphertxt, mapping):
    table = ciphertxt.maketrans(mapping)
    return ciphertxt.translate(table)


with open('Assignment 2/cipher.txt') as f:
    ciphertxt = f.read()
print(ciphertxt)
print()

freq = freq_analysis(ciphertxt)
print(freq)
print()

with open('Assignment 2/frequencies.txt', 'w') as f:
    f.write(json.dumps(freq, indent=0))

mapping = {
    # 'Y': 'e',
    'C': 't',

    'Q': 'h',

    'D': 'e',
    
    # # 'D': 'i',
    # # 'F': 'n',

    
}

plaintxt = decrypt(ciphertxt, mapping)
print(plaintxt)
print()

with open('Assignment 2/plaintext.txt', 'w') as f:
    f.write(plaintxt)
