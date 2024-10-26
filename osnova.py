from tkinter import *
from time import sleep
from random import randint

def sort_labels(labels_number, sort):
    global label_count

    if label_count == 'stand':

        for i in range(len(labels_number)):
            labels_number[i].place_forget()

        labels_number.sort(key=lambda label: int(label['text'].split(')')[1].strip()), reverse=True)


        for i in range(len(labels_number)):
            if i < 10:
                labels_number[i].place(x = 10 , y = 30 * (i + 1) + 40)
            elif i > 9 and i < 20:
                labels_number[i].place(x=210, y=30 * ( i - 10 + 1) + 40)
            elif i > 19:
                labels_number[i].place(x=410, y=30 * (i - 20 + 1) + 40)

        label_count = 'up'
        sort.configure(fg='green')
    elif label_count == 'up':
        for i in range(len(labels_number)):
            labels_number[i].place_forget()

        labels_number.sort(key=lambda label: int(label['text'].split(')')[1].strip()))


        for i in range(len(labels_number)):
            if i < 10:
                labels_number[i].place(x=10, y=30 * (i + 1) + 40)
            elif i > 9 and i < 20:
                labels_number[i].place(x=210, y=30 * (i - 10 + 1) + 40)
            elif i > 19:
                labels_number[i].place(x=410, y=30 * (i - 20 + 1) + 40)

        label_count = 'down'
        sort.configure(fg='red')
    else:
        for i in range(len(labels_number)):
            labels_number[i].place_forget()

        labels_number.sort(key=lambda label: int(label['text'].split(')')[0].strip()))


        for i in range(len(labels_number)):
            if i < 10:
                labels_number[i].place(x=10, y=30 * (i + 1) + 40)
            elif i > 9 and i < 20:
                labels_number[i].place(x=210, y=30 * (i - 10 + 1) + 40)
            elif i > 19:
                labels_number[i].place(x=410, y=30 * (i - 20 + 1) + 40)

        label_count = 'stand'
        sort.configure(fg='gray')

    root.update()
def new_menu_window(label, add, stats, menu, new_menu, sort, labels_number, all_exersise):

    global foto_menu

    all_exersise.place_forget()
    new_menu.place_forget()
    sort.place_forget()
    for i in range(len(labels_number)):
        labels_number[i].place_forget()

    label.place(x=50, y=20)

    menu.place(x=500, y=25)

    add.place(x=75, y=150)

    stats.place(x=375, y=150)

def stats_window(subject, exersise, menu,label, add, stats):

    global foto_menu, label_count

    label.place_forget()
    menu.place_forget()
    add.place_forget()
    stats.place_forget()

    new_menu = Button(root, image=foto_menu, bg='black', bd=0, command=lambda: new_menu_window(label, add, stats, menu, new_menu, sort, labels_number, all_exersise))
    new_menu.place(x = 500, y = 10)

    sort = Button(root, text='Сортировка', bg='black', fg='gray', bd=0, font=("Colibry",25), command=lambda: sort_labels(labels_number, sort))
    sort.place(x = 10, y = 5)




    file = open(f'{subject}.txt', 'r')
    all_result = file.read()
    file.close()

    all_result = all_result.split()

    all_exersise = Label(root, text=f"Решено: {all_result[-1]}", bg='black', fg='white', bd=0, font=("Colibry",25))
    all_exersise.place(x = 250, y = 20)

    labels_number = []
    for i in range(exersise):
        labels_number.append(f'labels{i + 1}')

    for i in range(exersise):
        labels_number[i] = Label(root, text=f"{i + 1}) {all_result[i]}", bg='black', fg='white',
                                 font=("Colibry", 18))
        if int(all_result[i]) <= int(all_result[-1]) / 3:
            labels_number[i].configure(fg='red')

        elif int(all_result[-1]) / 3 < int(all_result[i]) <= int(all_result[-1]) / 1.5:
            labels_number[i].configure(fg='yellow')

        else:
            labels_number[i].configure(fg='green')


    for i in range(exersise):
        if i < 10:
            labels_number[i].place(x = 10 , y = 30 * (i + 1) + 40)
        elif i > 9 and i < 20:
            labels_number[i].place(x=210, y=30 * ( i - 10 + 1) + 40)
        elif i > 19:
            labels_number[i].place(x=410, y=30 * (i - 20 + 1) + 40)

    label_count = 'stand'
def saving(save,result_list,subject, save_button,reset_button, exersise):
    if save:
        file = open(f'{subject}.txt', 'r')
        all_result = file.read()
        all_result = all_result.split()
        file.close()

        for i in range(exersise):
            all_result[i] = str(int(all_result[i]) + int(result_list[i]))
        all_result[-1] = str(int(all_result[-1]) + 1)

        all_result = ' '.join(all_result)
        file = open(f'{subject}.txt', 'w')
        file.write(all_result)
        file.close()

        result_list.clear()
        save_button.place_forget()
        reset_button.place_forget()

        if subject == "математика":
            math()
        elif subject == 'русский':
            russia()
        elif subject == 'информатика':
            it()
        elif subject == 'физика':
            phisic()

    else:
        result_list.clear()
        save_button.place_forget()
        reset_button.place_forget()

        if subject == "математика":
            math()
        elif subject == 'русский':
            russia()
        elif subject == 'информатика':
            it()
        elif subject == 'физика':
            phisic()



def add_grade(grade,exersise,exersise_number,result_list,zero_button, one_button, subject):

    global count, save_foto, unsave_foto

    result_list.append(grade)
    exersise_number.configure(fg=['red','green'][grade])
    root.update()
    sleep(0.5)
    count += 1
    if count <= exersise:
        exersise_number.configure(fg='white', text=count)
        root.update()

    if count == exersise + 1:
        exersise_number.place_forget()
        zero_button.place_forget()
        one_button.place_forget()

        count = 1

        reset_button = Button(root, image=unsave_foto,text="Сбросить", compound=CENTER,bg='black',bd=0,
                        font=("Colibry",35), command=lambda: saving(False,result_list,subject, save_button,reset_button, exersise))
        reset_button.place(x = 180, y = 40)

        save_button = Button(root, image=save_foto ,text="Сохранить", compound=CENTER,bg='black', bd=0,
                       font=("Colibry",35), command=lambda: saving(True,result_list,subject, save_button,reset_button, exersise))
        save_button.place(x = 175, y = 220)


def add_window(subject, exersise,menu , label, add, stats):
    global yes, no
    menu.place_forget()
    label.place_forget()
    add.place_forget()
    stats.place_forget()

    one_button = Button(root, bd=0, bg='black', image=yes ,
                        command=lambda: add_grade(1,exersise,exersise_number,result_list, zero_button, one_button, subject))
    one_button.place(x = 80, y = 180)

    zero_button = Button(root, bd=0, bg='black', image=no ,
                         command=lambda: add_grade(0,exersise,exersise_number,result_list,zero_button, one_button, subject))
    zero_button.place(x=380, y=180)

    result_list = []

    exersise_number = Label(root, text=count, bg='black', fg='white', font=('Colibry', 80, 'underline'))
    exersise_number.place(x=250, y=20)








def close_menu(menu ,label, add, stats):
    menu.place_forget()
    label.place_forget()
    add.place_forget()
    stats.place_forget()

    menu_window()





def math():
    global foto_menu, foto_add, foto_stats
    menu = Button(root, image=foto_menu, bg = 'black', bd = 0,command=lambda: close_menu(menu ,math_label, add, stats))
    add = Button(root, image=foto_add, bg = 'black', bd = 0, command=lambda: add_window('математика', 19,menu ,math_label, add, stats),
                 text= "Добавить",fg='white',compound='top', font=("Colibry", 15))
    stats = Button(root, image=foto_stats, bg = 'black', bd = 0, command=lambda: stats_window('математика', 19, menu, math_label, add, stats),
                   text= "Статистика",fg='white',compound='top', font=("Colibry", 15))

    math_label = Label(root, text="Математика", bg = 'black', fg = 'white',
                       font=("Colibri",50, 'underline'))
    math_label.place(x = 50, y = 20)

    menu.place(x=500,y=25)

    add.place(x = 75, y = 150)

    stats.place(x = 375, y = 150)


def russia():
    global foto_menu, foto_add, foto_stats
    menu = Button(root, image=foto_menu, bg = 'black', bd = 0,command=lambda: close_menu(menu ,math_label, add, stats))
    add = Button(root, image=foto_add, bg = 'black', bd = 0, command=lambda: add_window('русский', 26,menu ,math_label, add, stats),
                 text= "Добавить",fg='white',compound='top', font=("Colibry", 15))
    stats = Button(root, image=foto_stats, bg = 'black', bd = 0, command=lambda: stats_window('русский', 26, menu, math_label, add, stats),
                   text= "Статистика",fg='white',compound='top', font=("Colibry", 15))

    math_label = Label(root, text="Русский", bg = 'black', fg = 'white',
                       font=("Colibri",50, 'underline'))
    math_label.place(x = 50, y = 20)

    menu.place(x=500,y=25)

    add.place(x = 75, y = 150)

    stats.place(x = 375, y = 150)


def it():
    global foto_menu, foto_add, foto_stats
    menu = Button(root, image=foto_menu, bg = 'black', bd = 0,command=lambda: close_menu(menu ,math_label, add, stats))
    add = Button(root, image=foto_add, bg = 'black', bd = 0, command=lambda: add_window('информатика', 27,menu ,math_label, add, stats),
                 text= "Добавить",fg='white',compound='top', font=("Colibry", 15))
    stats = Button(root, image=foto_stats, bg = 'black', bd = 0, command=lambda: stats_window('информатика', 27, menu, math_label, add, stats),
                   text= "Статистика",fg='white',compound='top', font=("Colibry", 15))

    math_label = Label(root, text="Информатика", bg = 'black', fg = 'white',
                       font=("Colibri",50, 'underline'))
    math_label.place(x = 50, y = 20)

    menu.place(x=500,y=25)

    add.place(x = 75, y = 150)

    stats.place(x = 375, y = 150)


def phisic():
    global foto_menu, foto_add, foto_stats
    menu = Button(root, image=foto_menu, bg = 'black', bd = 0,command=lambda: close_menu(menu ,math_label, add, stats))
    add = Button(root, image=foto_add, bg = 'black', bd = 0, command=lambda: add_window('физика', 30,menu ,math_label, add, stats),
                 text= "Добавить",fg='white',compound='top', font=("Colibry", 15))
    stats = Button(root, image=foto_stats, bg = 'black', bd = 0, command=lambda: stats_window('физика', 30, menu, math_label, add, stats),
                   text= "Статистика",fg='white',compound='top', font=("Colibry", 15))

    math_label = Label(root, text="Физика", bg = 'black', fg = 'white',
                       font=("Colibri",50, 'underline'))
    math_label.place(x = 50, y = 20)

    menu.place(x=500,y=25)

    add.place(x = 75, y = 150)

    stats.place(x = 375, y = 150)



def subjects(subject):
    global foto, math_button, russia_button, it_button, phisic_button
    math_button.place_forget()
    russia_button.place_forget()
    it_button.place_forget()
    phisic_button.place_forget()


    if subject == 'математика':
        math()
    elif subject == 'русский':
        russia()
    elif subject == 'информатика':
        it()
    elif subject == 'физика':
        phisic()


def menu_window():
    global foto, math_button, russia_button, it_button, phisic_button

    math_button.place(x=100, y=25)
    russia_button.place(x = 100, y = 125)
    it_button.place(x = 100, y = 225)
    phisic_button.place(x = 100, y = 325)


    root.update()


def button_start():
    global start_rectangle, start_but, start_button
    start_but = False
    canvas.delete(start_rectangle)
    start_button.place_forget()
    root.update()
    if not start_but:
        sleep(0.5)
        menu_window()
    else:
        sleep(0.5)
        start_but = False
        menu_window()
#Start window
def start_window(text):
    global start_rectangle, start_but, start_button
    root.update()
    sleep(0.5)
    start_message1 = Label(root, text=text.split()[0], bg='black', fg='white', font=('Verdana', 30, 'underline'))
    start_message1.place(x=20,y=20)

    start_message2 = Label(root, text=text.split()[1], bg='black', fg='black', font=('Verdana', 50))
    start_message2.place(x=145, y=170)


    for i in range(60):
        canvas.move(start_rectangle, 0, -5)
        root.update()
        sleep(0.005)

    start_message2.configure(fg = 'white')
    root.update()
    sleep(1)

    start_message1.place_forget()
    start_message2.place_forget()

    start_button.place(x = 180, y = 150)
    a = 0
    while start_but:
        a = randint(0,5)
        canvas.itemconfig(start_rectangle, fill = ['red','blue','green','yellow','brown','white'][a])
        start_button.configure(fg=['red','blue','green','yellow','brown','white'][a])
        sleep(0.1)
        root.update()
#Создание окна

root = Tk()
root.title("Подготовка к ЕГЭ")
root.geometry("600x400+400+100")
root.resizable(0,0)

canvas = Canvas(root, width=600, height=400, bg='black')
canvas.pack()

start_rectangle = canvas.create_rectangle(0,430,600,590, fill='white')
start_but = True
start_button = Button(root, text="Start", bg='black', bd = 0, fg='white', font=('Verdana', 45),
                          width=6, height=1, command=button_start)

foto = PhotoImage(file = 'foto.png')

math_button = Button(root, image = foto, text="Математика", fg = 'black', compound=CENTER,
                     font=('Verdana',25), bg='black', bd = 0, command=lambda: subjects('математика'))

russia_button = Button(root, image = foto, text="Русский", fg = 'black', compound=CENTER,
                     font=('Verdana',25), bd = 0, bg='black', command=lambda: subjects('русский'))

it_button = Button(root, image = foto, text="Информатика", fg = 'black', compound=CENTER,
                     font=('Verdana',25), bd = 0, bg='black', command=lambda: subjects('информатика'))

phisic_button = Button(root, image = foto, text="Физика", fg = 'black', compound=CENTER,
                     font=('Verdana',25), bd = 0, bg='black', command=lambda: subjects('физика'))

foto_menu = PhotoImage(file = 'menu.png')
foto_add = PhotoImage(file='add.png')
foto_stats = PhotoImage(file='stats.png')
count = 1
label_count = ''

save_foto = PhotoImage(file='save.png')
unsave_foto = PhotoImage(file='unsave.png')

yes = PhotoImage(file='yes.png')
no = PhotoImage(file='no.png')



if __name__ == '__main__':
    start_window("Разработчик: ilkin2121")

root.mainloop()