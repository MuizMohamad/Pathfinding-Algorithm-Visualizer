
import tkinter as tk

window = tk.Tk()

window.title("Pathfinding Algorithm Visualiser")
window.geometry('1080x720')

lbl = tk.Label(window,text = "Hello" , font = ("Arial Bold",20))
lbl.grid(column = 0 , row = 0)

txt = tk.Entry(window,width = 10)
txt.grid(column = 1 , row = 0)


def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text = res)

btn = tk.Button(window,text = 'Click Me',bg = "orange", fg = "red", font = ("Comic Sans MS",30) , command = clicked)
btn.grid(column = 2 , row = 0)

rad1 = tk.Radiobutton(window,text='First', value=1)
rad2 = tk.Radiobutton(window,text='Second', value=2)
rad3 = tk.Radiobutton(window,text='Third', value=3)

rad1.grid(column=0, row=1)
rad2.grid(column=1, row=1)
rad3.grid(column=2, row=1)

c = tk.Canvas(window, height=600, width=600, bg='orange')
c.grid(column = 0 , row = 0)

c.create_line([(600, 0), (600, 600)], tag='grid_line')

window.mainloop()