from tkinter import *

root = Tk()
root.title("Заголовок приложения")
root.geometry("300x250")

# Устанавливаем иконку
try:
    root.iconbitmap(default="icon.ico")
except:
    pass  # если иконки нет - ничего не делаем

# Создаем и размещаем кнопку
try:
    btn = Button(text="Нажми")  
    btn.pack()
except:
    pass

root.mainloop()