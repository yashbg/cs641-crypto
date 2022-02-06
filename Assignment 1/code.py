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

# with open('Assignment 1/cipher.txt') as f:
#     ciphertxt = f.read()
# print(ciphertxt)
# print()

original_ciphertxt = '''omkf pi hdn cmgef icphsck .H krg vphqkc c,
fic mco kqgf ioqag eo qfcmckf oq ficpihdn
cm .Kg dcgeficu hfcm pi hdn cmklo uuncdgmc
oqfc mc kfoq afihqfiokgq c!Fi cpgy cvkc yeg 
mfio kdck kha cokh kodjuck vn k fofvfo
gqpojicmoqli opiyoa of kihsc nccqki oefc
ynr2 juhpck. Fi c jhkklgm yok oMxr9V1x ya
flofigvffic xvgfck. Fio kokfice
'''

ciphertxt = '''omkf pihdncm ge fic phsck.
Hk rgv phq kcc, ficmc ok qgfioqa ge oqfcmckf oq fic pihdncm.
Kgdc ge fic uhfcm pihdncmk louu nc dgmc oqfcmckfoqa fihq fiok gqc!
fic pgyc vkcy egm fiok dckkhac ok h kodjuc kvnkfofvfogq pojicm oq liopi yoaofk ihsc nccq kioefcy nr 2 juhpck.
fic jhkklgmy ok oMxr9V1xyaf lofigvf fic xvgfck.
Fiok ok fic e'''

freq = freq_analysis(ciphertxt)
print(freq)
print()

with open('Assignment 1/frequencies.txt', 'w') as f:
    f.write(json.dumps(freq, indent=0))

mapping = {
    'c': 'e',
    'f': 't',
    'i': 'h',

    'm': 'r',

    'o': 'i',
    'q': 'n',

    'k': 's',

    'p': 'c',
    'h': 'a',
    's': 'v',
    
    'd': 'm',
    'n': 'b',

    'g': 'o',
    'e': 'f',

    'u': 'l',

    'r': 'y',
    'v': 'u',

    'a': 'g',

    'l': 'w',

    'y': 'd',

    'j': 'p',

    'x': 'q',
}

plaintxt = decrypt(ciphertxt.lower(), mapping)
print(plaintxt)
print()

final_ciphertxt = '''Fiok ok fic eomkf pihdncm ge fic phsck.
Hk rgv phq kcc, ficmc ok qgfioqa ge oqfcmckf oq fic pihdncm.
Kgdc ge fic uhfcm pihdncmk louu nc dgmc oqfcmckfoqa fihq fiok gqc!
fic pgyc vkcy egm fiok dckkhac ok h kodjuc kvnkfofvfogq pojicm oq liopi yoaofk ihsc nccq kioefcy nr 2 juhpck.
fic jhkklgmy ok oMxr9V1xyaf lofigvf fic xvgfck.'''

final_plaintxt = decrypt(final_ciphertxt.lower(), mapping)
print(final_plaintxt)

with open('Assignment 1/plaintext.txt', 'w') as f:
    f.write(final_plaintxt)
