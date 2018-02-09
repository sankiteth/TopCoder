'''
http://community.topcoder.com/tc?module=Static&d1=tutorials&d2=findSolution
'''
def DistanceFromEnd(word):
    global end
    dist = 0
    pow = 0
    for i in range(4):
        dist += ( abs( ord(word[i]) - ord(end[i]) ) ) * (10**pow)
        pow += 1
    return dist

def NextValidWords(state):
    global forbid
    validWords = []
    valid = 0
    for i in range(4):
        temp = state
        if temp[i] == 'z':
            temp = temp[:i] + 'a' + temp[i+1:]
        else:
            temp = temp[:i] + chr(ord(temp[i]) + 1) + temp[i+1:]

        for string in forbid:
            valid = 0
            for j in range(4):
                if temp[j] in string[j]:
                    valid += 1
                    if valid == 4:
                        break;
            if valid == 4:
                        break;

        if valid < 4:
            validWords.append(temp)

    for i in range(4):
        temp = state
        if temp[i] == 'a':
            temp = temp[:i] + 'z' + temp[i+1:]
        else:
            temp = temp[:i] + chr(ord(temp[i]) - 1) + temp[i+1:]

        for string in forbid:
            valid = 0
            for j in range(4):
                if temp[j] in string[j]:
                    valid += 1
                    if valid == 4:
                        break;
            if valid == 4:
                        break;

        if valid < 4:
            validWords.append(temp)
    
    sortedValidWords = sorted(validWords, key = lambda word: DistanceFromEnd(word))
    return sortedValidWords

def dfs(node, res):
    global end
    global forbid
    global visited
    if node == end:
        return res
    else:
        visited.add(node)
        for i in NextValidWords(node):
            if i not in visited:
                visited.add(i)
                res = dfs(i, res+1)
        return res

if __name__ == '__main__':
    start = 'aaaa'
    end = 'zzzz'
    forbid = ["a a a z", "a a z a", "a z a a", "z a a a", "a z z z", "z a z z", "z z a z", "z z z a"]
    finalResult = 99999
    f = [[] for i in forbid]
    i = 0
    for string in forbid:
        f[i] = string.split(sep=' ')
        i += 1
    
    forbid = f
    visited = set()
    res = dfs(start, 0)
    print(res)