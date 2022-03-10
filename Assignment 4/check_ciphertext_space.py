import random
import string
import subprocess
from collections import defaultdict

def random_plaintxt():
    plaintxt = ''.join(random.choice(string.ascii_lowercase) for _ in range(16))
    return plaintxt

def freq_analysis(ciphertxt):
    freq = defaultdict(int)
    cnt = 0
    for char in ciphertxt:
        cnt += 1
        freq[char] += 1

    for key , val in freq.items():
        freq[key] = round(val / cnt * 100, 1)

    freq = dict(sorted(freq.items(), key = lambda item: item[0]))
    return freq

with open('random_plaintexts.txt', 'w') as f:
    f.writelines([
        '3Miners1Course\n',
        'cryptoiscool\n',
        '4\n',
        'read\n'
    ])
    for i in range(100):
        f.writelines([
            f'{random_plaintxt()}\n',
            'c\n'
        ])
    f.writelines([
        'back\n',
        'exit\n'
    ])

subprocess.run('./script_for_ciphertext_space.sh')
with open('random_ciphertexts.txt', 'r') as f:
    ciphertxts = [line.strip() for line in f.readlines()]

print(freq_analysis(''.join(ciphertxt for ciphertxt in ciphertxts)))

# {'d': 6.9, 'e': 5.6, 'f': 7.2, 'g': 6.6, 'h': 5.9, 'i': 6.2, 'j': 6.6, 'k': 6.3, 'l': 6.2, 'm': 5.6, 'n': 5.8, 'o': 6.4, 'p': 6.0, 'q': 6.1, 'r': 5.7, 's': 6.9}