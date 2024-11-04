import time
from tkinter import  *
from tkinter import ttk

def add_alarm():
    window_1 = Tk()
    window_1.title('Создать новый будильник')
    window_1.geometry('250x250+960+430')

    

def autorise():
    name = name_entry.get()
    label['text'] = f"Добрый день, {name}! "



window = Tk()
window.title("Будильник")
window.geometry("300x300+960+430")

greet = ttk.Label(text="Добро пожаловать, введите свое имя",font=('Times New Roman', 12))
greet.pack()

name_entry = ttk.Entry(foreground='blue')
name_entry.pack()
name_entry.focus()

button_autorise = ttk.Button(text="OK",command=autorise)
button_autorise.pack()

label = ttk.Label()
label.pack()

frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])

plus = ttk.Button(master=frame,text="+",width=2, command=add_alarm)
plus.pack(anchor="nw")

frame.pack(anchor="center", fill="x")


window.mainloop()

