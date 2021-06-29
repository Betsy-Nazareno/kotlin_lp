import ply.yacc as yacc
from kotlin_lp.kotlin_lexico import tokens


#Bug: Las restas las reconoce si pones espacio entre el número y el menos.
#Si quieren probar las expresiones sin antes agregarlas a una variable agreguen "| expression" a la primer regla



def p_cuerpo(p):
    """line : impresion SEMICOLON
                | asignacion SEMICOLON
                | expression
                | estructurasControl
                | estructurasDatos SEMICOLON
                """
def p_estructuras_datos(p):
    """estructurasDatos : queue
                        | queue_operations"""

def p_estructuras_control(p):
    """estructurasControl : for"""



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
    'impresion : PRINT LPAREN RPAREN'

def p_queue(p):
    '''queue : VAL ID DOTS QUEUE LANGLE tipoDato RANGLE EQUAL LINKEDLIST  LANGLE tipoDato RANGLE LPAREN RPAREN'''

def p_for(p):
    '''for : FOR LPAREN ID IN ID RPAREN LCURL morelines RCURL  '''

def p_morelines(p):
    '''morelines : line
                | line morelines'''

def p_asignacion(p):
    '''asignacion : keywordVariables asignacionSimple
                    | asignacionSimple'''

def p_keywordVariables(p):
    '''keywordVariables : VAR
                        | VAL'''

def p_asignacionS(p):
    '''asignacionSimple : ID DOTS tipoDato EQUAL valor
                        | ID EQUAL valor'''


def p_tipoDato(p):
    '''tipoDato : TINT
                | TLONG
                | TFLOAT
                | TDOUBLE
                | TBOOLEAN
                | TCHAR
                | TSTRING'''

def p_valor(p):
    '''valor : expression'''

def p_op_logica(p):
    '''opLogica : opLogica LANGLE term'''

def p_op_logica_fin(p):
    '''opLogica : term'''




def p_expression(p):
    '''expression : expression
                  | opLogica'''


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

def p_expression_single(p):
    '''expression : term'''

def p_term_factor(p):
    """term : factor"""

def p_term_Paren(p):
    '''term : LPAREN expression RPAREN
            | LPAREN opLogica RPAREN'''

def p_factor(p):
    '''factor : INT
                | FLOAT
                | LONG
                | CHAR
                | BOOLEAN
                | ID
                | STRING_1
                '''




# Error rule for syntax errors
def p_error(p):
    if p:
        print("Syntax error at token", p.type)
        # Just discard the token and tell the parser it's okay.
    else:
        print("Syntax error at EOF")
# Build the parser
parser = yacc.yacc()


while True:
    try:
        s = input("kotlin > ")
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
