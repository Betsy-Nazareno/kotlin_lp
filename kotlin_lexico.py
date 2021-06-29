import ply.lex as lex
from ply.lex import TOKEN
import ply.yacc as yacc

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
    'when': 'WHEN',
    'package': 'PACKAGE',
    'import' : 'IMPORT',
    'arrayOf': 'ARRAYOF',
    'print': 'PRINT',
    'println': 'PRINTLN',
    'Int': 'TINT',
    'Double': 'TDOUBLE',
    'String': 'TSTRING',
    'Long': 'TLONG',
    'Float': 'TFLOAT',
    'Boolean': 'TBOOLEAN',
    'Char': 'TCHAR',
    'Queue': 'QUEUE',
    'LinkedList': 'LINKEDLIST',
    'listOf': 'LISTOF',
    'add': 'ADD',
    'peek': 'PEEK',
    'remove': 'REMOVE',
    'poll': 'POLL',
    'public':'PUBLIC',      #Aporte de Eddy-------------------------------------------------------------------
    'private': 'PRIVATE',
    'protected':'PROTECTED',
    'internal':'INTERNAL',
    'enum':'ENUM',
    'sealed': 'SEALED',
    'annotation':'ANNOTATION',
    'data':'DATA',
    'inner':'INNER',
    'value':'VALUE',
    'tailrec':'TAILREC',
    'operator':'OPERATOR',
    'inline':'INLINE',
    'infix':'INFIX',
    'external':'EXTERNAL',
    'suspend':'SUSPEND',
    'override':'OVERRIDE',
    'abstract':'ABSTRACT',
    'final':'FINAL',
    'open':'OPEN',
    'const':'CONST',
    'lateinit':'LATEINIT',
    'vararg':'VARARG',
    'noinline':'NOINLINE',
    'crossinline' :'CROSSINLINE',
    'reified':  'REIFIED',
    'expect':  'EXPECT',
    'actual':  'ACTUAL',
    'file':  'FILE',
    'field':  'FIELD',
    'property':  'PROPERTY',
    'get':'GET',
    'set':'SET',
    'receiver':'RECEIVER',
    'param':'PARAM',
    'setparam':'SETPARAM',
    'class'  : 'CLASS',
    'interface': 'INTERFACE',
    'object':'OBJECT',
    'typealias':'TYPE_ALIAS',
    'constructor':'CONSTRUCTOR',
    'by':'BY',
    'companion':'COMPANION',
    'init':'INIT',
    'this':'THIS',
    'super':'SUPER',
    'typeof' : 'TYPEOF',
    'where':'WHERE',
    'try':'TRY',
    'catch': 'CATCH',
    'finally':'FINALLY',
    'do': 'DO',
    'throw':'THROW',
    'continue':'CONTINUE',
    'break':'BREAK',
    'as':'AS',
    'out':'OUT',
    'dynamic':'DYNAMIC',

    #karla
    'Stack':'STACK',
    'ArrayList':'ARRAYLIST',
    'pop':'POP',
    'isEmpty':'ISEMPTY',
    'push':'PUSH'
}

tokens = (
    'VAR_TIPO_1',
    'VAL_TIPO_1',
    'SUM',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    "MOD",
    "ID",
    "LINEBREAK",
    'EQUAL',#Aporte de Betsy--------------------------------------------------------------------------------------------
    'DOTS',
    'INCREMENTONE',
    'DECREMENTONE',
    'INCREMENTIN',
    'DECREMENTIN',
    'INCREMENTTIMES',
    'DIVIDEIN',
    'MODIN',
    'FLOAT',
    'INT',
    'LONG',
    'MARK_1',
    'MARK_2',
    'STRING_1',
    'CHAR',
    'COMMENT',
    'BOOLEAN', #Fin de aporte de Betsy-----------------------------------------------------------------------------------
    'DOT', #Aporte Eddy  ---------------------------------------------------------------------------------------
    'COMMA',
    'LSQUARE',
    'RSQUARE',
    'LCURL',
    'RCURL',
    'INCR',
    'DECR',
    'CONJ',
    'DISJ',
    'EXCL_WS',
    'EXCL_NO_WS',
    'ARROW',
    'DOUBLE_ARROW',
    'RANGE',
    'COLONCOLON',
    'DOUBLE_SEMICOLON',
    'SEMICOLON',
    'HASH',
    'AT_NO_WS',
    'QUEST_WS',
    'LANGLE',
    'RANGLE',
    'LE',
    'GE',
    'EXCL_EQ',
    'EXCL_EQEQ',
    'AS_SAFE',
    'EQEQ',
    'EQEQEQ',
    'SINGLE_QUOTE',
    'TEMPLATE'

) + tuple(reserved.values())
# Regular expression rules for simple tokens
#Aporte de Betsy--------------------------------------------------------------------------------------------------------
t_VAR_TIPO_1 = r'var=\.*'
t_LINEBREAK = r'\n'
t_MARK_1 = r'"'
t_MARK_2 = r"'"
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_MOD = r'%'
t_EQUAL = r'\='
t_DOTS = r':'
t_INCREMENTONE = r'\+\+'
t_DECREMENTONE = r'--'
t_INCREMENTIN = r'\+='
t_DECREMENTIN = r'-='
t_INCREMENTTIMES = r'\*='
t_DIVIDEIN = r'/\='
t_MODIN = r'%='

#Fin de aporte de Betsy-------------------------------------------------------------------------------------------------
# Aporte de Eddy
t_DOT= r'\.'
t_COMMA= r','
t_LSQUARE= r'\['
t_RSQUARE= r']'
t_LCURL= r'{' 
t_RCURL= r'}'
t_CONJ= r'&&'
t_DISJ= r'\|\|'
t_EXCL_WS= r'!'
t_EXCL_NO_WS= r'!'
t_SEMICOLON= ';'
t_ARROW= '->'
t_DOUBLE_ARROW= '=>'
t_RANGE= '\.\.'
t_COLONCOLON= '::'
t_DOUBLE_SEMICOLON= ';;'
t_HASH= '\#'
t_AT_NO_WS= '@'
t_QUEST_WS= '\?'
t_LANGLE= '<'
t_RANGLE= '>'
t_LE= '<='
t_GE= '>='
t_EXCL_EQ= '!='
t_EXCL_EQEQ= '!=='
t_AS_SAFE= 'as?'
t_EQEQ= '=='
t_EQEQEQ= '==='
t_SINGLE_QUOTE= '\''
#Findeaporte

# Regular expression rules for complex tokens - Aporte Karla -----------------------------------------------------------
t_STRING_1 = r'("([\w]*[^"])*")|("""[\w\t\n\$^"]*""")'
t_CHAR = r"'[\w]{0,1}'"

entero = r'(-[1-9][0-9]*)|(\d+)'
t_SUM = r'(' + entero + t_PLUS + entero + r')'
t_VAL_TIPO_1 = r'(var' + t_EQUAL + r'(' + t_STRING_1 + r')' + r')'
t_TEMPLATE = r'"([\w ]*)\${[\w= ]*}([\w ]*)"'

#Fin aporte Karla ------------------------------------------------------------------------------------------------------


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
    return t

# Regla de expresión regular para Long
def t_LONG(t):
    r'((-[1-9][0-9]*)|([0-9]+))L'
    return t

# Regla de expresión regular para enteros
def t_INT(t):
    r'(-[1-9][0-9]*)|(\d+)'
    t.value = int(t.value)
    return t

#Fin de aporte de Betsy-------------------------------------------------------------------------------------------------

#Aporte de Karla--------------------------------------------------------------------------------------------------------
def t_COMMENT(t):
    r'(\/\/\w*)|(\/\*\w*\*\/)'
    pass #ignora comentarios

def t_PACKAGE(t):
    r'package \w + (\.\w*) * (\ *)?'
    return t

def t_IMPORT(t):
    r'import \w+(\.\w*)*(\*)?( as [a-zA-Z]+)?'
    return t
#Fin aporte de Karla----------------------------------------------------------------------------------------------------





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

"""
linea=" "
while linea!="":
    linea=input(">>")
    lexer.input(linea)
    getTokens(lexer)
# Tokenize
print("Succesfull")
"""