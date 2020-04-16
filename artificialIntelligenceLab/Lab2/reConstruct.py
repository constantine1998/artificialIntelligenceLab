import copy
def reConstruct(state,pair_set,path):
    if(state[0]==None):
        path.append(state[1])
        for i in reversed(path):
            print(i)
        return
    path.append(state[1])
    for pair in pair_set:
        if(pair[1]==state[0]):
            state = copy.deepcopy(pair)
            break
    return reConstruct(state, pair_set,path)