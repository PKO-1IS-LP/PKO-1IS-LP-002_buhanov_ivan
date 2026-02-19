# PKO-1IS-LP-002_buhanov_ivan
практическое задание работа с Tkinter

 создание приложение с виджитами и своей иконкой 
<img width="1831" height="652" alt="image" src="https://github.com/user-attachments/assets/be74212e-1b9b-47f6-ba57-ab7026a8a49c" />


получение значения параметра Text
<img width="1925" height="1141" alt="image" src="https://github.com/user-attachments/assets/85448ef5-9c55-4422-8914-0d12d9f9bf3d" />


изменения значений параметров с помощью метода config
<img width="1952" height="747" alt="image" src="https://github.com/user-attachments/assets/ae0a9d47-1e8d-4dcb-922d-bd80010641f8" />

создание кликера 
<img width="1943" height="712" alt="image" src="https://github.com/user-attachments/assets/4b646d8a-dc3a-4fc2-ac78-031729603709" />

отключение кнопки 
<img width="1962" height="742" alt="image" src="https://github.com/user-attachments/assets/ca369cbe-78cb-4f55-8fa8-725554645a8e" />

изменение фона текста кнопки 

<img width="1845" height="834" alt="image" src="https://github.com/user-attachments/assets/4baef3de-15d7-48a2-a1b0-312418fb30ac" />


виджет Lable изменение шрифта
<img width="1929" height="665" alt="image" src="https://github.com/user-attachments/assets/266f4e0c-2446-47af-9b93-84a6f7240599" />


сортировка в веденного текста по алфавиту 

<img width="1820" height="733" alt="image" src="https://github.com/user-attachments/assets/86643aff-d3e4-4a48-9868-e167bd15675f" />



практическая работа калькулятор 
<img width="2116" height="953" alt="image" src="https://github.com/user-attachments/assets/553d5c91-8b76-4f09-9075-beb0cf81d31b" />


  
текстовое поле 

<img width="1936" height="596" alt="image" src="https://github.com/user-attachments/assets/817ecd99-3211-4037-8289-da14fcefeca9" />



получение введённого текста 
![10aac5d7-8ff5-4392-9f85-745b6afa7dd6](https://github.com/user-attachments/assets/ab905a27-c3de-48f5-abd1-4705f450a30d)

часы методом insert
<img width="2541" height="1158" alt="image" src="https://github.com/user-attachments/assets/69fadc64-f8b5-4da7-bfad-225f49b0d463" />

** Entry номер телефона 

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





практическая работа цвета 
<img width="1843" height="1161" alt="image" src="https://github.com/user-attachments/assets/dde300a3-3077-4a68-96ea-49833dae9c79" />

практическая задача Task 1


from tkinter import *
from tkinter import messagebox

def show_position(position):
    # Словарь с описанием позиций
    positions = {
        "NW": "Северо-запад (верхний левый угол)",
        "N": "Север (верхний центр)",
        "NE": "Северо-восток (верхний правый угол)",
        "W": "Запад (левый центр)",
        "CENTER": "Центр",
        "E": "Восток (правый центр)",
        "SW": "Юго-запад (нижний левый угол)",
        "S": "Юг (нижний центр)",
        "SE": "Юго-восток (нижний правый угол)"
    }
    
    messagebox.showinfo("Позиция кнопки", positions[position])

root = Tk()
root.title("Расположение кнопок")
root.geometry("400x350")

# Создаем основную рамку с сеткой 3x3
main_frame = Frame(root, bd=2, relief=SUNKEN)
main_frame.pack(expand=True, fill=BOTH, padx=20, pady=20)

# Настраиваем веса для строк и столбцов
for i in range(3):
    main_frame.grid_rowconfigure(i, weight=1)
    main_frame.grid_columnconfigure(i, weight=1)

# Создаем словарь с кнопками для всех позиций
buttons = {
    "NW": (0, 0), "N": (0, 1), "NE": (0, 2),
    "W": (1, 0), "CENTER": (1, 1), "E": (1, 2),
    "SW": (2, 0), "S": (2, 1), "SE": (2, 2)
}

# Создаем все кнопки (без цвета)
for position, (row, col) in buttons.items():
    btn = Button(
        main_frame,
        text=position,
        width=8,
        height=2,
        font=("Arial", 10, "bold"),
        relief=RAISED,
        bd=2,
        command=lambda pos=position: show_position(pos)
    )
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Добавляем заголовок
title_label = Label(
    root,
    text="Нажмите на любую кнопку",
    font=("Arial", 12, "bold")
)
title_label.pack(pady=5)

root.mainloop()



<img width="2559" height="1364" alt="image" src="https://github.com/user-attachments/assets/d40a2041-4bfb-48c6-ad55-425fbf9faf2f" />



практическая задача Task 2

<img width="1830" height="861" alt="image" src="https://github.com/user-attachments/assets/53c78a3a-c1ea-462f-bf57-259db2fb6056" />



