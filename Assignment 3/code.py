def modInverse(a, m):
    # If a and m are relatively prime,
    # then modulo inverse is a^(m-2) mode m
    return power(a, m - 2, m)
 
# To compute x^y under modulo m
 
 
def power(x, y, m):
 
    if (y == 0):
        return 1
 
    p = power(x, y // 2, m) % m
    p = (p * p) % m
 
    if(y % 2 == 0):
        return p
    else:
        return ((x * p) % m)

def solve(b, i, j, k):
    ans = 1
    if i < 0:
        ans *= power(modInverse(b[0], p), i, p)
    else:
        ans *= power(b[0], i, p)
    if j < 0:
        ans *= power(modInverse(b[1], p), j, p)
    else:
        ans *= power(b[1], j, p)
    if k < 0:
        ans *= power(modInverse(b[2], p), k, p)
    else:
        ans *= power(b[2], k, p)
    return ans


p = 455470209427676832372575348833

a = [429, 1973, 7596]
b = [
    431955503618234519808008749742,
    176325509039323911968355873643,
    98486971404861992487294722613
]

c = []

for i in range(-100, 101):
    for j in range(-100, 101):
        for k in range(-100, 101):
            if i * a[0] + j * a[1] + k * a[2] == 1:
                c.append([i, j, k])
                # print(i, j, k)

print(c)

for i in range(len(c)):
    g = solve(b, c[i][0], c[i][1], c[i][2])
    print(g)
