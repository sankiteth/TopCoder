'''
http://community.topcoder.com/stat?c=problem_statement&pm=13698
'''

def dfs(start, end, blocked, visited):
    global graph, N
    if blocked[start] == True:
        return False
    else:
        visited[start] = True
        if start == end:
            blocked[start] = True
            return True
        else:
            ret = False
            for nbr in graph[start]:
                if visited[nbr] == False and blocked[nbr] == False:
                    ret |= dfs(nbr, end, blocked, visited)
            return ret


def CheckValid(perm):
    global N, s
    blocked = [False for i in range(N)]
    count = 0
    for node in perm:
        visited = [False for i in range(N)]
        ret = dfs(s, node, blocked, visited)
        if ret == True:
            count += 1
        else:
            return False
    if count == N:
        return True
    else:
        return False

def AllPerms(arr, k, n):
    if k == n:
        perms.append(arr)
    else:
        for i in range(k,n+1,1):
            arr[i], arr[k] = arr[k], arr[i]
            AllPerms(arr[:], k+1, n)
            arr[i], arr[k] = arr[k], arr[i]

if __name__ == '__main__':
    perms = []
    a = [7, 4, 1, 0, 1, 1, 6, 0]
    b = [6, 6, 2, 5, 0, 3, 8, 4]
    s = 4
    N = len(a) + 1
    arr = [i for i in range(N)]
    AllPerms(arr, 0, N-1)
    #print(*perms, sep='\n')
    graph = [[] for i in range(N)]
    for i in range(N-1):
        graph[a[i]].append(b[i])
        graph[b[i]].append(a[i])
    
    res = 0
    for perm in perms:
        ret = CheckValid(perm)
        if ret == True:
            res += 1

    print(res)
        