'''
http://apps.topcoder.com/wiki/display/tc/SRM+657
'''

def SolveModEq(divisor):
    '''
    solves ax**2 + bx + c = 0 (mod divisor)
    '''
    global a, b, c
    for x in range(divisor):
        A = (a * (x**2 % divisor) ) % divisor
        B = (b * x) % divisor
        C = c
        if ((A + B + C) % divisor) == 0:
            return x
    return -1

if __name__ == '__main__':
    a = 479659453
    b = 928595613
    c = 143451144

    n = 10**9 # 1 billion
    p = 2**9
    q = 5**9 # n = pq such that GCD(p, q) = 1

    x2 = SolveModEq(p)
    x5 = SolveModEq(q)

    if (x2 == -1 or x5 == -1):
        print(-1)
    else:
        # try all value of x = x5 (mod 5**9). Only 2**9 such values
        x = x5
        while (x % p) != x2: # solution guranteed as GCD(p, q) = 1
            x += q
        print(x)