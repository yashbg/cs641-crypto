from collections import defaultdict

original_str = '''omkf pi hdn cmgef icphsck .H krg vphqkc c,
fic mco kqgf ioqag eo qfcmckf oq ficpihdn
cm .Kg dcgeficu hfcm pi hdn cmklo uuncdgmc
oqfc mc kfoq afihqfiokgq c!Fi cpgy cvkc yeg 
mfio kdck kha cokh kodjuck vn k fofvfo
gqpojicmoqli opiyoa of kihsc nccqki oefc
ynr2 juhpck. Fi c jhkklgm yok oMxr9V1x ya
flofigvffic xvgfck. Fio kokfice
'''

str = '''omkf pihdncm ge fic phsck.
Hk rgv phq kcc, ficmc ok qgfioqa ge oqfcmckf oq fic pihdncm.
Kgdc ge fic uhfcm pihdncmk louu nc dgmc oqfcmckfoqa fihq fiok gqc!
fic pgyc vkcy egm fiok dckkhac ok h kodjuc kvnkfofvfogq pojicm oq liopi yoaofk ihsc nccq kioefcy nr 2 juhpck.
fic jhkklgmy ok oMxr9V1xyaf lofigvf fic xvgfck.
Fiok ok fic e'''

freq = defaultdict(int)

cnt = 0

for char in str.lower():
    if 0 <= ord(char) - ord('a') < 26:
        cnt += 1
        freq[char] += 1

for key , val in freq.items():
    freq[key] = round(val / cnt * 100, 1)

freq = dict(sorted(freq.items(), key = lambda item: item[1], reverse=True))

print(freq)
print()

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

str1 = str.lower().translate(str.maketrans(mapping))

print(str1)
print()

final_str = '''Fiok ok fic eomkf pihdncm ge fic phsck.
Hk rgv phq kcc, ficmc ok qgfioqa ge oqfcmckf oq fic pihdncm.
Kgdc ge fic uhfcm pihdncmk louu nc dgmc oqfcmckfoqa fihq fiok gqc!
fic pgyc vkcy egm fiok dckkhac ok h kodjuc kvnkfofvfogq pojicm oq liopi yoaofk ihsc nccq kioefcy nr 2 juhpck.
fic jhkklgmy ok oMxr9V1xyaf lofigvf fic xvgfck.'''

text = final_str.lower().translate(final_str.maketrans(mapping))

print(text)
