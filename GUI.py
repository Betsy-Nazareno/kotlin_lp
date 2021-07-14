import tkinter as tk
from kotlin_sintactico import *
from kotlin_lexico import lexer

WIN_WIDTH = 430
WIN_HEIGHT = 553


window = tk.Tk() 
window.title("Proyecto LP")  # to define the title
#window.config(cursor= 'heart')
canvas = tk.Canvas(window, width=WIN_WIDTH, height=WIN_HEIGHT)  # define the size
canvas.pack()
frame = tk.Frame(window)

#set window at the center of the screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_win_coord = int((screen_width/2) - (WIN_WIDTH/2))
y_win_coord = int((screen_height/2) - (WIN_HEIGHT/2))
window.geometry("{}x{}+{}+{}".format(WIN_WIDTH, WIN_HEIGHT, x_win_coord, y_win_coord))


frame.place(relx=0.05, rely=0, relwidth=0.9, relheight=0.9)
menu = tk.Menu(window)
lexico = tk.IntVar() 
Sintactico = tk.IntVar() 
Semantico = tk.IntVar() 
window.config(menu=menu)

# menu cascade
#subMenu_exit = tk.Menu(menu)
#menu.add_cascade(label="Exit_menu", menu=subMenu_exit)
#subMenu_exit.add_command(label="Exit", command=window.destroy)

label = tk.Label(frame,text='Analizador del Lenguaje Kotlin', bd='3',fg='black', font='Helvetica 12 bold').grid(row=0,column=0,columnspan=4)  # placing labels

#checks 
check_button1 = tk.Checkbutton(frame, text="Léxico", variable= lexico, onvalue=1, offvalue=0)
check_button2= tk.Checkbutton(frame, text="Sintáctico", variable= Sintactico, onvalue=1, offvalue=0)
check_button3 = tk.Checkbutton(frame, text="Semántico", variable= Semantico, onvalue=1, offvalue=0)
check_button1.grid(pady=10,row=1,column=1, columnspan=1)
check_button2.grid(pady=10,row=1,column=2, columnspan=1)
check_button3.grid(pady=10,row=1,column=3, columnspan=1)

#input field
label1 = tk.Label(frame,text='Input', bd='1',fg='black', font='Helvetica 9 bold').grid(sticky = 'W',pady=10,row=1,column=0, columnspan=1)
entry_field1= tk.Text(frame,height = 12, width=47,bd='5')
entry_field1.grid(sticky = 'W', row=2, column=0, columnspan=4)
analizar = tk.Button(frame, text="Analizar", command=lambda: getValue(entry_field1.get("1.0", "end-1c"))).grid(sticky = 'W', padx=100, pady=10, row=3, column=1,columnspan=4)
clear_button = tk.Button(frame, text="Limpiar", command='').grid(sticky = 'E',pady=10, padx=3, row=3, column=3,columnspan=1)
#output field
label2 = tk.Label(frame,text='Output', bd='1',fg='black', font='Helvetica 9 bold').grid(sticky = 'W',pady=10,row=4, column=0,columnspan=1)
p1 = tk.StringVar(frame, "Resultado")
print("Valor de ", p1)
result_label= tk.Label(frame,height = 10, width=54,bd='5', textvariable=p1)
result_label.configure(bg='white',  borderwidth=2, relief="groove")
result_label.grid(sticky='W',row=5, column=0, columnspan=4)

#men_error = ""


#cadena del input a analizar
def getValue(cadena):
    try:
        s = cadena
    except EOFError:
        print("EOFError")
    if s:
        parser.parse(s, lexer=lexer)
        p1.set(cola[-1])
        cola.clear()
        cola.append("¡Everything it's ok!")


window.mainloop()

