import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self, **kwargs): 
        #*kwargs or args可以不寫
        super().__init__(**kwargs) 
        ttkStyle = ttk.Style()
        #*kwargs or args可以不寫
        #print(ttkStyle.theme_names())
        #ttkStyle.theme_use('classic')
        ttkStyle.theme_use('default') # classic -> default
        ttkStyle.configure('white.TLableFrame',background='white')

        drawingFrame = ttk.Labelframe(self, text="here is drawing area")
        drawingFrame.pack(padx=50, pady=50)
        #tk.Button(drawingFrame, text="press me!", padx=10, pady=10).pack(padx=30, pady=20)
        lineCanvas = tk.Canvas(drawingFrame, width=100, height=30)
        lineCanvas.create_line((0,0),(100,0),width=30, fill='blue')
        lineCanvas.pack()
        ovalCanvas = tk.Canvas(drawingFrame, width=110, height=110)
        ovalCanvas.create_oval((10,10),(100,100),width=10, outline='red',fill='black')
        ovalCanvas.pack()



def main():
    window = Window()
    window.title('drawing')
    window.mainloop()

if __name__ == "__main__":
    main()
