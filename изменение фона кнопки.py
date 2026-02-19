from tkinter import *

# Функция для изменения свойств кнопки
def change():
    b1['text'] = "Изменено"           
    b1['bg'] = "#04DF00"               
    b1['fg'] = '#ffffff'               
    b1['activebackground'] = '#555555'  
    b1['activeforeground'] = '#ffffff'  

root = Tk()
root.geometry("250x200")
try:
    root.iconbitmap(default="icon.ico")
except:
    pass  # если иконки нет - ничего не делаем

b1 = Button(text="Изменить", width=15, height=3)


b1.config(command=change)


b1.pack()

root.mainloop()