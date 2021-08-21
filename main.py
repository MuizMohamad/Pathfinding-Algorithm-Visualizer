
from math import floor

import tkinter as tk

from Maze import Maze,A_StarMaze
from Algorithms import dfs,bfs,a_star

from Visualizer import Visualizer

bgColor = '#FFD992'

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Pathfinding Algorithm Visualiser")
    root.geometry('1120x850')
    root.configure(background = bgColor)
    root.resizable(False,False)
    Visualizer(root)
    root.mainloop()

