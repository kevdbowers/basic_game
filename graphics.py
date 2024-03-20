from tkinter import Tk, Canvas, CENTER, BOTH  #importing necessary parts of tkinter library

class Window:  #defining a Window class

    def __init__(self):  #defining the initial variables for the Window class
        self.root = Tk()
        self.root.title("Basic Game")
        self.canvas = Canvas(self.root, bg = "white", width = 800, height = 600)
        self.canvas.pack(anchor = CENTER, fill = BOTH, expand = True)
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):  #defining a function to keep the Window updated
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):  #defining a function to maintain the window until it is closed, then print an exit message
        self.running = True
        while self.running == True:
            self.redraw()
        print("Window closed...")

    def close(self):  #defining a function to close the Window
        self.running = False