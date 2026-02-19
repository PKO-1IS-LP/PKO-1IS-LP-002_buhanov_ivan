from tkinter import *
from tkinter import ttk

root = Tk()
root.title("my gui app")
root.geometry("250x200")
try:
    root.iconbitmap(default="icon.ico")
except:
    pass  # если иконки нет - ничего не делаем
# Создаем кнопку с текстом "Click Me" и устанавливаем состояние "disabled" (неактивная)
btn = ttk.Button(text="Click Me", state=["disabled"])
btn.pack()

root.mainloop()