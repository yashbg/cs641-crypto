from utils import decryption, generate_round_keys, str_to_bin
from brute_force import final_key

final_round_keys = generate_round_keys(final_key)

#Encrypted Password obtained from game
encrypted_password = 'ofhnfddqmlopkrlesipofmnepjkjnqpi'

# Decrypt password using the obtained final_key
d = decryption(str_to_bin(encrypted_password[:16]), final_round_keys, 6) + decryption(str_to_bin(encrypted_password[16:]), final_round_keys, 6)
print("\n\nPassword in binary form: ", d)

ans = ""
for i in range(0, len(d), 8):
    s = d[i:i+8]
    ans += chr(int(s, 2))
print("\nDecrypted password: ", ans)

# Removing trailing 0s
while ans[-1] == '0':
    ans = ans[:-1]
print("\nFinal password: ", ans)
