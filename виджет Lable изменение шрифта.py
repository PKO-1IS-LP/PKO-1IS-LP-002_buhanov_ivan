from tkinter import *

root = Tk()

# ИСПРАВЛЕНО: переменные не могут начинаться с цифры
# Было: 11 = Label(...) - так нельзя!
label1 = Label(text="Буханов", font="Arial 32")  # имя переменной изменено
label2 = Label(text="Иван",
               font=("Comic Sans MS", 24, "bold"))
label3 = Label(text="Александрович", font="Arial 32")
# Устанавливаем границы и фоновый цвет
label1.config(bd=20, bg="#ffffff")  # bd = border width (ширина границы)
label2.config(bd=20, bg="#0022ff")  # светло-голубой фон
label3.config(bd=20, bg="#ff0000")
# Размещаем метки в окне
label1.pack()
label2.pack()
label3.pack()
root.mainloop()