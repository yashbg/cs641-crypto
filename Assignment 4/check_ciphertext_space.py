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

with open('plaintexts.txt', 'w') as f:
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

subprocess.run('./script.sh')

with open('ciphertexts.txt', 'r') as f:
    ciphertxts = [line.strip() for line in f.readlines()]

print(freq_analysis(''.join(ciphertxt for ciphertxt in ciphertxts)))
