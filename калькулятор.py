from tkinter import *

def calc(op):
    try:
        a = float(e1.get())
        b = float(e2.get())
        if op == "/" and b == 0:
            res.config(text="ошибка")
            return
        res.config(text=str(eval(f"{a}{op}{b}")))
    except:
        res.config(text="ошибка")

root = Tk()
root.geometry("250x200")

e1 = Entry(root)
e1.pack()
e2 = Entry(root)
e2.pack()

f = Frame(root)
f.pack()

Button(f, text="+", command=lambda: calc("+")).pack(side=LEFT)
Button(f, text="-", command=lambda: calc("-")).pack(side=LEFT)
Button(f, text="*", command=lambda: calc("*")).pack(side=LEFT)
Button(f, text="/", command=lambda: calc("/")).pack(side=LEFT)

res = Label(root, text="0", bg="lightgray")
res.pack()

root.mainloop()