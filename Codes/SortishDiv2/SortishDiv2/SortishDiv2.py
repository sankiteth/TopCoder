'''
http://apps.topcoder.com/wiki/display/tc/SRM+636
'''
def getSortedness(seq):
    s = 0
    for i in range(n):
        for j in range(i):
            if seq[j] < seq[i]:
                s += 1
    return s

def backTrack(x):
    global total
    global seq
    global used
    if x == n:
        if getSortedness(seq) == sortedness:
            total += 1
    else:
        if seq[x] == 0:
            for i in range(1, n+1):
                if used[i] == False:
                    seq[x] = i
                    used[i] = True
                    backTrack(x+1)
                    seq[x] = 0
                    used[i] = False
        else:
            backTrack(x+1)

if __name__ == '__main__':
    sortedness = 2
    seq = [1, 2, 0, 5, 0, 0]
    n = len(seq)
    used = [True if i in seq else False for i in range(n+1)]
    total = 0
    backTrack(0)
    print(total)
