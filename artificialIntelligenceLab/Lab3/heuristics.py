def h1(state):
    n = 0
    if(state[1]==1):
        n = n-1
    else:
        n = n+1.
    if(state[2]==1):
        n = n-3
    else:
        n = n+3
    if(state[3]==1):
        n = n-6
    else:
        n = n+6
    if(state[4]==1):
        n = n-8
    else:
        n = n+8
    if(state[5]==1):
        n = n-12
    else:
        n = n+12
    return n
        
def h2(state):
    n = 0
    if(state[1]==1):
        n = n-1
    else:
        n = n+1.
    if(state[2]==1):
        n = n-3
    else:
        n = n+3
    if(state[3]==1):
        n = n-6
    else:
        n = n+6
    if(state[4]==1):
        n = n-8
    else:
        n = n+8
    if(state[5]==1):
        n = n-12
    else:
        n = n+12
    if(state[5]==0 or state[3]==0 and (state[2]==1 or state[1]==1) and state[6]>11):
        n = n-40
    if(state[5]==1 and state[6]<20):
        n = n-40
    return n
        
def h3(state):
    n = 0
    if(state[0]==0 and state[1]==1 and state[2]==1):
        n = n - 30
    if(state[0]==1 and (state[1]==1 or state[2]==1) and state[6]<10):
        n=n+10
    if(state[6]<18):
        if(state[1]==1):
            n = n-1
        else:
            n = n+1.
        if(state[2]==1):
            n = n-3
        else:
            n = n+3
        if(state[3]==1):
            n = n-6
        else:
            n = n+6
        if(state[4]==1):
            n = n-16
        else:
            n = n+16
        if(state[5]==1):
            n = n-24
        else:
            n = n+24
    
    else:
        if(state[1]==1):
            n = n-1
        else:
            n = n+1.
        if(state[2]==1):
            n = n-3
        else:
            n = n+3
        if(state[3]==1):
            n = n-6
        else:
            n = n+6
        if(state[4]==1):
            n = n-8
        else:
            n = n+8
        if(state[5]==1):
            n = n-12
        else:
            n = n+12
            
    if(state[5]==0 or state[4]==0 or state[3]==0 and (state[2]==1 or state[1]==1) and state[6]>17):
        n = n-40
    if(state[5]==1 and state[6]<20):
        n = n-40
    return n
    