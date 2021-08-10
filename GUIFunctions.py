from math import floor

from Maze import Maze,A_StarMaze
from Algorithms import dfs,bfs,a_star

import tkinter as tk
from tkinter import messagebox

class Visualizer:

    def __init__(self,root):

        self.window = root
        self.bgColor = '#FFD992'

        self.main_canvas = tk.Canvas(self.window, height=50, width=50, bg=self.bgColor,highlightthickness=0)
        self.main_canvas.grid(column = 0 , row = 0,sticky = "wens",pady = 0 ,padx = 0)

        self.blockage_state = []
        self.cur_square_num = 30

        self.widget_init()

        self.canvasHeight = 750
        self.canvasWidth = 750 

        self.start_maze = (0,0)
        self.end_maze = (30,30)

        self.c = tk.Canvas(self.window, height= self.canvasHeight, width = self.canvasWidth, bg='#FFD992',highlightthickness=0)
        self.c.grid(column = 1 , row = 1, sticky = "wens",pady = 0 ,padx = 0)

        self.c.bind('<Configure>', self.create_grid)
        self.c.bind('<Button-1>',self.click_square)

    def widget_init(self):

        self.button_frame = tk.Frame(self.window,height = 600, width = 280, highlightthickness = 5, bg = '#6D4700', highlightbackground= '#5B3B00')
        self.button_frame.grid(column = 2 , row = 1 ,padx = 20)
        self.button_frame.grid_propagate(0)

        self.algoTxt = tk.Label(self.button_frame, text = 'Size' , bg = '#FFDFA4' ,font = "Arial 25 bold", width = 11 , highlightthickness = 5)
        self.algoTxt.grid(column = 0 , row = 0, ipady = 10, padx = 0 , pady = (10,10))

        self.sqNumFrame = tk.Frame(self.button_frame,height = 100, width = 270, bg = '#FFCC6D')
        self.sqNumFrame.grid(column = 0 , row = 1)
        self.sqNumFrame.grid_propagate(0)

        self.sqNumButtonText = tk.Label(self.sqNumFrame, text = 'Maze size ( 2-30 ) ' ,font = "Arial 15" , bg = '#FFCC6D',height = 0 , width = 15 )
        self.sqNumButtonText.grid(column = 0 , row = 1,pady = (30,0) , padx = (20,0) )

        self.squareNumEntry = tk.Entry(self.sqNumFrame, width= 5 ,bd = 5,font = "Helvetica 12 bold",justify = tk.CENTER)
        self.set_text(self.squareNumEntry,'30')
        self.squareNumEntry.grid(column = 1 , row = 1, ipady = 3,pady = (30,0) , padx = 0)

        self.sizeBFrame = tk.Frame(self.button_frame,height = 50, width = 270, bg = '#FFCC6D')
        self.sizeBFrame.grid_propagate(0)
        self.sizeBFrame.grid(column = 0 , row = 2, pady = 0, padx = 0, ipadx = 0, ipady = 0)

        self.resetButton = tk.Button(self.sizeBFrame,text = "Clear maze" , font = "Helvetica 12 bold", command = self.reset_maze)
        self.resetButton.grid(column = 0 , row = 0,padx = (30,20))

        self.applySizeButton = tk.Button(self.sizeBFrame,text = "Apply size",font = "Helvetica 12 bold", command = self.apply_square_num)
        self.applySizeButton.grid(column = 1, row = 0)

        self.algoTxt = tk.Label(self.button_frame, text = 'Algorithms' , bg = '#FFDFA4' ,font = "Arial 25 bold", width = 11 , highlightthickness = 5)
        self.algoTxt.grid(column = 0 , row = 3, ipady = 10, padx = 0 , pady = (10,10))

        self.algoRBFrame = tk.Frame(self.button_frame,height = 100, width = 270, bg = '#FFCC6D')
        self.algoRBFrame.grid_propagate(0)
        self.algoRBFrame.grid(column = 0 , row = 4, pady = 0, padx = 0, ipadx = 0, ipady = 0)

        v = tk.StringVar(self.algoRBFrame,"dfs")

        self.dfsRadioButton =  tk.Radiobutton(self.algoRBFrame, variable = v,text= 'DFS', value = 'dfs',font = "Helvetica 15 bold" , bg = '#FFCC6D')
        self.dfsRadioButton.grid(column = 0 , row = 0, pady = (20,0), padx = (50,20))

        self.bfsRadioButton =  tk.Radiobutton(self.algoRBFrame, variable = v,text= 'BFS', value = 'bfs',font = "Helvetica 15 bold", bg = '#FFCC6D')
        self.bfsRadioButton.grid(column = 1 , row = 0, pady = (20,0) , padx = 0)

        self.astar_RadioButton =  tk.Radiobutton(self.algoRBFrame, variable = v,text= 'A*', value = 'astar',font = "Helvetica 15 bold", bg = '#FFCC6D')
        self.astar_RadioButton.grid(column = 0 , row = 1, pady = 0 , padx = (30,20))

        self.pathBFrame = tk.Frame(self.button_frame,height = 50, width = 270 , bg ='#FFCC6D')
        self.pathBFrame.grid_propagate(0)
        self.pathBFrame.grid(column = 0 , row = 5, pady = (0,0), padx = 0, ipadx = 0, ipady = 0)

        self.resetPathButton = tk.Button(self.pathBFrame,font = "Helvetica 12 bold" ,text = "Reset path", command = self.reset_path)
        self.resetPathButton.grid(column = 0 , row = 0, padx = (20,10), pady = 10)

        self.createPathButton = tk.Button(self.pathBFrame,font = "Helvetica 12 bold" ,text = "Visualize path", command = self.create_path)
        self.createPathButton.grid(column = 1 , row = 0, padx = (10,0) , pady = 10)

        

    def set_text(self,text_box,text):

        text_box.delete(0,tk.END)
        text_box.insert(0,text)

        return

    def apply_square_num(self):

        self.cur_square_num = int(self.squareNumEntry.get())
        if (self.cur_square_num <= 30 and self.cur_square_num >= 2):
            self.create_grid()
        else :
            tk.messagebox.showerror("Error", "Please input in range from 2 to 30")
        
        return

    def reset_maze(self):
        
        self.create_grid()
        
        return

    def reset_path(self):
        
        self.clear_path()
        
        return     

    def create_path(self):
        
        w = self.c.winfo_width() # Get current width of canvas
        
        squareNumTest = int(self.squareNumEntry.get())
        if (squareNumTest != self.cur_square_num):
            
            tk.messagebox.showerror("Error", "Click apply button to change dimension first")
            
        else :
            
            self.clear_path()
            chosenAlgo = self.v.get()
            size_init = w/self.cur_square_num
            size = floor(size_init)
            
            currentMaze = Maze(self.cur_square_num)
            currentMaze.update_blockage(self.blockage_state)
                
            startSquare = self.start_maze
            endSquare   = (self.end_maze[0]/size,self.end_maze[1]/size)
                
            if (chosenAlgo == 'dfs' or chosenAlgo == 'bfs'):
                
                if (chosenAlgo == 'dfs'):
                    actualPath = []
                    visited = []
                    
                    dfs(actualPath,visited,currentMaze.return_maze(),startSquare,endSquare)
                    
                    currentMaze.update_path(actualPath)
                    currentMaze.update_visited(visited)
                        
                        
                elif (chosenAlgo == 'bfs') :
                    
                    (path,visited) = bfs(currentMaze.return_maze(),startSquare,endSquare)

                    currentMaze.update_path(path)
                    currentMaze.update_visited(visited)
            
            elif (chosenAlgo == 'astar'):
                
                curMaze = A_StarMaze(self.cur_square_num)
                curMaze.update_blockage(self.blockage_state)
                
                (path,visited) = a_star(curMaze,curMaze.return_obj_ref(startSquare),curMaze.return_obj_ref(endSquare))
                curMaze.update_path(path)
                curMaze.update_visited(visited)
                
                if (curMaze.return_path() == []):
                    tk.messagebox.showerror("Error", "No solution for the maze")
                else :
                    delay = 0
                    for (x,y) in curMaze.return_visited():
                        self.c.after(delay,self.changeSquareColor,x,y,'white')
                        delay += 50
                                
                    for (x,y) in curMaze.return_path():
                        self.c.after(delay,self.changeSquareColor,x,y,'purple')
                        delay += 50
                        
                return
                    
            if (currentMaze.return_path() == []):
                    tk.messagebox.showerror("Error", "No solution for the maze")
            else :
                delay = 0
                for (x,y) in currentMaze.return_visited():
                    self.c.after(delay,self.changeSquareColor,x,y,'white')
                    delay += 50
                            
                for (x,y) in currentMaze.return_path():
                    self.c.after(delay,self.changeSquareColor,x,y,'purple')
                    delay += 50
                

    def changeSquareColor(self,x,y,color):
        
        w = self.c.winfo_width() # Get current width of canvas
        #h = c.winfo_height() # Get current height of canvas
    
        size_init = w/self.cur_square_num
        size = floor(size_init)
        x_grid = x*size
        y_grid = y*size 
        
        endOrStart = ((x_grid,y_grid) == self.start_maze or (x_grid,y_grid) == self.end_maze)
        
        if (not endOrStart):
            self.c.create_rectangle( x_grid , y_grid , x_grid+size , y_grid+size , fill = color , outline = 'black' , width = 2 )

    def create_grid(self,event=None):
        w = self.c.winfo_width() # Get current width of canvas
        h = self.c.winfo_height() # Get current height of canvas
        
        self.blockage_state.clear()
        self.c.delete('grid_line') # Will only remove the grid_line
        self.c.create_rectangle(0,0,w,h,fill = '#FFD992',outline = 'black',width = 0)
        
        size_init = w/self.cur_square_num
        size = floor(size_init)
        end = size*self.cur_square_num
        
        for x in range(0,end,size):
            square_color_tmp = []
            for y in range(0,end,size): 
                self.c.create_rectangle(x,y,x+size,y+size,fill = 'orange',outline = 'black',width = 2)
                square_color_tmp.append(0)
            self.blockage_state.append(square_color_tmp)
        
        self.c.create_rectangle(0,0,size,size,fill = 'green',outline = 'black',width = 2)
        self.c.create_rectangle(end-size,end-size,end,end,fill = 'blue',outline = 'black',width = 2)
        
        self.start_maze = (0,0)
        self.end_maze = (end-size,end-size)
        
    def clear_path(self):
    
        w = self.c.winfo_width() # Get current width of canvas
        
        self.c.delete('grid_line') # Will only remove the grid_line
        
        size_init = w/self.cur_square_num
        size = floor(size_init)
        end = size*self.cur_square_num
        
        for x in range(0,end,size):
            for y in range(0,end,size):
                x_index = floor(x/size)
                y_index = floor(y/size)
                startOrEnd = (x,y) == self.start_maze or (x,y) == self.end_maze
                if (self.blockage_state[x_index][y_index] == 0 and not startOrEnd):
                    self.c.create_rectangle(x,y,x+size,y+size,fill = 'orange',outline = 'black',width = 2)

    def click_square(self,event):
    
        w = self.c.winfo_width() # Get current width of canvas
        h = self.c.winfo_height() # Get current height of canvas

        size = min(floor(w/self.cur_square_num),floor(h/self.cur_square_num))
        
        x = floor(event.x/size) * size
        y = floor(event.y/size) * size
        i = floor(x/size)
        j = floor(y/size)
    
        endOrStart = ((x,y) == self.start_maze or (x,y) == self.end_maze)
            
        if (not endOrStart):
            if (self.blockage_state[i][j] == 0):
                self.c.create_rectangle(x,y,x+size,y+size,fill = 'red',outline = 'black',width = 2)
                self.blockage_state[i][j] = 1
            else :
                self.c.create_rectangle(x,y,x+size,y+size,fill = 'orange',outline = 'black',width = 2)
                self.blockage_state[floor(x/size)][floor(y/size)] = 0
        
    
   
