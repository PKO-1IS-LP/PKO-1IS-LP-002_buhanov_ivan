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