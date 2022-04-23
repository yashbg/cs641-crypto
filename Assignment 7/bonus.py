p = [22, 0, 104, 11, 116, 23, 34, 8, 86, 85, 104, 36, 32, 34, 115, 63, 87, 19, 38, 29, 4, 36, 6, 9, 99, 89, 83, 10, 80, 42, 27, 110]
pswd = ''
len_pswd = p[0]
mod = 127

def check_zeroes(root, e): # Function checks whether a character is a root
    polynomial = 0 # We define the polynomial
    for k in range(p[0]+1):
        polynomial += pow(-1, k) * e[k] * pow(root, p[0] - k, mod) # We calculate the polynomial
        polynomial %= mod
    if polynomial == 0: # If it is zero for the polynomial then return 1 ELSE 0
        return 1
    return 0

c = 'f' # We start with c = 'f' as given in the problem statement

while len(pswd) < len_pswd: 

    e = [1] # e_0 is always 1
    for k in range(1, p[0]+1):
        coeff = 0
        for i in range(1, k+1):
            coeff += pow(-1, i-1) * e[k-i] * p[i]
        coeff *= pow(k, 125, mod) # k^125 % 127
        coeff %= mod
        e = e + [coeff]

    root = ord(c)
    if check_zeroes(root, e):
        pswd += c
        for k in range(len(p)): # Updating the hash p
            temp = p[k]
            temp -= pow(ord(c),k,  mod)
            temp %= mod
            p[k] = temp

    else:
        c = chr(root + 1)
    root = ord(c)

print(f"Final Password : {pswd}")
