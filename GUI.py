import tkinter as tk

window = tk.Tk() 
window.title("Proyecto LP")  # to define the title
window.config(cursor= 'heart')
canvas = tk.Canvas(window, width=550, height=550)  # define the size
canvas.pack()
frame = tk.Frame(window)

frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)
menu = tk.Menu(window)
lexico = tk.IntVar() 
Sintactico = tk.IntVar() 
Semantico = tk.IntVar() 
window.config(menu=menu)
subMenu_exit = tk.Menu(menu)
menu.add_cascade(label="Exit_menu", menu=subMenu_exit)
subMenu_exit.add_command(label="Exit", command=window.destroy)
label = tk.Label(frame,text='Analizador del Lenguaje Kotlin', bd='3',fg='blue', font='Helvetica 9 bold').grid(column=1)  # placing labels
label1 = tk.Label(frame,text='Input', bd='1',fg='blue', font='Helvetica 9 bold').grid(column=1)
check_button1 = tk.Checkbutton(frame, text="Lexico", variable= lexico, onvalue=1, offvalue=0)
check_button2= tk.Checkbutton(frame, text="Sintactico", variable= Sintactico, onvalue=1, offvalue=0)
check_button3 = tk.Checkbutton(frame, text="Semantico", variable= Semantico, onvalue=1, offvalue=0)
#check_button1.pack(side= 'right', after=label1)
#check_button2.pack(side= 'right', before=label1)
#check_button3.pack(side= 'right',before=label1)
#label1.grid(row=0,column=0)
check_button1.grid(row=2,column=0)
check_button2.grid(row=2,column=1)
check_button3.grid(row=2,column=2)
entry_field1= tk.Text(frame,height = 10, width=30,bd='10')
entry_field1.grid(column=1)
analizar = tk.Button(frame, text="Analizar").grid(column=1)
label2 = tk.Label(frame,text='Output', bd='1',fg='blue', font='Helvetica 9 bold').grid(column=1)
entry_field2= tk.Text(frame,height = 10, width=30,bd='10')
entry_field2.grid(column=1)

window.mainloop()

