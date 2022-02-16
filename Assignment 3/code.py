from operator import mod


def power(x, y, m):
    if (y == 0):
        return 1

    p = power(x, y // 2, m) % m
    p = (p * p) % m
 
    if(y % 2 == 0):
        return p
    else:
        return ((x * p) % m)

def modInverse(a):
    return power(a, p - 2, p)

def solve(b, c):
    ans = 1
    for i in range(len(c)):
        if c[i] < 0:
            ans = (ans * power(modInverse(b[i]), -c[i], p)) % p
        else:
            ans = (ans * power(b[i], c[i], p)) % p
    return ans

p = 455470209427676832372575348833

a = [429, 1973, 7596]
b = [
    431955503618234519808008749742,
    176325509039323911968355873643,
    98486971404861992487294722613
]

a_dif = [a[1] - a[0], a[2] - a[1]]
b_dif = [
    (b[1] * modInverse(b[0])) % p,
    (b[2] * modInverse(b[1])) % p
]

print(a_dif)
print(b_dif)

c = []
for i in range(-10000, 10000):
    if (1 - i * a_dif[0]) % a_dif[1] == 0:
        j = (1 - i * a_dif[0]) // a_dif[1]
        c.append([i, j])
print(c)

gs = []
for i in range(len(c)):
    gs.append(solve(b_dif, c[i]))

for g in sorted(gs):
    print(g)
print()

g = 52565085417963311027694339
coef = [-2298, 631]

g_inv = modInverse(g)
pwd = (b[0] * power(g_inv, a[0], p)) % p
print(pwd)
