'''
The extra spaces includes spaces put at the end of every line except the last one.  
The problem is to minimize the following total cost.
Cost of a line = (Number of extra spaces in the line)^3
Total Cost = Sum of costs for all lines
'''
def printSolution(p, n):
    if p[n] == 1:
        k = 1
    else:
        k = printSolution(p, p[n] - 1)
    print('line num {0}: From word num {1} to {2}'.format(k, p[n], n))

def main():
    l = [5, 3, 5, 8, 4, 4, 7] #l[i]=num of chars in 'i'th word
    n = len(l)
    M = 15 #Max number of chars in a line
    # extra[i][j] = num of extra spaces words 'i' to 'j' are placed in a single line
    extras = [[9 for j in range(n)] for i in range(n)]
    for i in range(n):
        extras[i][i] = M - l[i]
        for j in range(i+1, n):
            extras[i][j] = extras[i][j-1] - l[j] - 1
    print('Extras:')
    print(*extras,sep='\n')
    # lc[i][j] = cost of putting words from word 'i' to 'j' in a single line
    lc = [[None for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(i,n):
            if extras[i][j] < 0:
                lc[i][j] = INF
            #elif j == n-1 and extras[i][j] >= 0: # to not extra space cost for last line
            #    lc[i][j] = 0
            else:
                lc[i][j] = extras[i][j]**2
    print('lc:')
    print(*lc,sep='\n')
    # c[i] = cost to wrap 'i' words starting from 0th index   
    c = [INF for i in range(n+1)]
    # p[n] = num of word from which last line starts
    # p[p[n]] = num of word from which penultimate line starts
    p = [INF for i in range(n+1)]
    c[0] = 0
    for i in range(1,n+1):
        for j in range(1,i+1):
            if lc[i-1][j-1] != INF and c[i] > c[j-1] + lc[j-1][i-1]:
                c[i] = c[j-1] + lc[j-1][i-1]
                p[i] = j
    print('c:')
    print(*c,sep=',')
    print('p:')
    print(*p,sep=',')
    printSolution(p, n)

if __name__=='__main__':
    INF = 9999
    main()