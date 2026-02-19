from tkinter import *
from tkinter import ttk
import re

def is_valid(newval):
    # Разрешаем пустую строку или строку, начинающуюся с + и содержащую только цифры после него
    if newval == "":
        errmsg.set("")
        return True
    
    # Проверяем, что первый символ - это +
    if newval[0] != '+':
        errmsg.set("Номер должен начинаться с '+'")
        return False
    
    # Проверяем, что остальные символы - только цифры
    if len(newval) > 1:
        if not newval[1:].isdigit():
            errmsg.set("После '+' должны быть только цифры")
            return False
    
    # Проверяем длину (не более 12 символов включая +)
    if len(newval) > 12:
        errmsg.set("Максимальная длина номера - 12 символов (включая +)")
        return False
    
    # Если все проверки пройдены
    if len(newval) >= 2:  # есть + и хотя бы одна цифра
        errmsg.set("✓ Формат верный")
    else:
        errmsg.set("")
    
    return True

root = Tk()
root.title("Проверка номера телефона")
root.geometry("350x180")

# Регистрируем функцию валидации
check = root.register(is_valid)

errmsg = StringVar()

# Подсказка формата
hint_label = ttk.Label(text="Формат: +xxxxxxxxxxx (до 11 цифр после +)", font=("Arial", 9))
hint_label.pack(padx=5, pady=5, anchor=NW)

# Поле ввода с валидацией
phone_entry = ttk.Entry(validate="key", validatecommand=(check, "%P"), width=25, font=("Arial", 11))
phone_entry.pack(padx=5, pady=5, anchor=NW)

# Метка для отображения ошибки/успеха
error_label = ttk.Label(foreground="red", textvariable=errmsg, wraplength=330, font=("Arial", 9))
error_label.pack(padx=5, pady=5, anchor=NW)

# Добавляем кнопку для проверки
def check_number():
    num = phone_entry.get()
    if re.match(r"^\+\d{1,11}$", num):
        errmsg.set("✓ Номер корректный!")
    else:
        errmsg.set("✗ Неверный формат номера")

check_btn = ttk.Button(text="Проверить номер", command=check_number)
check_btn.pack(padx=5, pady=10, anchor=NW)

root.mainloop()