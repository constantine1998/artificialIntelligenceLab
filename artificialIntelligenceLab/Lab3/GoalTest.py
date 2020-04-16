def goal(state):
    if(state == None):
        return False
    for i in range(6):
        if(state[i]==1):
            return False
        
    if(state[6]<0):
        return False
    return True        
