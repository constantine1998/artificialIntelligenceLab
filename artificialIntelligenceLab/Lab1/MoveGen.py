import copy
def placeQ(config,row,col,n):
    #Check this row on left side
    for i in range(row):
        if (config[i][col]):
            return False
    #Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if (config[i][j]):
            return False
    #Check lower diagonal on left side
    for i, j in zip(range(row,-1, -1), range(col, n)):
        if (config[i][j]):
            return False
    for i in range(n):
        if(config[row][i]):
            return False
    return True

def moveGen(config,n):
    row = 0;
    for i in range(n):
        for j in range(n):
            if(config[i,j]==1):
                row=row+1
                continue;
    branch = []
    for i in range(n):
        #Check if queen can be placed on board[i][col]
        if (placeQ(config, row, i,n)):
            #Place this queen in board[i][col]
            config2 = copy.deepcopy(config)
            config2[row][i] = 1;
            branch.append(config2)
    return branch
