from tkinter import *
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)

class App:
    def __init__(self, master):
        frame = Frame(master)
        fram.pack()
        self.check_var = BooleanVar()
        check = Checkbutton(frame, text='pin 12', command=selft.update, variable=self.check_var, onvalue=True, offvalue=False)
        check.grid(row=1)
    def update(self):
        GPIO.output(12, self.check_var.get())

root = Tk()
root.wm_write('On/Off switch')
app = App(root)
root.geometry("200x50+0+0")
root.mainloop()