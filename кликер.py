from tkinter import *
from tkinter import ttk

# Счетчик кликов
clicks = 0

# Функция, которая вызывается при нажатии на кнопку
def click_button():
    global clicks  # указываем, что используем глобальную переменную
    clicks += 100    # увеличиваем счетчик на 1
    # изменяем текст на кнопке - показываем количество кликов
    btn["text"] = f"Clicks {clicks}"  # ИСПРАВЛЕНО: было "Clocks" (опечатка)

root = Tk()
root.title("school")
root.geometry("250x150")
try:
    root.iconbitmap(default="icon.ico")
except:
    pass  # если иконки нет - ничего не делаем
# Создаем кнопку с текстом "Click Me" и привязываем функцию click_button к событию нажатия
btn = ttk.Button(text="Click Me", command=click_button)
btn.pack()

root.mainloop()