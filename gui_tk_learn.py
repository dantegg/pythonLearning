from tkinter import * 
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    
    def createWidgets(self):
        self.nameInput 
        self.helloLabel = Label(self, text="hello, world!")
        self.helloLabel.pack()
        self.quitButton = Button(self, text="Quit", command=self.quit)
        self.quitButton.pack()


app = Application()

# 设置窗口标题
app.master.title('Hello world')
app.mainloop()