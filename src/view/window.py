from tkinter import Tk, Frame, Label, BOTH, END

class MainWindow(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)   

        self.parent = parent

        label = Label(parent, text="LIVE", width=200, height=80, background="red")
        label.config(font=("Calibri", 44),foreground="white")
        label.pack(fill=BOTH, expand=1)
        self.parent.overrideredirect(1) 
        self.parent.title("Twitch Live Notifier")
        self.pack()

root = Tk()
root.geometry("250x100+" + str(root.winfo_screenwidth() - 250) + "+0")
app = MainWindow(root)
root.lift()
root.call('wm', 'attributes', '.', '-topmost', True)
root.mainloop() 