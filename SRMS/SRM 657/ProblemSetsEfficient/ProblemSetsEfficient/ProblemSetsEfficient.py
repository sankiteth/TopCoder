'''
http://community.topcoder.com/stat?c=problem_statement&pm=13771
'''

def IsAllowed(E,EM,M,MH,H,med):
    if med > E + EM:
        return False
    if med > MH + H:
        return False
    maxA = min(E + EM - med, EM)
    maxB = min(MH + H - med, MH)
    return (M + maxA + maxB >= med)

if __name__ == '__main__':
    E, EM, M, MH, H = 2, 2, 1, 2, 2
    minim = min(E, M, H)
    partialRes = 0
    if minim > 0:
        partialRes = minim
        E -= minim
        M -= minim
        H -= minim
    #Now one of (E,M,H) is 0
    low = 0
    high = EM + MH + 1
    while(low + 1 < high):
        med = (low + high) // 2
        if IsAllowed(E,EM,M,MH,H,med) :
            low = med
        else:
            high = med

    print(low + partialRes)