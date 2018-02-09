'''
http://apps.topcoder.com/wiki/display/tc/SRM+655
'''

def AbleToDraw(board):
    for k in range(2):
        bad = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '?':
                    if board[i][j] != ('W' if (k + i + j) % 2 != 0 else 'B'):
                        bad = True
                        break
        if not bad:
            return "Possible"
        else:
            return "Not Possible"

if __name__ == '__main__':
    board = ["W???",
             "??B?",
             "W???",
             "?B?W"]
    ret = AbleToDraw(board)
    print(ret)