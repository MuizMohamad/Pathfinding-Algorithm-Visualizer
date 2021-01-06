
from math import floor

import time
import tkinter as tk
from tkinter import messagebox

from Maze import Maze
from Algorithms import dfs,bfs,a_star
from Node import Node,A_StarMaze


root = tk.Tk()
root.title("Pathfinding Algorithm Visualiser")
root.geometry('1120x900')
root.configure(background = 'white')

blankC = tk.Canvas(root, height=50, width=50, bg='white',highlightthickness=0)
blankC.grid(column = 0 , row = 0,sticky = "wens",pady = 0 ,padx = 0)

blankC = tk.Canvas(root, height=50, width=600, bg='white',highlightthickness=0)
blankC.grid(column = 1 , row = 0,sticky = "wens",pady = 0 ,padx = 0)

blankC = tk.Canvas(root, height=600, width=50, bg='white',highlightthickness=0)
blankC.grid(column = 0 , row = 1,sticky = "wens",pady = 0 ,padx = 0)

blockage_state = []


def set_text(text):
    squareNumEntry.delete(0,tk.END)
    squareNumEntry.insert(0,text)
    return

def apply_square_num():
    cur_square_num = int(squareNumEntry.get())
    if (cur_square_num <= 30 and cur_square_num >= 2):
        create_grid()
    else :
        tk.messagebox.showerror("Error", "Please input in range from 2 to 30")
    
    return

def create_path():
    
    w = c.winfo_width() # Get current width of canvas
    #h = c.winfo_height() # Get current height of canvas
    
    squareNumTest = int(squareNumEntry.get())
    if (squareNumTest != cur_square_num):
        tk.messagebox.showerror("Error", "Click apply button to change dimension first")
    else :
        reset_maze()
        chosenAlgo = v.get()
        size_init = w/cur_square_num
        size = floor(size_init)
        
        
        currentMaze = Maze(cur_square_num)
        currentMaze.update_blockage(blockage_state)
            
        startSquare = startMaze
        endSquare   = (endMaze[0]/size,endMaze[1]/size)
            
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
            
            curMaze = A_StarMaze(cur_square_num)
            curMaze.update_blockage(blockage_state)
            
            (path,visited) = a_star(curMaze,curMaze.return_obj_ref(startSquare),curMaze.return_obj_ref(endSquare))
            curMaze.update_path(path)
            curMaze.update_visited(visited)
            
            if (curMaze.return_path() == []):
                tk.messagebox.showerror("Error", "No solution for the maze")
            else :
                delay = 0
                for (x,y) in curMaze.return_visited():
                    c.after(delay,changeSquareColor,x,y,'white')
                    delay += 50
                            
                for (x,y) in curMaze.return_path():
                    c.after(delay,changeSquareColor,x,y,'purple')
                    delay += 50
                    
            return
                
        if (currentMaze.return_path() == []):
                tk.messagebox.showerror("Error", "No solution for the maze")
        else :
            delay = 0
            for (x,y) in currentMaze.return_visited():
                c.after(delay,changeSquareColor,x,y,'white')
                delay += 50
                        
            for (x,y) in currentMaze.return_path():
                c.after(delay,changeSquareColor,x,y,'purple')
                delay += 50
            

def changeSquareColor(x,y,color):
    
    w = c.winfo_width() # Get current width of canvas
    #h = c.winfo_height() # Get current height of canvas
    
    size_init = w/cur_square_num
    size = floor(size_init)
    x_grid = x*size
    y_grid = y*size 
    
    endOrStart = ((x_grid,y_grid) == startMaze or (x_grid,y_grid) == endMaze)
    
    if (not endOrStart):
        c.create_rectangle(x_grid,y_grid,x_grid+size,y_grid+size,fill = color,outline = 'black',width = 2)

     
button_frame = tk.Frame(root,height = 600, width = 280, highlightthickness = 5)
button_frame.grid(column = 2 , row = 1 ,padx = 20)
button_frame.grid_propagate(0)

#fillerCanvas1 = tk.Canvas(button_frame,height = 50, width = 270 , highlightthickness = 0)
#fillerCanvas1.grid(column = 0 , row = 0 , pady = 0 , padx = 0)

algoTxt = tk.Label(button_frame, text = 'Size' , bg = 'white' ,font = "Arial 25 bold", width = 11 , highlightthickness = 5)
algoTxt.grid(column = 0 , row = 0, ipady = 10, padx = 0 , pady = (20,0))

sqNumFrame = tk.Frame(button_frame,height = 100, width = 270)
sqNumFrame.grid(column = 0 , row = 1)
sqNumFrame.grid_propagate(0)

sqNumButtonText = tk.Label(sqNumFrame, text = 'Maze size ( 2-30 ) ' ,font = "Arial 15" ,height = 0 , width = 15 )
sqNumButtonText.grid(column = 0 , row = 1,pady = (30,0) , padx = (20,0) )

squareNumEntry = tk.Entry(sqNumFrame, width= 5 ,bd = 5,font = "Helvetica 12 bold",justify = tk.CENTER)
set_text('30')
squareNumEntry.grid(column = 1 , row = 1, ipady = 3,pady = (30,0) , padx = 0)

squareNumButton = tk.Button(button_frame,text = "Apply size",font = "Helvetica 15 bold", command = apply_square_num)
squareNumButton.grid(column = 0 , row = 2, padx = 50 , pady = (10,10))

algoTxt = tk.Label(button_frame, text = 'Algorithms' , bg = 'white' ,font = "Arial 25 bold", width = 11 , highlightthickness = 5)
algoTxt.grid(column = 0 , row = 3, ipady = 10, padx = 0 , pady = (50,0))

algoRBFrame = tk.Frame(button_frame,height = 100, width = 270)
algoRBFrame.grid_propagate(0)
algoRBFrame.grid(column = 0 , row = 4, pady = 0, padx = 0, ipadx = 0, ipady = 0)

v = tk.StringVar(algoRBFrame,"dfs")

dfsRadioButton =  tk.Radiobutton(algoRBFrame, variable = v,text= 'DFS', value = 'dfs',font = "Helvetica 15 bold")
dfsRadioButton.grid(column = 0 , row = 0, pady = (20,0), padx = (50,20))

bfsRadioButton =  tk.Radiobutton(algoRBFrame, variable = v,text= 'BFS', value = 'bfs',font = "Helvetica 15 bold")
bfsRadioButton.grid(column = 1 , row = 0, pady = (20,0) , padx = 0)

astar_RadioButton =  tk.Radiobutton(algoRBFrame, variable = v,text= 'A*', value = 'astar',font = "Helvetica 15 bold")
astar_RadioButton.grid(column = 0 , row = 1, pady = 0 , padx = (30,20))

createPathButton = tk.Button(button_frame,font = "Helvetica 15 bold" ,text = "Visualize path", command = create_path)
createPathButton.grid(column = 0 , row = 5,pady = 20)


canvasHeight = 750
canvasWidth = 750 

def create_grid(event=None):
    w = c.winfo_width() # Get current width of canvas
    h = c.winfo_height() # Get current height of canvas
    
    blockage_state.clear()
    c.delete('grid_line') # Will only remove the grid_line
    c.create_rectangle(0,0,w,h,fill = 'black',outline = 'black',width = 2)
    
    global cur_square_num
    cur_square_num = int(squareNumEntry.get())
    size_init = w/cur_square_num
    size = floor(size_init)
    end = size*cur_square_num
    
    for x in range(0,end,size):
        square_color_tmp = []
        for y in range(0,end,size): 
            c.create_rectangle(x,y,x+size,y+size,fill = 'orange',outline = 'black',width = 2)
            square_color_tmp.append(0)
        blockage_state.append(square_color_tmp)
    
    c.create_rectangle(0,0,size,size,fill = 'green',outline = 'black',width = 2)
    c.create_rectangle(end-size,end-size,end,end,fill = 'blue',outline = 'black',width = 2)
    
    global startMaze 
    global endMaze
    
    startMaze = (0,0)
    endMaze = (end-size,end-size)

def reset_maze():
    
    w = c.winfo_width() # Get current width of canvas
    
    c.delete('grid_line') # Will only remove the grid_line
    
    global cur_square_num
    cur_square_num = int(squareNumEntry.get())
    size_init = w/cur_square_num
    size = floor(size_init)
    end = size*cur_square_num
    
    for x in range(0,end,size):
        for y in range(0,end,size):
            x_index = floor(x/size)
            y_index = floor(y/size)
            startOrEnd = (x,y) == startMaze or (x,y) == endMaze
            if (blockage_state[x_index][y_index] == 0 and not startOrEnd):
                c.create_rectangle(x,y,x+size,y+size,fill = 'orange',outline = 'black',width = 2)
           


  
c = tk.Canvas(root, height= canvasHeight, width=canvasWidth, bg='black',highlightthickness=0)
c.grid(column = 1 , row = 1, sticky = "wens",pady = 0 ,padx = 0)

c.bind('<Configure>', create_grid)

def click_square(event):
    
    w = c.winfo_width() # Get current width of canvas
    h = c.winfo_height() # Get current height of canvas
    
    squareNum = int(squareNumEntry.get())
    size = min(floor(w/squareNum),floor(h/squareNum))
    
    x = floor(event.x/size) * size
    y = floor(event.y/size) * size
    i = floor(x/size)
    j = floor(y/size)
   
    endOrStart = ((x,y) == startMaze or (x,y) == endMaze)
    
    if (not endOrStart):
        if (blockage_state[i][j] == 0):
            c.create_rectangle(x,y,x+size,y+size,fill = 'red',outline = 'black',width = 2)
            blockage_state[i][j] = 1
        else :
            c.create_rectangle(x,y,x+size,y+size,fill = 'orange',outline = 'black',width = 2)
            blockage_state[floor(x/size)][floor(y/size)] = 0
        
    
c.bind('<Button-1>',click_square)

root.mainloop()