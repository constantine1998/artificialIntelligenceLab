import GoalTest as gt
import MoveGen as mg
import reConstruct as rc
import heuristics as h
import Queue
from operator import itemgetter
import copy

raw_input("Press any key to start solving\n")

state = [1,1,1,1,1,1,30]

L = Queue.Queue()
pat_len_bfs = 0
close_bfs=[]
pair_bfs = []
state_explored_bfs = 0
length_track = 0
f=0
g=0

pair_hc = []
state_explored_hc = 0


def BFS(state):
    global L
    global f
    global g
    global close_bfs
    global pat_len_bfs
    global pair_bfs
    global state_explored_bfs
    global length_track
    if(gt.goal(state[1])):
        print("Found a solution(BestFS)!")
        rc.reConstruct(state,pair_bfs,[])
        return
    branch = mg.moveGen(state[1])
    add = len(branch)
    ready_sort =[]
    for cub in branch:
        n = h.h3(cub)
        temp = (cub,n)
        ready_sort.append(temp)
    sorted_branch = sorted(ready_sort, key = itemgetter(1))
    sorted_branch = sorted_branch[::-1]
    for node in sorted_branch or []:
        if node[0] in close_bfs:
            add = add -1
        else:
            temp = (state[1],node[0])
            L.put(temp)
            pair_bfs.append(temp)        
    close_bfs =  close_bfs + branch
    if((length_track%2) == 0):
        f = f+add
    else:
        g = g+add
    state_explored_bfs = state_explored_bfs+add
    if(L.empty()):
        print("No solution can be found for the starting configuration.\n Closest we could reach is -")
        rc.reConstruct(state, pair_bfs)
        return
    
    if((g==0 or f==0) and not (add==0)):
        length_track = length_track+1
    state = L.get()
    
    if((length_track%2) == 1):
        f = f-1
    else:
        g = g-1
    if(f<0):
        g = g-1
        f = f+1
        length_track = length_track+1
    if(g<0):
        g = g+1
        f = f-1
        length_track = length_track+1
    BFS(state)
    
def HC(state):
    global pair_hc
    global state_explored_hc
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
    
    ready_sort =[]
    for cub in branch:
        n = h.h3(cub)
        temp = (cub,n)
        ready_sort.append(temp)
    sorted_branch = sorted(ready_sort, key = itemgetter(1))
    sorted_branch = sorted_branch[::-1]
    first = ()
    i = 1
    for node in sorted_branch or []:
        temp = (state[1],node[0])
        if(i==1):
            first = copy.deepcopy(temp)
        pair_hc.append(temp)
        i=2
            
    state_explored_hc = state_explored_hc+add
    return HC(first)


start=(None,state)

pair_bfs.append((None,state))
BFS(start)

pair_hc.append((None,state))
HC(start)

print("\n")
print("Length of path(BestFS): "+str(length_track))
print("Number of states explored(BestFS): "+str(state_explored_bfs))
print("\n")

print("Number of states explored(HC): "+str(state_explored_hc))
print("\n")