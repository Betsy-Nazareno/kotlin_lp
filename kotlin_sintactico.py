import ply.yacc as yacc
from kotlin_lexico import *

cola = ["Everything is ok!"]

def p_cuerpo(p):
    """line : blocks
                | blocks SEMICOLON
                | blocks LINEBREAK
                | blocks LINEBREAK line
                | blocks LINEBREAK line LINEBREAK
                | blocks SEMICOLON LINEBREAK
                | blocks SEMICOLON LINEBREAK line
                | blocks SEMICOLON LINEBREAK line LINEBREAK
                | LINEBREAK
                """

def p_body(p):
    """blocks : impresion
                | expression
                | asignacion
                | estructurasControl
                | condicion
                | funcion
                | estructurasDatos"""


#def p_body_lineas(p):
#    """lineas : blocks
#            | blocks SEMICOLON"""


def p_estructuras_datos(p):
    """estructurasDatos : queue
                        | queue_operations
                        | stack
                        | stack_actuar
                        | instance_linkedlist
                        | def_estruct_tipoDato
                        | lista
                        | lsimplem
                        | lcomp

                         """

def p_estructuras_control(p):
    """estructurasControl : for
                         | if
                         | while """


def p_queue_operations(p):
    '''queue_operations : queue_add
                        | queue_peek
                        | queue_remove
                        | queue_poll'''


def p_queue_add(p):
    '''queue_add : ID DOT ADD LPAREN factor RPAREN'''


def p_queue_peek(p):
    '''queue_peek : ID DOT PEEK LPAREN RPAREN'''


def p_queue_poll(p):
    '''queue_poll : ID DOT POLL LPAREN RPAREN'''


def p_queue_remove(p):
    '''queue_remove : ID DOT REMOVE LPAREN RPAREN'''


def p_impresion(p):
    '''impresion : PRINT LPAREN expression RPAREN
                |  PRINTLN LPAREN expression RPAREN'''

def p_asignacion(p):
    '''asignacion : keywordVariables asignacionSimple
                    | asignacionSimple'''


def p_keywordVariables(p):
    '''keywordVariables : VAR
                        | VAL
                        '''



def p_asignacionS(p):
    '''asignacionSimple : ID DOTS tipoDatoEspecifico
                        | ID EQUAL valor'''


def p_tipoDatoEspecifico(p):
    '''tipoDatoEspecifico : TINT EQUAL INT
                            | TLONG EQUAL LONG
                            | TFLOAT EQUAL FLOAT
                            | TBOOLEAN EQUAL BOOLEAN
                            | TCHAR EQUAL CHAR
                            | TSTRING EQUAL STRING_1'''


def p_tipoDato(p):
    '''tipoDato : TINT
                | TLONG
                | TFLOAT
                | TDOUBLE
                | TBOOLEAN
                | TCHAR
                | TSTRING'''


def p_queue(p):
    'queue : keywordVariables ID DOTS QUEUE LANGLE tipoDato RANGLE EQUAL LINKEDL LANGLE tipoDato RANGLE LPAREN RPAREN'


def p_for(p):
    '''for : FOR LPAREN ID IN iterable RPAREN LCURL lineorBreak RCURL  '''


def p_iterable(p):
    """iterable : ID
                | INT THREEDOTS INT
                | ID DOT INDICES"""


#def p_morelines(p):
#    '''morelines : line
#                | line morelines'''





def p_valor(p):
    '''valor : expression'''


def p_expression_plus(p):
    "expression : expression PLUS term"


def p_expression_minus(p):
    'expression : expression MINUS term'


def p_expression_times(p):
    'expression : expression TIMES term'


def p_expression_divide(p):
    'expression : expression DIVIDE term'


def p_expression_mod(p):
    'expression : expression MOD term'


def p_expression_increment(p):
    'expression : expression INCREMENTONE'


def p_expression_decrement(p):
    'expression : expression DECREMENTONE'


def p_expression_single(p):
    '''expression : term'''


def p_term_factor(p):
    """term : factor"""


def p_term_Paren(p):
    '''term : LPAREN expression RPAREN'''


def p_factor(p):
    '''factor : INT
                | FLOAT
                | LONG
                | CHAR
                | BOOLEAN
                | ID
                | STRING_1
                '''


# ---------- Karla -------------
def p_funcion(p):
    '''funcion : FUN ID LPAREN RPAREN LCURL lineorBreak RCURL
                | FUN ID LPAREN ID RPAREN LCURL lineorBreak RCURL
                | FUN ID LPAREN ID RPAREN LCURL RCURL
                | FUN ID LPAREN RPAREN LCURL RCURL
    '''

def p_lineorBreak(p):
    ''' lineorBreak : line
                    | LINEBREAK line LINEBREAK
                    | LINEBREAK line
    '''

def p_if(p):
    '''if : IF LPAREN condicion RPAREN LCURL lineorBreak RCURL
            | IF LPAREN condicion RPAREN LCURL lineorBreak RCURL else
            '''

def p_else(p):
    'else : ELSE LCURL lineorBreak RCURL'

#condiciones del if
# ((<datos> (<operadorL> | <operadorR>)) | <operadorN>) <datos>

#condicionL : condicion con operadores logicos
#condicionR : condicion con operadores relacionales
#condicionN : negar expresion, p.e: !variable

def p_condicion(p):
    '''condicion : condicionL
                | condicionR
                | condicionN
                '''

def p_condicionL(p):
    '''condicionL : BOOLEAN opL BOOLEAN
                    | ID opL ID
                    | ID opL BOOLEAN
                    | BOOLEAN opL ID
                    '''

def p_condicionR(p):
    '''condicionR : INT opR INT
                    | INT opR FLOAT
                    | INT opR LONG
                    | INT opR ID
                    | FLOAT opR FLOAT
                    | FLOAT opR INT
                    | FLOAT opR LONG
                    | FLOAT opR ID
                    | LONG opR LONG
                    | LONG opR INT
                    | LONG opR FLOAT
                    | LONG opR ID
                    | STRING_1 opR STRING_1
                    | STRING_1 opR ID
                    | CHAR opR CHAR
                    | CHAR opR ID
                    | ID opR ID
                    | ID opR INT
                    | ID opR FLOAT
                    | ID opR LONG
                    | ID opR STRING_1
                    | ID opR CHAR
                    '''

def p_condicionN(p):
    '''condicionN : EXCL_WS BOOLEAN
                    | EXCL_WS ID
                    '''

#operaciones logicos y relacionales
def p_opL(p):
    '''opL : CONJ
            | DISJ
            '''

def p_opR(p):
    '''opR : LANGLE
            | RANGLE
            | LE
            | GE
            | EXCL_EQ
            | EXCL_EQEQ
            | AS_SAFE
            | EQEQ
            | EQEQEQ
            '''

# ---------------- STACK ---------------
# <pila> ::= "var " <variable> ": Stack<" <tipoDato> ">" "=" "LinkedList()"
def p_stack(p):
    'stack : keywordVariables ID DOTS def_estruct_tipoDato EQUAL instance_linkedlist'


# Stack<" <tipoDato> ">"
def p_def_estruct_dato(p):
    'def_estruct_tipoDato : STACK LANGLE tipoDato RANGLE'


# ArrayList()
def p_instance_linkedList(p):
    'instance_linkedlist : LINKEDL LPAREN RPAREN'


# ejecutar funciones para pilas
def p_stack_actuar(p):
    'stack_actuar : ID DOT stack_funciones'


# funciones pilas
def p_stack_funciones(p):
    ''' stack_funciones : stack_isEmpty
                        | stack_push
                        | stack_pop
                        | stack_peek
                        | stack_size
                        '''


def p_stack_isEmpty(p):
    'stack_isEmpty : ISEMPTY LPAREN RPAREN'


def p_stack_pop(p):
    'stack_pop : POP LPAREN RPAREN'


def p_stack_push(p):
    'stack_push : PUSH LPAREN factor RPAREN'


def p_stack_peek(p):
    'stack_peek : PEEK LPAREN RPAREN'


def p_stack_size(p):
    'stack_size : SIZE LPAREN RPAREN'


# EDDY

def p_Lmetod(p):
    '''Lmetod : FIRST LPAREN RPAREN
    | LAST LPAREN RPAREN
    | REMOVEL LPAREN RPAREN
                '''


def p_Cmetod(p):
    '''Cmetod : APPEND LPAREN OBJECT RPAREN
    | REMOVEN LPAREN OBJECT RPAREN
    | REMOVEI LPAREN TINT RPAREN

                '''


def p_while(p):
    'while : WHILE LPAREN ID opR INT RPAREN LCURL lineorBreak RCURL '


def p_lista(p):
    'lista : keywordVariables ID DOTS LINKEDL LANGLE OBJECT RANGLE EQUAL LINKEDL LANGLE OBJECT RANGLE LPAREN RPAREN'


def p_lsimplem(p):
    'lsimplem : ID DOT Lmetod'


def p_lcomp(p):
    'lcomp : ID DOT Cmetod'


# Error rule for syntax errors
def p_error(p):
    if p:
        cola.append("Syntax ERROR: Token "+ str(p.value) +" de tipo "+ p.type + " no está permitido!")
    else:
        cola.append("EOF: Error at the end of the line. \nYour line is incomplete. Try again!")



# Build the parser
parser = yacc.yacc()
'''
while True:
    try:
        s = input("kotlin > ")
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
'''