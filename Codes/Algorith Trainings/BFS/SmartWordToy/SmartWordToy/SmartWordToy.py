'''
http://community.topcoder.com/tc?module=Static&d1=tutorials&d2=findSolution
'''
from queue import Queue

def DistanceFromEnd(word, end):
    dist = 0
    for i in range(4):
        dist += abs( ord(word[i]) - ord(end[i]) )
    return dist

def NextValidWords(state, forbid, end):
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
    
    sortedValidWords = sorted(validWords, key = lambda word: DistanceFromEnd(word, end))
    return sortedValidWords

def minPresses():
    start = 'aaaa'
    end = 'zzzz'
    forbid = ["a a a z", "a a z a", "a z a a", "z a a a", "a z z z", "z a z z", "z z a z", "z z z a"]
    f = [[] for i in forbid]
    i = 0
    for string in forbid:
        f[i] = string.split(sep=' ')
        i += 1
    
    forbid = f
    queue = Queue()
    queue.put(start)
    count = 1
    res = 0
    visited = set()
    visited.add(start)

    while(not queue.empty()):
        siblings = 0
        while count > 0:
            state = queue.get()
            if state == end:
                return res
            for i in NextValidWords(state, forbid, end):
                if i not in visited:
                    queue.put(i)
                    siblings += 1
            count -= 1
        res += 1
        count = siblings

if __name__ == '__main__':
    res = minPresses()
    print(res)

