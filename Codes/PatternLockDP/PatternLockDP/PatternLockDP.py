'''
This problem is about a pattern lock similar to the one used on Android devices.

On the screen there is a set of nodes, placed onto vertices of a rectangular grid. (Android devices usually use a 3 times 3 grid, but we will use grids of different dimensions in this problem.) We will assign Cartesian coordinates to the nodes, starting with (0,0) in a corner.

To unlock the device, the user has to draw the correct pattern: a path that connects some of the nodes. Below we describe the properties of a valid pattern.

The pattern is a sequence of nodes.
There must be at least one node in the pattern.
Each node may only appear in the pattern at most once.
For any two consecutive nodes A and B in the pattern, each other node that lies on the straight line segment AB must occur in the pattern before A and B.
According to the last rule, (0,1)-(0,0)-(0,2) is a valid pattern: the segment (0,0)-(0,2) does contain another node (0,1) but that node was already used in the pattern. On the other hand, no valid pattern can start with the nodes (0,0) and (0,2).

You are given ints N and MOD. Alice's device has a grid of 2 times N nodes. (That is, the nodes have coordinates between (0,0) and (1,N-1), inclusive.) Alice wants to choose a pattern of length 2*N (i.e., the longest possible pattern). Let X be the number of different patterns she may choose. Return the value (X modulo MOD).
'''

def f(x, y):  
    '''
    x, y => the two rows
    '''  
    if  dp[x][y] != -1:
        return dp[x][y]
    else:
        if x == 0:
            if y == 0:
                res = 1
            else:
                res = 0
        else:
            a = (x * f(y, x-1)) % MOD
            b = ((2 * f(x - 1, y)) % MOD) if x > 1 else 0
            res = (a + b) % MOD
        dp[x][y] = res
        return res

def main():
    '''
    For x>1:
    f(x,y)=xf(y,x?1)+2f(x?1,y)
    '''
    numPaths = (2*f(N, N)) % MOD
    print('Finally dp:')
    print(*dp,sep='\n')
    print('Num of possible patterns={0}'.format(numPaths))

if __name__=='__main__':
    N = 3
    MOD = 1000000007
    dp = [[-1 for i in range(N+1)] for i in range(N+1)]
    main()