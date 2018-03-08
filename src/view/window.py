from tkinter import Tk, Frame, Label, BOTH, END
from PIL import ImageTk, Image
from controller.controller import Controller
import os
import threading

class MainWindow(Frame):

    def __init__(self, url, headers):
        
        self.root = Tk()
        self.root.geometry("250x100+" + str(self.root.winfo_screenwidth() - 256) + "+0")
        #Fix this all up with actual root window not in child window
        Frame.__init__(self, self.root)
        self.url = url
        self.headers = headers
        self.parent = self.root #Here too
        self.notifyThread = None

        label = Label(self.parent, text="LIVE", width=200, height=80, background="red")
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

    def refresh(self):
        self.update()
        self.after(5000, self.start)

    def start(self):
        print "Thread is " + str(self.notifyThread)
        if(self.notifyThread is None):
            self.notifyThread = True
            self.notifyThread = threading.Thread(target=self.controller.notifier(self.url, self.headers)).start()
        self.refresh()

    def displayWindow(self, controller):
        self.controller = controller
        self.root.lift()
        self.root.call('wm', 'attributes', '.', '-topmost', True)
        self.start()
        self.root.mainloop()