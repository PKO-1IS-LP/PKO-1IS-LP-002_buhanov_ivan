from tkinter import *
from tkinter import messagebox

def check_login():
    if user.get() == "ivanbuhanov" and pwd.get() == "02042002":
        messagebox.showinfo("Успех", "Добро пожаловать!")
    else:
        messagebox.showerror("Ошибка", "Неверный логин или пароль")

root = Tk()
root.title("Авторизация")
root.geometry("300x200")

Label(root, text="Вход в систему", font=("Arial", 14)).pack(pady=10)

frame = Frame(root)
frame.pack(pady=10)

Label(frame, text="Логин:").grid(row=0, column=0, pady=5)
user = Entry(frame)
user.grid(row=0, column=1, pady=5)

Label(frame, text="Пароль:").grid(row=1, column=0, pady=5)
pwd = Entry(frame, show="*")
pwd.grid(row=1, column=1, pady=5)

Button(root, text="Войти", command=check_login).pack(pady=10)

root.mainloop()