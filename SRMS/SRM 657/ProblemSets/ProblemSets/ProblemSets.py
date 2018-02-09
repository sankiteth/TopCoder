'''
http://community.topcoder.com/stat?c=problem_statement&pm=13771
'''

if __name__ == '__main__':
    E, EM, M, MH, H = 657, 657, 657, 657, 657
    minim = min(E, M, H)
    partialRes = 0
    if minim > 0:
        partialRes = minim
        E -= minim
        M -= minim
        H -= minim

    res = -1
    for a in range(0, EM+1):
        for b in range(0, MH+1):
            easy = E + EM - a
            medium = M + a + b
            hard = H + MH - b
            curRes = min(easy, medium, hard)
            res = max(res, curRes)
    print(res + partialRes)