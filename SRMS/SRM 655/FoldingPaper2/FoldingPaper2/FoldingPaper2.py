'''
http://apps.topcoder.com/wiki/display/tc/SRM+655
'''

def fold(big, small):
    global INF
    '''
    fold big to small
    '''
    if small > big:
        return INF
    elif small == big:
        return 0
    else:
        return 1 + fold(big - min(big/2, big - small), small)

if __name__ == '__main__':
    W = 127
    H = 129
    A = 72
    INF = 999999

    res = INF
    for w in range(1,A+1):
        if (A % w) == 0:
            h = A/w
            res = min(res, fold(W, w) + fold(H, h) )
    if res >= INF:
        print(-1)
    else:
        print(res)