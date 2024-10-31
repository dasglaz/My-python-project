import time
from tkinter import  *
from tkinter import ttk

def autorise():
    name = name_entry.get()
    label['text'] = f"{name} авторизован"
    label_name['text'] = name



window = Tk()
window.title("Будильник")
window.geometry("300x300+960+430")

greet = ttk.Label(text="Добро пожаловать, введите своё имя",font=('Times New Roman', 12))
greet.pack()

name_entry = ttk.Entry(foreground='blue')
name_entry.pack()
name_entry.focus()

button_autorise = ttk.Button(text="Авторизовать",command=autorise)
button_autorise.pack()

label = ttk.Label()
label.pack()

label_name = ttk.Label()


window.mainloop()

