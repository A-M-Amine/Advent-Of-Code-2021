def mark(x,board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if x == board[i][j]:
                board[i][j] = '-1'

def checkWin(board):

    marked = ['-1' for i in range(5)]

    for i in board:
        if i == marked:
            return board
    
    
    for i in range(len(board[0])):
        tmp = []
        for j in range(len(board)):
            tmp.append(board[j][i])
        if tmp == marked:
            return board
    
    return None

def resBoard(board,nb):
    res = 0
    for i in board:
        for j in i:
            if j != '-1':
                res += int(j)
            
    return res * int(nb)

fl = open("input4.txt").readlines()

bingolst = fl[0].strip("\n").split(',')

boards = []
stop = False
strt = 2

while not stop:

    grid = []
    end = strt + 5
    
    for strt in range(strt,end):
        grid.append(fl[strt].strip("\n").split())


    boards.append(grid)
    strt = end + 1

    if strt + 5 > len(fl):
        stop = True

found = False
winb = []
while bingolst and not found:
    nb = bingolst.pop(0)

    for board in boards:
        mark(nb, board)
        winb = checkWin(board)
        if winb != None:
            found = True
            break

print(resBoard(winb,nb))