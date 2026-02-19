from tkinter import *
from tkinter import ttk

def show_message():
    text = entry.get().strip()  # получаем текст и убираем пробелы
    if text:  # если текст не пустой
        label["text"] = text
    else:
        label["text"] = "Ничего не введено!"

root = Tk()
root.title("my gui app")
root.geometry("250x200")

entry = ttk.Entry()
entry.pack(anchor=NW, padx=6, pady=6)

btn = ttk.Button(text="Click", command=show_message)
btn.pack(anchor=NW, padx=6, pady=6)

label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)

root.mainloop()