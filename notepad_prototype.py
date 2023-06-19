from tkinter import *
from tkinter import filedialog

root = Tk()

root.geometry("720x720")
root.title("NotepadIsUnbreakable")
root.config(bg='black')
root.resizable(False, False)

save_btn = Button(root, width='9', height='1', bg='grey', text='save').place(x = 5, y = 2)
load_btn = Button(root, width='9', height='1', bg='grey', text='load').place(x = 80, y = 2)

entry = Text(root, height='33', width='77', wrap=WORD)
entry.place(x=10, y=60)

root.mainloop()
