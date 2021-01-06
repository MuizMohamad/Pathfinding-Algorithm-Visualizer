

class Node:
    
    def __init__(self,coordinate):
        self.coordinate = coordinate
        self.parent = None
        self.gcost = -1
        self.hcost = -1
        self.fcost = -1

    def return_coordinate(self):
        return self.coordinate
    
    def return_parent(self):
        return self.parent
    
    def return_gcost(self):
        return self.gcost
    
    def return_hcost(self):
        return self.hcost
    
    def return_fcost(self):
        return self.fcost
    
    def calculate_gcost(self,parentNode):
        x_self = self.coordinate[0]
        y_self = self.coordinate[1]
        
        parentCoordinate = parentNode.return_coordinate()
        x_parent = parentCoordinate[0]
        y_parent = parentCoordinate[1]
        
        return self.gcost +  (x_self-x_parent)**2 + (y_self-y_parent)**2
    
    def calculate_hcost(self,targetNode):
        x_self = self.coordinate[0]
        y_self = self.coordinate[1]
        
        target = targetNode.return_coordinate()
        x_target = target[0]
        y_target = target[1]
        
        return (x_self-x_target)**2 + (y_self-y_target)**2
    
    def calculate_fcost(self,parentNode,target):
        gcost = self.calculate_gcost(parentNode)
        fcost = self.calculate_hcost(target)
        return gcost + fcost
    
    def update_gcost(self,parentNode):
        self.gcost = self.calculate_gcost(parentNode)
        
    def update_hcost(self,target):
        self.hcost = self.calculate_hcost(target)
    
    def update_fcost(self,parentNode,target):
        self.update_gcost(parentNode)
        self.update_hcost(target)
        self.fcost = self.calculate_fcost(parentNode,target)
           
    def set_parent(self,parent):
        self.parent = parent
    
    def set_gcost(self, gcost):
        self.gcost = gcost
                
    def set_hcost(self, hcost):
        self.hcost = hcost
    
    def set_fcost(self, fcost):
        self.fcost = fcost
        
    #def __hash__(self):
    #    return hash((self.coordinate, self.parent,self.gcost,self.hcost,self.fcost))

    #def __eq__(self, other):
    #    return (self.coordinate,self.parent,self.gcost,self.hcost, self.fcost) == (other.coordinate,other.parent,other.gcost,other.hcost, other.fcost)

    #def __ne__(self, other):
        # Not strictly necessary, but to avoid having both x==y and x!=y
        # True at the same time
    #    return not(self == other)

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
     