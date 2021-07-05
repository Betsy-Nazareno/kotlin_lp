import tkinter as tk

window = tk.Tk() 
window.title("Example for Tkinter")  # to define the title

canvas = tk.Canvas(window, width=450, height=500)  # define the size
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
label = tk.Label(frame,text='Analizador Sintactico', bd='3',fg='blue', font='Helvetica 9 bold').pack()  # placing labels
label1 = tk.Label(frame,text='Input', bd='1',fg='blue', font='Helvetica 9 bold').pack()
check_button1 = tk.Checkbutton(frame, text="Lexico", variable= lexico, onvalue=1, offvalue=0).pack(side=tk.TOP)
check_button2= tk.Checkbutton(frame, text="Sintactico", variable= Sintactico, onvalue=1, offvalue=0).pack()
check_button3 = tk.Checkbutton(frame, text="Semantico", variable= Semantico, onvalue=1, offvalue=0).pack()
#label1.grid(row=0,column=0)
#check_button1.grid(row=0,column=1)
#check_button2.grid(row=0,column=2)
#check_button3.grid(row=0,column=3)
entry_field1= tk.Text(frame,height = 10, width=20,bd='10')
entry_field1.pack()
analizar = tk.Button(frame, text="Analizar").pack(after=entry_field1)
label2 = tk.Label(frame,text='Output', bd='1',fg='blue', font='Helvetica 9 bold').pack()
entry_field2= tk.Text(frame,height = 10, width=20,bd='10')
entry_field2.pack()

window.mainloop()

