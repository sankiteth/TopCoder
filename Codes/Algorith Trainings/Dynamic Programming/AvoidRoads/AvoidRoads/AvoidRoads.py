'''
http://community.topcoder.com/stat?c=problem_statement&pm=1889&rd=4709
'''

def Neighbours(node):
    '''
    We only need to go up because minimum num of moves to reach from 
    (0,0) to (width,height) is {width+height}
    '''
    global width
    global height
    res = []
    if 0<=node[0]<=width:
        #if 0<=(node[1]-1)<=height:
        #    res.append((node[0], node[1]-1))
        if 0<=(node[1]+1)<=height:
            res.append((node[0], node[1]+1))

    if 0<=node[1]<=height:
        #if 0<=(node[0]-1)<=width:
        #    res.append((node[0]-1, node[1]))
        if 0<=(node[0]+1)<=width:
            res.append((node[0]+1, node[1]))

    return res

def f(start, end, num):
    global avoid
    global visited
    if dp[num][start[1]][start[0]] != -1:
        return dp[num][start[1]][start[0]]
    else:
        if num == 0:
            if start == end:
                res = 1
            else:
                res = 0
        else:
            res = 0
            for nbr in Neighbours(start):
                if ((nbr, start) not in avoid) and ((start, nbr) not in avoid) and (nbr not in visited):
                    visited.add(nbr)
                    res += f(nbr, end, num-1)
                    visited.remove(nbr)

        dp[num][start[1]][start[0]] = res
        return res

if __name__ == '__main__':
    width = 35
    height = 31
    bad = []
    start = (0,0)
    end = (width,height)
    num = width+height
    avoid = set()
    visited = set()

    for i in bad:
        t1 = (int(i[0]), int(i[2]))
        t2 = (int(i[4]), int(i[6]))
        avoid.add((t1, t2))
    dp = [[[-1 for j in range(width+1)] for i in range(height+1)] for k in range(num+1)]
    
    visited.add(start)
    res = f(start, end, num)
    print("Total num of ways = {0}".format(res))

