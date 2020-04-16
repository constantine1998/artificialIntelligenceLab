import GoalTest as gt
import MoveGen as mg
import reConstruct as rc
import heuristics as h
from operator import itemgetter
import copy
from collections import deque
from cgi import maxlen

raw_input("Press any key to start solving\n")

state = [1,1,1,1,1,1,30]

L = deque([[1,1,1,1,1,1,30],[1,1,1,1,1,1,30],[1,1,1,1,1,1,30],[1,1,1,1,1,1,30],[1,1,1,1,1,1,30],[1,1,1,1,1,1,30]],maxlen = 6)
pair_hc = []
state_explored_hc = 0
    
def TS(state):
    global L
    global pair_hc
    global state_explored_hc
    if(len(L)<4):
        print("poping")
        L.rotate()
        L.pop()
    if(gt.goal(state[1])):
        print("Found a solution(HC)!")
        rc.reConstruct(state,pair_hc,[])
        return
    
    branch = mg.moveGen(state[1])
    add = len(branch)
    if(not branch):
        print("\n(HC) Can't reach the solution.\n Closest we could reach is -")
        rc.reConstruct(state, pair_hc,[])
        return
    L.append(state[1])
    ready_sort =[]
    for cub in branch:
        n = h.h3(cub)
        temp = (cub,n)
        ready_sort.append(temp)
        
    sorted_branch = sorted(ready_sort, key = itemgetter(1))
    sorted_branch = sorted_branch[::-1]
    
    first = ()
    i = 1
    j = 1
    for node in sorted_branch or []:
        temp = (state[1],node[0])
        if(i==j):
            if node[0] not in L:
                first = copy.deepcopy(temp)
            else:
                j=j+1
        pair_hc.append(temp)
        i=i+1    
    state_explored_hc = state_explored_hc+add
    return TS(first)


start=(None,state)

pair_hc.append((None,state))
TS(start)


print("Number of states explored(HC): "+str(state_explored_hc))
print("\n")