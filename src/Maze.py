from Node import Node

class Maze:
    
    def __init__(self,square_num):
        
        self.maze_dict = {}
        self.square_num = square_num
        self.path = []
        self.visited = []
        for x in range(0,square_num):
            for y in range(0,square_num):
                possible_c = []
                if (x-1 >= 0) :
                    possible_c.append((x-1,y))
                if (y-1 >= 0) :
                    possible_c.append((x,y-1))
                if (x + 1 < square_num):
                    possible_c.append((x+1,y))
                if (y + 1 < square_num):
                    possible_c.append((x,y+1))
                    
                self.maze_dict[(x,y)] = possible_c
            
    def update_square(self,x,y,blockage_state):
        
        if (x-1 >= 0):
            if (blockage_state[x-1][y] == 1):
                self.maze_dict[(x,y)].remove((x-1,y))
        
        if (y-1 >= 0):
            if (blockage_state[x][y-1] == 1):
                self.maze_dict[(x,y)].remove((x,y-1))
        
        if (x+1 < self.square_num):
            if (blockage_state[x+1][y] == 1):
                self.maze_dict[(x,y)].remove((x+1,y))
        
        if (y+1 < self.square_num):
            if (blockage_state[x][y+1] == 1):
                self.maze_dict[(x,y)].remove((x,y+1))
    
    def update_blockage(self,blockage_state):
        
        for x in range(0,self.square_num):
            for y in range(0,self.square_num):
                self.update_square(x,y,blockage_state)
              
    def return_maze(self):
        return self.maze_dict
    
    def update_path(self,path):
        self.path = path
    
    def return_path(self):
        return self.path
    
    def update_visited(self,visited):
        self.visited = visited
    
    def return_visited(self):
        return self.visited
    
    def return_square_num(self):
        return self.square_num
    
class A_StarMaze:
    
    def __init__(self,square_num):
        
        self.maze_dict = {}
        self.square_num = square_num
        self.path = []
        self.visited = []
        self.object_ref = {}
        
        for x in range(0,square_num):
            for y in range(0,square_num):
                theNode = Node((x,y))
                self.object_ref[(x,y)] = theNode

        for x in range(0,square_num):
            for y in range(0,square_num):
                possible_c = []
                if (x-1 >= 0) :
                    possible_c.append(self.object_ref[(x-1,y)])
                if (y-1 >= 0) :
                    possible_c.append(self.object_ref[(x,y-1)])
                if (x + 1 < square_num):
                    possible_c.append(self.object_ref[(x+1,y)])
                if (y + 1 < square_num):
                    possible_c.append(self.object_ref[(x,y+1)])
                    
                self.maze_dict[self.object_ref[(x,y)]] = possible_c
            
    def update_square(self,x,y,blockage_state):
        
        if (x-1 >= 0):
            if (blockage_state[x-1][y] == 1):
                self.maze_dict[self.object_ref[(x,y)]].remove(self.object_ref[(x-1,y)])
        
        if (y-1 >= 0):
            if (blockage_state[x][y-1] == 1):
                self.maze_dict[self.object_ref[(x,y)]].remove(self.object_ref[(x,y-1)])
        
        if (x+1 < self.square_num):
            if (blockage_state[x+1][y] == 1):
                self.maze_dict[self.object_ref[(x,y)]].remove(self.object_ref[(x+1,y)])
        
        if (y+1 < self.square_num):
            if (blockage_state[x][y+1] == 1):
                self.maze_dict[self.object_ref[(x,y)]].remove(self.object_ref[(x,y+1)])
    
    def update_blockage(self,blockage_state):
        
        for x in range(0,self.square_num):
            for y in range(0,self.square_num):
                self.update_square(x,y,blockage_state)
              
    def return_maze(self):
        return self.maze_dict
    
    def update_path(self,path):
        self.path = path
    
    def return_path(self):
        return self.path
    
    def update_visited(self,visited):
        self.visited = visited
    
    def return_visited(self):
        return self.visited
    
    def return_square_num(self):
        return self.square_num
    
    def return_obj_ref(self,coordinate):
        return self.object_ref[coordinate]
    
    def retrace_path(self,start,endNode):
        
        path = []
        currentNode = endNode
        
        while (currentNode != start):
            path.append(currentNode.return_coordinate())
            currentNode = currentNode.return_parent()
        
        path.reverse()
        
        return path