from tkinter import *
from tkinter import ttk

root = Tk()
root.title("my gui app")
root.geometry("250x150")
try:
    root.iconbitmap(default="icon.ico")
except:
    pass  # если иконки нет - ничего не делаем 
# Создаем кнопку
btn = ttk.Button()
btn.pack()

# Устанавливаем параметр text через квадратные скобки (как в словаре)
btn["text"] = "Send"
# Получаем значение параметра text
btnText = btn["text"]
print(btnText)  # Выведет: Send

# Устанавливаем параметр text через метод config()
btn.config(text="Send Email")
# Снова получаем значение параметра text
btnText = btn["text"]
print(btnText)  # Выведет: Send Email

root.mainloop()