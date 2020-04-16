import copy
def cross(i,j,state_original,lamp):
    state_c = copy.deepcopy(state_original)
    if(j>i):
        person = j
    else:
        person = i
    
    if(person==1):
        state_c[6] = state_c[6]-1
    if(person==2):
        state_c[6] = state_c[6]-3
    if(person==3):
        state_c[6] = state_c[6]-6
    if(person==4):
        state_c[6] = state_c[6]-8
    if(person==5):
        state_c[6] = state_c[6]-12
    
    if(state_c[6]<0):
        return
    
    if(lamp):
        if(j != 0):
            state_c[i]=0
            state_c[j]=0
        else:
            state_c[i]=0
        state_c[0]=0
        return state_c
    
    if(not lamp):
        if(j != 0):
            state_c[i]=1
            state_c[j]=1
        else:
            state_c[i]=1
        state_c[0]=1
        return state_c
    
def moveGen(state):
    next = []
    if(state == None):
        return next
    for i in range(1,6):
        if(state[i]==state[0]):
            item = cross(i,0,state,state[0])
            if(item != None):
                next.append(item)
            for j in range(i,6):
                if(state[j]==state[0] and i!=j):
                    item = cross(i,j,state,state[0])
                    if(item != None):
                        next.append(item)
    return next