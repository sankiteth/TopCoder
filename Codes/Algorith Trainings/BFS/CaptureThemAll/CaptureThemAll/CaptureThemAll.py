'''
http://community.topcoder.com/tc?module=Static&d1=tutorials&d2=findSolution
'''
from queue import Queue
def KnightValidNextMoves(pos):
    movesList = []
    r, c = pos[0], pos[1]
    if r-2 > 0:
        if c-1 > 0:
            movesList.append((r-2, c-1))
        if c+1 < 9:
            movesList.append((r-2, c+1))
    if r-1 > 0:
        if c-2 > 0:
            movesList.append((r-1, c-2))
        if c+2 < 9:
            movesList.append((r-1, c+2))
    if r+1 < 8:
        if c-2 > 0:
            movesList.append((r+1, c-2))
        if c+2 < 9:
            movesList.append((r+1, c+2))
    if r+2 < 9:
        if c-1 > 0:
            movesList.append((r+2, c-1))
        if c+1 < 9:
            movesList.append((r+2, c+1))
    return movesList

def FastKnight():
    knight = 'h8'
    rook = 'e2'
    queen = 'd2'
    rowK = ord(knight[0]) - ord('a') + 1
    rowR = ord(rook[0]) - ord('a') + 1
    rowQ = ord(queen[0]) - ord('a') + 1
    colK = int(knight[1])
    colR = int(rook[1])
    colQ = int(queen[1])

    knight = [(rowK, colK), False, False]
    rook = (rowR, colR)
    queen = (rowQ, colQ)

    queue = Queue()
    queue.put(knight)

    count = 1
    res = 0

    while(not queue.empty()):
        siblings = 0
        while count != 0:
            pos = queue.get()
            if pos[1] == True and pos[2] == True:
                return res

            for i in KnightValidNextMoves(pos[0]):
                node = [i, False, False]
                if i == rook:
                    node[1] = True
                elif i == queen:
                    node[2] = True

                if pos[1] == True:
                    node[1] = True
                if pos[2] == True:
                    node[2] = True
                queue.put(node)
                siblings += 1
            count -= 1
        res += 1
        count = siblings

if __name__ == '__main__':
    res = FastKnight()
    print(res)

             

    
