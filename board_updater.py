#board_updater code

# This code compares old master.py position to new
# position of 8x8 array of black and white pieces

# INPUT: 2 8X8 arrays of W, B, or - (prev. and new board arrays)



def updateBoard(oldboard,newboard):
    white2black = 0
    black2space = 0 #note: we're only considered with computer moves and 
    space2black = 0 #      the computer always plays black
    white2space = 0 # only possible for en passent scenario 
    for i in range(0,8): # doesn't include 8
        for j in range(0,8):
            if oldboard[i][j] != newboard[i][j]:
                if oldboard[i][j] == '-' and newboard[i][j] == 'B':
                    space2black += 1
                elif oldboard[i][j] == 'W' and newboard[i][j] == 'B':
                    white2black += 1
                elif oldboard[i][j] == 'B' and newboard[i][j] == '-':
                    black2space += 1
                elif oldboard[i][j] == 'W' and newboard[i][j] == '-':
                    white2space += 1
                else:
                    print("ERROR-UNKNOWN BOARD PIECE")

    if space2black == 1 and black2space == 1 and white2space == 0 and white2black == 0:
        print('simple move')
    elif space2black == 0 and black2space == 1 and white2space == 0 and white2black == 1:
        print('capture')
    elif space2black == 2 and black2space == 2 and white2space == 0 and white2black == 0:
        print('castling') # ***send K or Q to indicate king- or queenside castling
    elif space2black == 1 and black2space == 1 and white2space == 1 and white2black == 0:
        print('en passent')
    else:
        print("ERROR-MOVE UNKNOWN")
