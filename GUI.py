import tkinter as tk
from kotlin_sintactico import *
from kotlin_lexico import *

WIN_WIDTH = 430
WIN_HEIGHT = 575


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


logo = tk.PhotoImage(file='kotlin_logo.png')
logo = logo.subsample(12)
logo_label = tk.Label(frame, image=logo).grid(sticky='W',row=0,column=0,columnspan=1)
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
entry_field1= tk.Text(frame,height = 12, width=47,bd='2')
entry_field1.grid(sticky = 'W', row=2, column=0, columnspan=4)
entry_field1.config(state='normal')
analizar = tk.Button(frame, text="Analizar", command=lambda: getValue(entry_field1.get("1.0", "end-1c"))).grid(sticky = 'W', padx=100, pady=10, row=3, column=1,columnspan=4)
clear_button = tk.Button(frame, text="Limpiar", command=lambda: entry_field1.delete("1.0", "end-1c")).grid(sticky = 'E',pady=10, padx=3, row=3, column=3,columnspan=1)


#output field
label2 = tk.Label(frame,text='Output', bd='1',fg='black', font='Helvetica 9 bold').grid(sticky = 'W',pady=10,row=4, column=0,columnspan=1)
p1 = tk.StringVar(frame, "")
v = tk.Scrollbar(frame, orient='vertical')
t = tk.Text(frame, height = 10, width=48, bd='5', wrap=tk.WORD, yscrollcommand=v.set, borderwidth=2, relief="groove")
t.insert(tk.END, p1.get())
t.grid(sticky='W',row=5, column=0, columnspan=4)
v.config(command=t.yview)

#cadena del input a analizar
def getValue(cadena):
    s=""
    try:
        s = cadena
    except EOFError:
        p1.set("EOFError")
    t.configure(state='normal')
    p1.set("")
    t.delete("1.0", "end")
    if s and lexico.get() and (Sintactico.get() or Semantico.get()):
        analizar_lex_sintax(s)
    elif s and (Sintactico.get() or Semantico.get()):
        analizar_sintactico(s)
    elif s and lexico.get():
       analizar_lexico(s)
    elif s:
        p1.set('Seleccione un tipo de análisis')
    t.insert(tk.END, p1.get())
    t.configure(state='disabled')


def analizar_sintactico(s):
    lexer.lineno = 1
    parser.parse(s, lexer=lexer, tracking=True)
    p1.set(cola[-1])
    cola.clear()
    cola.append("¡Perfecto, es una sintáxis de kotlin limpia!")

def analizar_lexico(s):
    lista_tokens.clear()
    lexer.input(s)
    getTokens(lexer)
    lexer.lineno = 1
    for i in lista_tokens:
        if (i.find('LINEBREAK') != -1):
            lexer.lineno += 1
        elif (i.find('Illegal') != -1):
            p1.set(p1.get() + "[ERROR] Linea " + str(lexer.lineno) + ": " + i + '\n')
        else:
            p1.set(p1.get() + "Linea " + str(lexer.lineno) + ": " + i + '\n')
    lista_tokens.clear()

def analizar_lex_sintax(s):
    lexer.lineno = 1
    parser.parse(s, lexer=lexer)
    p1.set(cola[-1] + '\n')
    analizar_lexico(s)
    cola.clear()
    cola.append("¡Perfecto, es una sintáxis de kotlin limpia!")


window.mainloop()

