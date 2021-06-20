import ply.lex as lex
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'var': 'VAR',
    'val': 'VAL',
    'fun': 'FUN',
    'return': 'RETURN',
    'in': 'IN',
    'is': 'IS',
    'when': 'WHEN'
}
tokens = (
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    "MOD",
    "ID",
    'EQUAL',#Aporte de Betsy--------------------------------------------------------------------------------------------
    'DOTS',
    'INCREMENTONE',
    'DECREMENTONE',
    'INCREMENTIN',
    'DECREMENTIN',
    'INCREMENTTIMES',
    'DIVIDEIN',
    'MODIN',
    'FLOAT',    #Asumo que desde aquí debemos definir tipos de datos
    'INT',
    'LONG',
    'BOOLEAN' #Fin de aporte de Betsy-----------------------------------------------------------------------------------

) + tuple(reserved.values())
# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_MOD = r'%'
#Aporte de Betsy--------------------------------------------------------------------------------------------------------
t_EQUAL = r'='
t_DOTS = r':'
t_INCREMENTONE = r'\+\+'
t_DECREMENTONE = r'--'
t_INCREMENTIN = r'\+='
t_DECREMENTIN = r'-='
t_INCREMENTTIMES = r'\*='
t_DIVIDEIN = r'/\='
t_MODIN = r'%='

#Fin de aporte de Betsy-------------------------------------------------------------------------------------------------




#Aquí seguir implementando los tokens




#Aporte de Betsy--------------------------------------------------------------------------------------------------------
def t_BOOLEAN(t):
    r'true|false'
    t.value = bool(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

# Regla de expresión regular para decimales
def t_FLOAT(t):
    r'-?[0-9]+\.[0-9]+f'
    t.value = float(t.value[:-1])
    return t

# Regla de expresión regular para Long
def t_LONG(t):
    r'(-[1-9][0-9]*)|([0-9]+)L'
    t.value = int(t.value[:-1])
    return t

# Regla de expresión regular para enteros
def t_INT(t):
    r'(-[1-9][0-9]*)|(\d+)'
    t.value = int(t.value)
    return t



#Fin de aporte de Betsy-------------------------------------------------------------------------------------------------



# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
def getTokens(lexer):
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)
# Build the lexer
lexer = lex.lex()
linea=" "
while linea!="":
    linea=input(">>")
    lexer.input(linea)
    getTokens(lexer)
# Tokenize
print("Succesfull")