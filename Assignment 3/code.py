def power(x, y, m):
    if (y == 0):
        return 1

    p = power(x, y // 2, m) % m
    p = (p * p) % m
 
    if(y % 2 == 0):
        return p
    else:
        return ((x * p) % m)

def modInverse(a, m):
    return power(a, m - 2, m)

def solve(b, c):
    ans = 1
    for i in range(len(c)):
        if c[i] < 0:
            ans = (ans * power(modInverse(b[i], p), -c[i], p)) % p
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

c = []

for i in range(-1000, 1001):
    for j in range(-1000, 1001):
        if (1 - i * a[0] - j * a[1]) % a[2] == 0:
            k = (1 - i * a[0] - j * a[1]) / a[2]
            c.append([i, j, k])

print(c)

gs = []
for i in range(len(c)):
    gs.append(solve(b, c[i]))

for g in sorted(gs):
    print(g)
