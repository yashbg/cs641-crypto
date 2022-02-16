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

# a = [429, 1973, 7596]
# b = [
#     431955503618234519808008749742,
#     176325509039323911968355873643,
#     98486971404861992487294722613
# ]

a = [1973 - 429, 7596 - 1973]
b = [
    (176325509039323911968355873643 * modInverse(431955503618234519808008749742)) % p,
    (98486971404861992487294722613 * modInverse(176325509039323911968355873643)) % p
]

print(a)
print(b)

c = []
for i in range(-10000, 10000):
    if (1 - i * a[0]) % a[1] == 0:
        j = (1 - i * a[0]) / a[1]
        c.append([i, j])
print(c)

gs = []
for i in range(len(c)):
    gs.append(solve(b, c[i]))

for g in sorted(gs):
    print(g)
