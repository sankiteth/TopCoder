'''
http://community.topcoder.com/stat?c=problem_statement&pm=13719
'''

def Neighbours(row, col):
    global rows, cols
    ret = []
    if 0 <= row < rows:
        if 0 <= col - 1 < cols:
            ret.append((row, col - 1))
        if 0 <= col + 1 < cols:
            ret.append((row, col + 1))
    if 0 <= col < cols:
        if 0 <= row - 1 < rows:
            ret.append((row - 1, col))
        if 0 <= row + 1 < rows:
            ret.append((row + 1, col))
    return ret

def dfs(board, visited, row, col, result):
    global rows, cols
    if not visited[row][col]:
        visited[row][col] = True
        nbrs = Neighbours(row, col)
        allBlack = True
        allWhite = True
        hasBlack = False
        hasWhite = False
        hasQuestion = False
        for nbr in nbrs:
            if board[nbr[0]][nbr[1]] == '?':
                hasQuestion = True
            elif board[nbr[0]][nbr[1]] == 'B':
                hasBlack = True
                allWhite = False
            else:
                hasWhite = True
                allBlack = False

        if board[row][col] == '?':
            if allWhite:
                board[row][col] = 'B'
            elif allBlack:
                board[row][col] = 'W'
            else:
                return "Not Possible"

        else:
            if board[row][col] == 'B' and hasBlack:
                return "Not Possible"
            if board[row][col] == 'W' and hasWhite:
                return "Not Possible"

        for nbr in nbrs:
            res = ''
            if not visited[nbr[0]][nbr[1]]:
                res = dfs(board, visited, nbr[0], nbr[1], "Possible")
                if res == "Not Possible":
                    return res
        return "Possible"
    else:
        return result

def f(board, visited):
    return dfs(board, visited, 0, 0, "Possible")

if __name__ == '__main__':
    board = ["W???",
             "??B?",
             "W???",
             "?B?W"]
    newBoard = []
    index = 0
    for string in board:
        newBoard.append([])
        for char in string:
            newBoard[index].append(char)
        index += 1
    board = newBoard

    rows = len(board)
    cols = len(board[0])
    visited = [[False for j in range(cols) ] for i in range(rows)]
    ret = f(board, visited)
    print(ret)
    print(*board, sep='\n')