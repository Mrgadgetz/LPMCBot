TICTACTOE = ["_","_","_","_","_","_","_","_","_"]

def tttWinCheck():
    winner = 0
    if ((TICTACTOE[0] == TICTACTOE[1]) and (TICTACTOE[1] == TICTACTOE[2]) 
        and (TICTACTOE[2] != '_')):winner = TICTACTOE[0] 
    elif ((TICTACTOE[3] == TICTACTOE[4]) and (TICTACTOE[4] == TICTACTOE[5]) 
        and (TICTACTOE[5] != '_')):winner = TICTACTOE[3] 
    elif ((TICTACTOE[6] == TICTACTOE[7]) and (TICTACTOE[7] == TICTACTOE[8]) 
        and (TICTACTOE[8] != '_')):winner = TICTACTOE[6] 
    elif ((TICTACTOE[0] == TICTACTOE[3]) and (TICTACTOE[3] == TICTACTOE[6]) 
        and (TICTACTOE[6] != '_')):winner = TICTACTOE[0] 
    elif ((TICTACTOE[1] == TICTACTOE[4]) and (TICTACTOE[4] == TICTACTOE[7]) 
        and (TICTACTOE[7] != '_')):winner = TICTACTOE[1] 
    elif ((TICTACTOE[2] == TICTACTOE[5]) and (TICTACTOE[5] == TICTACTOE[8]) 
        and (TICTACTOE[8] != '_')):winner = TICTACTOE[2] 
    elif ((TICTACTOE[0] == TICTACTOE[4]) and (TICTACTOE[4] == TICTACTOE[8]) 
        and (TICTACTOE[8] != '_')):winner = TICTACTOE[0] 
    elif ((TICTACTOE[2] == TICTACTOE[4]) and (TICTACTOE[4] == TICTACTOE[6]) 
        and (TICTACTOE[6] != '_')):winner = TICTACTOE[2] 
    return winner
    
def tttAI():
    #Gave the AI the potential to lose so it can be fun, but is still decent.
    #Returns the numeric value [1-9] of the move it wants to make
    #based on 1 = top left & 9 = bottom right moving left to right & top to bottom
    win = tttWin()
    if (win != -1):
        return win
    center = tttCenter()
    if (center != -1):
        return center
    corner = tttCorner()
    if (corner != -1):
        return corner
    else:
        return tttEdge()

def tttWin():
    #Checks for win conditions in the upcoming move (Either for the AI or the player)
    #and if so, moves to win or block the win, respectively
    
    #Defines starting positions for all possible win scenarios
    startingPoints = [[0,3,6],[0,1,2],[0,2,6,8]]
    for outerCount in startingPoints:
        for innerCount in outerCount:
            #The diagonal scenarios
            if (4 == len(outerCount)):
                if (TICTACTOE[4] == TICTACTOE[innerCount] and 0 == innerCount and "_" == TICTACTOE[8] and "_" != TICTACTOE[4]):
                    return 9
                if (TICTACTOE[4] == TICTACTOE[innerCount] and 2 == innerCount and "_" == TICTACTOE[6] and "_" != TICTACTOE[4]):
                    return 7
                if (TICTACTOE[4] == TICTACTOE[innerCount] and 6 == innerCount and "_" == TICTACTOE[2] and "_" != TICTACTOE[4]):
                    return 3
                if (TICTACTOE[4] == TICTACTOE[innerCount] and 8 == innerCount and "_" == TICTACTOE[0] and "_" != TICTACTOE[4]):
                    return 1
            #The vertical and horizontal scenarios
            else:
                #The horizontal scenarios
                if (3 == outerCount[1]): 
                    if (TICTACTOE[innerCount] == TICTACTOE[innerCount+1] and "_" != TICTACTOE[innerCount] and "_" == TICTACTOE[innerCount+2]):
                        return innerCount+3
                    if (TICTACTOE[innerCount+1] == TICTACTOE[innerCount+2] and "_" != TICTACTOE[innerCount+1] and "_" == TICTACTOE[innerCount]):
                        return innerCount+1
                    if (TICTACTOE[innerCount] == TICTACTOE[innerCount+2] and "_" != TICTACTOE[innerCount] and "_" == TICTACTOE[innerCount+1]):
                        return innerCount+2
                #The vertical scenarios
                if (1 == outerCount[1]):
                    if (TICTACTOE[innerCount] == TICTACTOE[innerCount+3] and "_" != TICTACTOE[innerCount] and "_" == TICTACTOE[innerCount+6]):
                        return innerCount+7
                    if (TICTACTOE[innerCount+3] == TICTACTOE[innerCount+6] and "_" != TICTACTOE[innerCount+3] and "_" == TICTACTOE[innerCount]):
                        return innerCount+1
                    if (TICTACTOE[innerCount] == TICTACTOE[innerCount+6] and "_" != TICTACTOE[innerCount] and "_" == TICTACTOE[innerCount+3]):
                        return innerCount+4
    return -1
    
def tttCenter():
    #Returns the center square
    if ("_" == TICTACTOE[4]):
        return 5
    else:
        return -1

def tttCorner():
    #Returns an open corner
    checkList = [0,2,6,8]
    for check in checkList:
        if ("_" == TICTACTOE[check]):
            return check+1
    return -1
    
def tttEdge():
    #Returns an open edge
    checkList = [1,3,5,7]
    for check in checkList:
        if ("_" == TICTACTOE[check]):
            return check+1
    return -1
    