

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
        


     