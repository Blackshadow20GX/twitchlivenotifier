from tkinter import Tk, Frame, Label, BOTH, END
from PIL import ImageTk, Image
import os

class MainWindow(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)   

        self.parent = parent

        label = Label(parent, text="LIVE", width=200, height=80, background="red")
        label.config(font=("Calibri", 44),foreground="white")
        label.pack(fill=BOTH, expand=1)

        rwd = os.path.dirname(os.path.realpath(__file__))
        rwd = os.path.split(rwd)[0]
        path = rwd + "/assets/icon/cog.png"
        
        img = ImageTk.PhotoImage(Image.open(path).resize((30,30), Image.ANTIALIAS))
        panel = Label(label, image=img, background="red")
        panel.image = img
        panel.place(rely=0, relx=1.0, x=0, y=0, anchor="ne")


        self.parent.title("Twitch Live Notifier")
        self.pack()

root = Tk()
root.geometry("250x100+" + str(root.winfo_screenwidth() - 256) + "+0")
app = MainWindow(root)
root.lift()
root.call('wm', 'attributes', '.', '-topmost', True)
root.mainloop() 