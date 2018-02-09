'''
http://community.topcoder.com/stat?c=problem_statement&pm=1592&rd=4482
'''
def f(start, end, numMoves):
    global dp
    global size

    if dp[numMoves][start[0]][start[1]] != -1:
        return dp[numMoves][start[0]][start[1]]
    else:
        if numMoves == 0:
            if start == end:
                res = 1
            else:
                res = 0
        else:
            res = 0
            for nbr in Neighbours(start):
                res += f(nbr, end, numMoves-1)

        dp[numMoves][start[0]][start[1]] = res
        return res

def Neighbours(node):
    global size
    res = []
    row = col = 0
    if 0<=node[0]<size and 0<=node[1]<size:
        for i in range(2):
            if i==0:
                row = (node[0]-2)
            else:
                row = (node[0]+2)
            if 0<=row<size:
                for j in [(node[1]-1), (node[1]+1)]:
                    if 0<=j<size:
                        res.append((row, j))
            
            if i==0:
                row = (node[0]-1)
            else:
                row = (node[0]+1)
            if 0<=row<size:
                for j in range((node[1]-2), (node[1]+3), 1):
                    if 0<=j<size:
                        res.append((row, j))
            if i==0:
                row = (node[0])
                for j in [(node[1]-1), (node[1]+1)]:
                        if 0<=j<size:
                            res.append((row, j))
    return res

if __name__ == '__main__':
    size = 100
    start = (0, 0)
    end = (0, 99)
    numMoves = 50

    dp = [[[-1 for j in range(size)] for i in range(size)] for k in range(numMoves+1)]

    res = f(start, end, numMoves)
    print("Total num of ways = {0}".format(res))