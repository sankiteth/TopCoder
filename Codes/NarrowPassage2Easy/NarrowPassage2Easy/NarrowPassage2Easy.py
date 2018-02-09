'''
http://apps.topcoder.com/wiki/display/tc/SRM+638
'''

def dfs(perm):
    if perm not in visited:
        visited.add(perm)
        for i in range(n-1):
            if size[perm[i]] + size[perm[i+1]] <= maxSizeSum:
                newPerm = perm[:i] + (perm[i+1],perm[i]) + perm[i+2:]
                dfs(newPerm)

if __name__ == '__main__':
    size = [2,4,6,1,3,5]
    maxSizeSum = 8
    n = len(size)
    visited = set()
    dfs(tuple(range(n)))
    perms = len(visited)
    print('Possible Permutations:')
    print(*visited,sep='\n')
    print('No. of possible permutations={0}'.format(perms))