from tkinter import *
class App(Frame):
    def __init__(self, parent):
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.canvas = Canvas(self.parent, bg = "white", width = 400, height = 400 )
        self.item1 = self.canvas.create_oval(50,60,40,50, fill = "red")
        self.item2 = self.canvas.create_oval(100,110,90,100, fill = "red")
        self.item3 = self.canvas.create_oval(150,160,140,150,fill = "red")
        self.item4 = self.canvas.create_oval(200,210,190,200, fill = "red")
        self.item5 = self.canvas.create_oval(250,260,240,250,fill = "red")
        self.canvas.pack()
        self.canvas.bind("<Button-3>",self.color)
        self.canvas.bind("<Button-1>",self.move)
    def color(self,event):
        self.item = self.canvas.find_closest(event.x, event.y)
        self.coord = self.canvas.coords(self.item)
        print(self.coord)
        print(self.item)
        print(event.x,event.y)
        if self.canvas.itemcget(self.item,"fill") == "red":
            self.canvas.itemconfig(self.item,fill = "blue")
        else:
            self.canvas.itemconfig(self.item,fill = "red")

    def move(self,events):
        self.coords1 = self.canvas.coords(self.item)
        print(self.coords1)
        print(events.x,events.y)
        self.canvas.move(self.item,events.x-self.coords1[0],events.y-self.coords1[1])
        if self.canvas.itemcget(self.item,"fill") == "blue":
            self.canvas.itemconfig(self.item,fill = "green")
        else:
            self.canvas.itemconfig(self.item,fill = "green")

def main():
    root = Tk()
    a = App(root)
    root.mainloop()
main()
