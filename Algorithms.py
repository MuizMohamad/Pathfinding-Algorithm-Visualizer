
from Maze import Maze,A_StarMaze
from Node import Node

graph = { (0,0) : [(1,0),(0,1)],(1,0) : [(2,0)],(2,0):[], 
          (0,1) : [(0,2)] , (0,2) : [(0,3)] , (0,3) : [(1,3)],
          (1,3) : [(2,3)] , (2,3) : [(3,3)], (3,3) : []}

graph1 = { (0,0) : [(1,0),(0,1)],(1,0) : [(2,0)],(2,0):[], 
          (0,1) : [(0,2)] , (0,2) : [] }

#actualPath = []
#visited = []

blockage_state = [[0,0,0,0],[0,1,1,0],[0,1,1,0],[1,1,1,0]]

testMaze = Maze(4)
testMaze.update_blockage(blockage_state)

def dfs(path, visited, graph, node, target):
    
    visited.append(node)
    path.append(node)
    if (node == target):
        return path

    x = node[0]
    y = node[1]
    
    if graph[node] == [] :
        path.pop()
        return []
    
    if (x,y-1) in graph[node] and (x,y-1) not in visited :
       
        testPath = dfs(path,visited, graph, (x,y-1),target)
        if testPath != [] :
            return testPath
        
    if (x+1,y) in graph[node] and (x+1,y) not in visited :
        
        testPath = dfs(path,visited, graph, (x+1,y),target)
        if testPath != [] :
            return testPath
        
    if (x,y+1) in graph[node] and (x,y+1) not in visited :

        testPath = dfs(path,visited, graph, (x,y+1),target)
        if testPath != [] :
            return testPath
        
    if (x-1,y) in graph[node] and (x-1,y) not in visited:
      
        testPath = dfs(path, visited,graph, (x-1,y),target)
        if testPath != [] :
            return testPath

    path.pop()
    return []


def bfs(graph_to_search, start, end):
    queue = [[start]]
    visited = []

    while queue:
        # Gets the first path in the queue
        path = queue.pop(0)

        # Gets the last node in the path
        vertex = path[-1]

        # Checks if we got to the end
        if vertex == end:
            return (path,visited)
        # We check if the current node is already in the visited nodes set in order not to recheck it
        elif vertex not in visited:
            # enumerate all adjacent nodes, construct a new path and push it into the queue
            for current_neighbour in graph_to_search.get(vertex, []):
                new_path = list(path)
                new_path.append(current_neighbour)
                queue.append(new_path)

            # Mark the vertex as visited
            visited.append(vertex)


testmaze2 = A_StarMaze(4)
testmaze2.update_blockage(blockage_state)

def a_star(maze,start,target):
    
    opened = []
    closed = []
    visited = []
    
    opened.append(start)

    graph = maze.return_maze()
    while (len(opened) > 0):
        
        currentNode  = min(opened,key=lambda x: x.return_fcost())
        #print('cur node = ',currentNode)
        opened.remove(currentNode)
        closed.append(currentNode)
        visited.append(currentNode.return_coordinate())
        
        if (currentNode == target):
            testmaze2.update_path(maze.retrace_path(start,currentNode)) 
            testmaze2.update_visited(visited)
            return (maze.retrace_path(start,currentNode),visited)
        
        try :
            neighbours = graph[currentNode]
        except :
            print('ERORR')
            print('same =', maze.return_maze() == graph)
            print(maze.return_maze())
            break
        
        for n in neighbours:
            
            if n in closed:
                continue
                
            shorterPathExist = n.calculate_fcost(currentNode,target) < n.return_fcost()

            if (shorterPathExist) or (n not in opened):
                n.update_fcost(currentNode,target)
                n.set_parent(currentNode)
                if n not in opened:
                    opened.append(n)
                

        
            
            