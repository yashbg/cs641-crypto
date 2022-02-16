def inverse(a):
    return pow(a, p - 2, p)

def solve(b, c):
    ans = 1
    for i in range(len(c)):
        if c[i] < 0:
            ans = (ans * pow(inverse(b[i]), -c[i], p)) % p
        else:
            ans = (ans * pow(b[i], c[i], p)) % p
    return ans

p = 455470209427676832372575348833

a = [429, 1973, 7596]
b = [
    431955503618234519808008749742,
    176325509039323911968355873643,
    98486971404861992487294722613,
]

a_dif = [
    a[1] - a[0],
    a[2] - a[1],
]

b_dif = [
    (b[1] * inverse(b[0])) % p,
    (b[2] * inverse(b[1])) % p,
]

print(a_dif)
print(b_dif)
print()

c = []
for i in range(-10000, 10000):
    if (1 - i * a_dif[0]) % a_dif[1] == 0:
        j = (1 - i * a_dif[0]) // a_dif[1]
        c.append([i, j])
print(c)
print()

g_list = []
for i in range(len(c)):
    g_list.append(solve(b_dif, c[i]))

for g in g_list:
    print(g)
print()

g = 52565085417963311027694339

g_inv = inverse(g)
pwd = (b[0] * pow(g_inv, a[0], p)) % p
print(pwd)
