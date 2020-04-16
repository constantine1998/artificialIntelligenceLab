import GoalTest as gt
import MoveGen as mg
import numpy as np
import Queue

n = int(input("Input size of the board(n):\n(should be greater than 3\n)"))
x = int(input("Input the initial queen position in the first row:\n(remember that counting starts from zero and ends at 'n-1')\n"))
config = np.array([[0]*n]*n)
config[0,x] = 1

L = Queue.Queue()
pat_len_bfs = 0
state_explored_bfs = 0
length_track = 0
f=0
g=0

M = Queue.LifoQueue()
pat_len_dfs = 0
state_explored_dfs = 0

N = Queue.LifoQueue()
pat_len_dbdfs = 0
state_explored_dbdfs = 0
depth_track = Queue.LifoQueue()

bound = 1

def BFS(config,n):
    global L
    global f
    global g
    global pat_len_bfs
    global state_explored_bfs
    global length_track
    if(gt.goal(config, n)):
        print("Found a solution(BFS)!")
        print(config)
        print("\n")
        return
    branch = mg.moveGen(config, n)
    state_explored_bfs = state_explored_bfs+len(branch)
    for node in branch or []:
        L.put(node)
    
    if((length_track%2) == 0):
        f = f+len(branch)
    else:
        g = g+len(branch)
    if(L.empty()):
        print("No solution can be found for the starting configuration.\n Closest we could reach is -")
        print(config)
        print("\n")
        return
    if((g==0 or f==0) and not (len(branch)==0)):
        length_track = length_track+1
    config = L.get()
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
    BFS(config, n)

def DFS(config,n):
    global M
    global pat_len_dfs
    global state_explored_dfs
    if(gt.goal(config, n)):
        print("Found a solution(DFS)!")
        print(config)
        print("\n")
        return
    branch = mg.moveGen(config, n)
    state_explored_dfs = state_explored_dfs+len(branch)
    for node in branch or []:
        M.put(node)
    if(M.empty()):
        print("No solution can be found for the starting configuration.\n Closest we could reach is -")
        print(config)
        print("\n")
        return
    config = M.get()
    pat_len_dfs = pat_len_dfs+1
    DFS(config, n)
    
def DBDFS(config,n,d_bound):
    global N
    global pat_len_dbdfs
    global state_explored_dbdfs
    global depth_track
    if(gt.goal(config, n)):
        print("Found a solution(DIFD)")
        print(config)
        print("\n")
        return True
    if(d_bound<=0):
        child = depth_track.get()
        if(np.array_equal(child, config)):
            d_bound = d_bound+1
        depth_track.put(child)
    if(N.empty()):
        return False
    config = N.get()
    if(d_bound>0):
        branch = mg.moveGen(config, n)
        state_explored_dbdfs = state_explored_dbdfs+len(branch)
        for node in branch or []:
            N.put(node)
        if(len(branch)>0):
            depth_track.put(branch[0])
    pat_len_dbdfs = pat_len_dbdfs+1
    d_bound = d_bound -1
    return DBDFS(config, n,d_bound)
    
def DFID(config,n):
    global bound
    global pat_len_dbdfs
    global state_explored_dbdfs
    global N
    global depth_track
    while((not DBDFS(config,n,bound)) and bound <= 100):
        bound = bound+1
        pat_len_dbdfs = 0
        state_explored_dbdfs = 0
        while(not N.empty()):
            N.get()
        while(not depth_track.empty()):
            depth_track.get()
        N.put(config)
N.put(config)
BFS(config,n)
DFS(config,n)
DFID(config, n)
print("Length of path(BFS): "+str(length_track))
print("Number of states explored(BFS): "+str(state_explored_bfs))
print("\n")
print("Length of path(DFS): "+str(pat_len_dfs))
print("Number of states explored(DFS): "+str(state_explored_dfs))
print("\n")
if(not bound>100):
    print("Had to go to "+str(bound)+" depth.")
    print("Number of states explored(DFID): "+str(state_explored_dbdfs))
else:
    print("Solution couldn't be found under 100 depth.")

    
    