def goal(config,n):
    row = 0;
    for i in range(n):
        for j in range(n):
            if(config[i,j]==1):
                row=row+1
                continue;
    if(row!=n):
        return False
    return True
