def decrypt(e, n, c, padding, k):
    mod_n = Zmod(n)
    binary_padding = ''.join(['{0:08b}'.format(ord(x)) for x in padding])
    
    for m_len in range(k + 1):
        P.<M> = mod_n[]

        polynomial = ((int(binary_padding, 2) << m_len) + M) ^ e - c
        polynomial_deg = polynomial.degree()

        m = ceil(8 / polynomial_deg)
        X = ceil(n ** ((1 / polynomial_deg) - 1 / 8))
        
        nn = polynomial_deg * m
        polZ = polynomial.change_ring(ZZ)
        x = polZ.parent().gen()

        gg = []
        for i in range(m):
            for j in range(polynomial_deg):
                gg.append((x * X) ** j * n ** (m - i) * polZ(x * X) ** i)
        
        BB = Matrix(ZZ, nn)

        for i in range(nn):
            for j in range(i+1):
                BB[i, j] = gg[i][j]
        
        BB = BB.LLL()

        new_polynomial = 0
        for i in range(nn):
            new_polynomial += x ** i * BB[0, i] / X ** i
        
        potential_roots = new_polynomial.roots()
        
        roots = []
        for root in potential_roots:
            if root[0].is_integer():
                result = polZ(ZZ(root[0]))
                if gcd(n, result) >= n:
                    roots.append(ZZ(root[0]))
        
        if roots:
            root_binary = '{0:b}'.format(roots[0])
            extra_zeroes = 8 - len(root_binary) % 8
            root_binary = '0' * extra_zeroes + root_binary

            pswd = ''.join([chr(int(root_binary[i : i + 8], 2)) for i in range(0, len(root_binary), 8)])
            
            return root_binary, pswd

e = 5
n = 84364443735725034864402554533826279174703893439763343343863260342756678609216895093779263028809246505955647572176682669445270008816481771701417554768871285020442403001649254405058303439906229201909599348669565697534331652019516409514800265887388539283381053937433496994442146419682027649079704982600857517093
c = 62098468639233012676976405999623683626540214106488100336260629661806980099752799017741880607632022761476870262175900576821008409520616379997122004047049203452743794261486989240546799061566297852855160632887678567353029528725691247154366623742979496705996536518541897541584045561110280917407433898271786043512

root_binary, pswd = decrypt(e, n, c, '3Miners1Course: This door has RSA encryption with exponent 5 and the password is ', 300)

print('Password in binary: ', root_binary)
print(f"Final password is '{pswd}'")
