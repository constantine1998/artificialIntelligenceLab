import GoalTest as gt
import MoveGen as mg
import reConstruct as rc
import Queue

M = Queue.LifoQueue()
pat_len_dfs = 0
state_explored_dfs = 0
close_dfs = []

def DFS(config):
    global M
    global close_dfs
    global pat_len_dfs
    global state_explored_dfs
    if(gt.goal(config)):
        print("Found a solution(DFS)!")
        print(config)
        print("\n")
        return
    #print("config given to movegen: ",config)
    #print("printing movegen: ",mg.moveGen(config))
    branch = mg.moveGen(config)
    #print("branches: ",branch)
    add = len(branch)
    for node in branch or []:
        if(node not in close_dfs):
            #print("node to put: ",node)
            M.put(node)
        else:
            add = add-1
    close_dfs = close_dfs + branch
    state_explored_dfs = state_explored_dfs+add
    if(M.empty()):
        print("No solution can be found for the starting configuration.\n Closest we could reach is -")
        print(config)
        print("\n")
        return
    config = M.get()
    #print(config)
    #raw_input()
    pat_len_dfs = pat_len_dfs+1
    DFS(config)
    
print("Length of path(DFS): "+str(pat_len_dfs))
print("Number of states explored(DFS): "+str(state_explored_dfs))
print("\n")