from tkinter import *
from datetime import datetime as dt

def insert_time():
    t = dt.now().time()
    e1.insert(0, t.strftime('%H:%M:%S '))

def insert_date():
    d = dt.now().date()
    e1.insert(0, d.strftime('%d.%m.%Y '))

def clear_field():
    e1.delete(0, END)

root = Tk()
root.title("Вставка даты и времени")
root.geometry("500x150")

e1 = Entry(width=60, font=("Arial", 12))
e1.pack(pady=10)

# Рамка для кнопок
button_frame = Frame(root)
button_frame.pack()

btn_time = Button(button_frame, text="Время", command=insert_time, width=10)
btn_time.grid(row=0, column=0, padx=5)

btn_date = Button(button_frame, text="Дата", command=insert_date, width=10)
btn_date.grid(row=0, column=1, padx=5)

btn_clear = Button(button_frame, text="Очистить", command=clear_field, width=10)
btn_clear.grid(row=0, column=2, padx=5)

root.mainloop()