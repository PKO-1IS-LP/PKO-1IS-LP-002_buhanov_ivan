from tkinter import *

def str_to_sort_list(event):
    s = ent.get()           # получаем текст из поля ввода
    s = s.split()           # разбиваем на слова
    s.sort()                # сортируем слова
    lab['text'] = ' '.join(s)  # объединяем обратно в строку с пробелами

root = Tk()
root.geometry("205x200")

ent = Entry(width=20)        # поле ввода
but = Button(text="Преобразовать")  # кнопка
lab = Label(width=20, bg='black', fg='white')  # метка для результата

but.bind('<Button-1>', str_to_sort_list)  # привязываем функцию к клику

ent.pack()
but.pack()
lab.pack()

root.mainloop()