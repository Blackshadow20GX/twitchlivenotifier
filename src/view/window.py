from tkinter import Tk, Frame, Label, BOTH, END
from PIL import ImageTk, Image
from controller.controller import Controller
import os
import threading

class MainWindow(Frame):

    def __init__(self):
        
        self.root = Tk()
        self.root.geometry("250x100+" + str(self.root.winfo_screenwidth() - 250) + "+0")
        Frame.__init__(self, self.root)
        self.notifyThread = threading.Thread()
        
        self.initializeWidgets()
        self.initializeEvents()

        self.root.title("Twitch Live Notifier")
        self.root.overrideredirect(1) #Removes window dressing

        self.pack()

    def initializeWidgets(self):
        self.lbl_status = Label(self.root, text="LIVE", width=200, height=80, background="red")
        self.lbl_status.config(font=("Calibri", 44),foreground="white")
        self.lbl_status.pack(fill=BOTH, expand=1)

        rwd = os.path.dirname(os.path.realpath(__file__))
        rwd = os.path.split(rwd)[0]
        path = rwd + "/assets/icon/cog.png"
        
        img = ImageTk.PhotoImage(Image.open(path).resize((25,25), Image.ANTIALIAS))
        self.cog = Label(self.lbl_status, image=img, background="red")
        self.cog.image = img
        self.cog.place(rely=0, relx=1.0, x=0, y=0, anchor="ne")

    def initializeEvents(self):
        self.root.bind('<B1-Motion>', self.movewindow)

    def movewindow(self, event):
        self.root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

    def refresh(self):
        self.updateStatus()
        self.update()
        self.root.call('wm', 'attributes', '.', '-topmost', True)
        self.after(5000, self.checkStreamStatus)

    def checkStreamStatus(self):
        self.notifyThread = threading.Thread(target=self.controller.checkStreamStatus()).start()
        self.refresh()

    def updateStatus(self):
        live = self.controller.isOnline()
        if(live):
            self.lbl_status.config(text="LIVE", background="red")
            self.cog.config(background="red")
            self.pack()
        else:
            self.lbl_status.config(text="OFFLINE", background="gray")
            self.cog.config(background="gray")
            self.pack()

    def displayWindow(self, controller):
        self.controller = controller
        self.root.lift()
        self.root.call('wm', 'attributes', '.', '-topmost', True)
        self.checkStreamStatus()
        self.root.mainloop()