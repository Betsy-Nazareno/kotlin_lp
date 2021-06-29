import ply.yacc as yacc
from kotlin_lexico import tokens


#Bug: Las restas las reconoce si pones espacio entre el número y el menos.
#Si quieren probar las expresiones sin antes agregarlas a una variable agreguen "| expression" a la primer regla


def p_cuerpo(p):
    """line : impresion SEMICOLON
                | expression
                | asignacion SEMICOLON
                | for
                | if
                """

def p_impresion(p):
    'impresion : PRINT LPAREN STRING_1 RPAREN'

def p_for(p):
    'for : FOR LPAREN ID IN ID RPAREN LCURL line RCURL'


#asignacion de variable
def p_keywordVariables(p):
    '''keywordVariables : VAR
                        | VAL'''

def p_asignacion(p):
    '''asignacion : keywordVariables asignacionSimple
                    | asignacionSimple'''

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
    'term : LPAREN expression RPAREN'

def p_factor(p):
    '''factor : INT
                | FLOAT
                | LONG
                | CHAR
                | BOOLEAN
                | ID
                | STRING_1
                '''

#-----------------------Karla------------------------------------
def p_if(p):
    '''if : IF LPAREN condicion RPAREN LCURL line RCURL
            | IF LPAREN condicion RPAREN LCURL line RCURL else
            '''

def p_else(p):
    'else : ELSE LCURL line RCURL'

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
    'condicionL : term opL term'

def p_condicionR(p):
    'condicionR : term opR term'

def p_condicionN(p):
    'condicionN : EXCL_WS term'

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