'''
Count the number of ways we can parenthesize the expression so that the value of 
expression evaluates to true.
'''
def main():
    sym = 'TTFT'
    op = '|&^'
    n = len(sym)
    tr = [[0 for i in range(n)] for i in range(n)]
    fl = [[0 for i in range(n)] for i in range(n)]
    for i in range(n):
        tr[i][i] = 1 if sym[i] == 'T' else 0
        fl[i][i] = 1 if sym[i] == 'F' else 0
    for l in range(2,n+1):
        for i in range(n-l+1):
            j = i+l-1
            for k in range(i,j):
                if op[k] == '&':
                    tr[i][j] = tr[i][j] + (tr[i][k]*tr[k+1][j])
                    fl[i][j] = fl[i][j] + (fl[i][k]*fl[k+1][j] + 
                                           fl[i][k]*tr[k+1][j] +
                                           tr[i][k]*fl[k+1][j])
                elif op[k] == '|':
                    tr[i][j] = tr[i][j] + (tr[i][k]*tr[k+1][j] + 
                                           tr[i][k]*fl[k+1][j] +
                                           fl[i][k]*tr[k+1][j])
                    fl[i][j] = fl[i][j] + (fl[i][k]*fl[k+1][j])
                elif op[k] == '^':
                    tr[i][j] = tr[i][j] + (tr[i][k]*fl[k+1][j] +
                                           fl[i][k]*tr[k+1][j])
                    fl[i][j] = fl[i][j] + (tr[i][k]*tr[k+1][j] +
                                           fl[i][k]*fl[k+1][j])
    print('True:')
    print(*tr,sep='\n')
    print('False:')
    print(*fl,sep='\n')
    print('Possible no. of ways = {0}'.format(tr[0][n-1]))


if __name__=='__main__':
    main()