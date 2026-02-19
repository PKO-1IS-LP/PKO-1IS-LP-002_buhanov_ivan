from tkinter import *

def show(c_name, c_code):
    entry.delete(0, END)
    entry.insert(0, c_code)
    label.config(text=c_name)

root = Tk()
root.title("Цвета радуги")
root.geometry("400x300")

colors = [
    ("красный", "#ff0000"),
    ("оранжевый", "#ff7d00"),
    ("желтый", "#ffff00"),
    ("зеленый", "#00ff00"),
    ("голубой", "#007dff"),
    ("синий", "#0000ff"),
    ("фиолетовый", "#7d00ff")
]

frame = Frame(root)
frame.pack(pady=20)

# Кнопки БЕЗ ТЕКСТА
for i, (name, code) in enumerate(colors):
    btn = Button(
        frame,
        bg=code,           # только цвет, текста нет!
        width=8,
        height=3,
        relief=RAISED,
        bd=3,
        command=lambda n=name, c=code: show(n, c)
    )
    btn.grid(row=i//3, column=i%3, padx=5, pady=5)

entry = Entry(root, width=20, font=("Arial", 12), justify=CENTER)
entry.pack(pady=10)

label = Label(root, text="", font=("Arial", 12), width=20, height=2, relief=SUNKEN)
label.pack(pady=10)

root.mainloop()