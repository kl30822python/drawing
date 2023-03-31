import tkinter as tk
from tkinter import ttk
# add below
import tkinter.font as tkFont

class Window(tk.Tk):
    def __init__(self, **kwargs): 
        #*kwargs or args可以不寫
        super().__init__(**kwargs) 
        ttkStyle = ttk.Style()
        #*kwargs or args可以不寫
        #print(ttkStyle.theme_names())
        #ttkStyle.theme_use('classic')
        ttkStyle.theme_use('default') # classic -> default
        ttkStyle.configure('white.TLableframe',background='white',bd=0)
        ttkStyle.configure('white.TLableframe.Label',background='white', foreground='red')
        #*** add below
        f1 = tkFont.Font(family='Helvetica', size=16, weight='bold')

        drawingFrame = ttk.LabelFrame(self, text="here is drawing area")
        drawingFrame.pack(padx=50, pady=50)
        #tk.Button(drawingFrame, text="press me!", padx=10, pady=10).pack(padx=30, pady=20)

        lineCanvas = tk.Canvas(drawingFrame, width=100, height=30, bd=0, highlightthickness=0, background='white')
        lineCanvas.create_line((0,0),(100,0),width=30, fill='blue')
        lineCanvas.pack()

        ovalCanvas = tk.Canvas(drawingFrame, width=110, height=110, bd=0, highlightthickness=0, background='white')
        ovalCanvas.create_oval((10,10),(100,100),width=10, outline='red',fill='black')
        ovalCanvas.pack()

        textCanvas = tk.Canvas(drawingFrame, width=110, height=50, bd=0, highlightthickness=0, background='white')
        textCanvas.create_text(0,0,test="ABC_中文",font=f1, anchor='nw')
        textCanvas.pack()



def main():
    window = Window()
    window.title('drawing')
    window.mainloop()

if __name__ == "__main__":
    main()
