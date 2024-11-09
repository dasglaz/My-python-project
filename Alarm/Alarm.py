import time
from tkinter import  *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo

def add_alarm():
    def create_alarm():

    def alarm():
        window_alarm = Tk()
        window_alarm.title(entry_options1.get())
        window_alarm.geometry('250x250+960+430')
        label_alarm = Label(window_alarm,text=label_options2.get())
        label_alarm.pack()
        photo_alarm = PhotoImage(file=entry_options3.get())
        photography = Label(image=photo_alarm)
        photography.pack(anchor=CENTER)
        window_alarm.mainloop()

        
    window_1 = Tk()
    window_1.title('Создать новый будильник')
    window_1.geometry('250x250+960+430')

    notebook = ttk.Notebook(window_1)
    notebook.pack(fill=BOTH, expand=True)
    
    frame1 = ttk.Frame(notebook)
    frame2 = ttk.Frame(notebook)
    frame1.pack(fill=BOTH, expand=True)
    frame2.pack(fill=BOTH, expand=True)
    notebook.add(frame1,text='Основное')
    notebook.add(frame2,text='Дополнительно')

    inf = Label(frame1, text='Введите время будильника')
    inf.pack()

    hours = ['0','1', '2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
    minutes = []
    for i in range(60):
        minutes.append(str(i))
    label_hours = Label(frame1,text='Часы')
    label_hours.pack(padx=0,pady=1)
    combobox_hours = ttk.Combobox(frame1,values=hours)
    combobox_hours.pack(padx=0,pady=1)
    label_minutes = Label(frame1,text='Минуты')
    label_minutes.pack(padx=0,pady=1)
    combobox_minutes = ttk.Combobox(frame1,values=minutes)
    combobox_minutes.pack(padx=0,pady=1)

    label_options1 = Label(frame2,text='Добавить название будильника')
    label_options1.pack(anchor=NW)

    entry_options1 = ttk.Entry(frame2)
    entry_options1.pack(anchor=NW,pady=5)
    entry_options1.insert(0,'Мой будильник')

    label_options2 = Label(frame2,text='Выберите текст будильника')
    label_options2.pack(anchor=NW,pady=5)

    entry_options2 = ttk.Entry(frame2)
    entry_options2.pack(anchor=NW,pady=5)
    entry_options2.insert(0,'Будильник')

    label_options3 = Label(frame2,text='Выберите путь к картинке для вашего будильника(Указывайте корректно!)')
    label_options3.pack(anchor=NW,pady=5)

    entry_options3 = ttk.Entry(frame2)
    entry_options3.pack(anchor=NW,pady=5)

    


    window_1.mainloop()


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

