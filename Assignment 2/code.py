morse_dict = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', 
    '-..': 'D', '.': 'E', '..-.': 'F', 
    '--.': 'G', '....': 'H', '..': 'I', 
    '.---': 'J', '-.-': 'K', '.-..': 'L', 
    '--': 'M', '-.': 'N', '---': 'O', 
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', 
    '...': 'S', '-': 'T', '..-': 'U', 
    '...-': 'V', '.--': 'W', '-..-': 'X', 
    '-.--': 'Y', '--..': 'Z', 
    '.----': '1', '..---': '2', '...--': '3', 
    '....-': '4', '.....': '5', '-....': '6', 
    '--...': '7', '---..': '8', '----.': '9', 
    '-----': '0', '--..--': ', ', '.-.-.-': '.', 
    '..--..': '?', '-..-.': '/', '-....-': '-', 
    '-.--.': '(', '-.--.-': ')'
}

def morse_decoder(morsecode):
    morse_list = morsecode.split()
    key_list = [morse_dict[code] for code in morse_list]
    key = ''.join(key_list)
    return key

with open('Assignment 2/morse_code.txt') as f:
    morsecode = f.read()
print(morsecode)
print()

key = morse_decoder(morsecode)
print(key)

with open('Assignment 2/key.txt', 'w') as f:
    f.write(key)

playfair_sq = [
    ['C', 'R', 'Y', 'P', 'T'],
    ['A', 'N', 'L', 'S', 'I'],
    ['B', 'D', 'E', 'F', 'G'],
    ['H', 'K', 'M', 'O', 'Q'],
    ['U', 'V', 'W', 'X', 'Z'],
]
