from Tkinter import *

root = Tk()

lable1 = Label(root, text="Entry your expression:")
lable1.pack()

def evaluate(event):
    data = e.get()
    ans.configure(text="Answer: " + str(eval(data)))

e = Entry(root)
e.bind("<Return>", evaluate)
e.pack()

ans = Label(root)
ans.pack()

root.mainloop()