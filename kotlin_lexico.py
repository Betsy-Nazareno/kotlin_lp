import ply.lex as lex
from ply.lex import TOKEN

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
    'import' : 'IMPORT'
       #Aporte de Eddy
'PUBLIC': 'public',
'PRIVATE': 'private',
'PROTECTED': 'protected',
'INTERNAL': 'internal',
'ENUM': 'enum',
'SEALED': 'sealed',
'ANNOTATION': 'annotation',
'DATA': 'data',
'INNER': 'inner',
'VALUE': 'value',
'TAILREC': 'tailrec',
'OPERATOR': 'operator',
'INLINE': 'inline',
'INFIX': 'infix',
'EXTERNAL': 'external',
'SUSPEND': 'suspend',
'OVERRIDE': 'override',
'ABSTRACT': 'abstract',
'FINAL': 'final',
'OPEN': 'open',
'CONST': 'const',
'LATEINIT': 'lateinit',
'VARARG': 'vararg',
'NOINLINE': 'noinline',
'CROSSINLINE': 'crossinline',
'REIFIED': 'reified',
'EXPECT': 'expect',
'ACTUAL': 'actual',
'RETURN_AT': 'return@',
'CONTINUE_AT': 'continue@',
'BREAK_AT': 'break@',
'THIS_AT': 'this@',
'SUPER_AT': 'super@',
'FILE': 'file',
'FIELD': 'field',
'PROPERTY': 'property',
'GET': 'get',
'SET': 'set',
'RECEIVER': 'receiver',
'PARAM': 'param',
'SETPARAM': 'setparam',
'DELEGATE': 'delegate',
'PACKAGE': 'package',
'IMPORT': 'import',
'CLASS': 'class',
'INTERFACE': 'interface',
'FUN': 'fun',
'OBJECT': 'object',
'VAL': 'val',
'VAR': 'var',
'TYPE_ALIAS': 'typealias',
'CONSTRUCTOR': 'constructor',
'BY': 'by',
'COMPANION': 'companion',
'INIT': 'init',
'THIS': 'this',
'SUPER': 'super',
'TYPEOF': 'typeof',
'WHERE': 'where',
'IF': 'if',
'ELSE': 'else',
'WHEN': 'when',
'TRY': 'try',
'CATCH': 'catch',
'FINALLY': 'finally',
'FOR': 'for',
'DO': 'do',
'WHILE': 'while',
'THROW': 'throw',
'RETURN': 'return',
'CONTINUE': 'continue',
'BREAK': 'break',
'AS': 'as',
'IS': 'is',
'IN': 'in',
'NOT_IS': '!is',
'NOT_IN': '!in',
'OUT': 'out',
'DYNAMIC': 'dynamic',
}
tokens = (
    'VAR_TIPO_1',
    'SUM',
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
    'MARK_1',
    'MARK_2',
    'STRING_1',
    'STRING_2',
    'COMMENT',
    'BOOLEAN' #Fin de aporte de Betsy-----------------------------------------------------------------------------------

) + tuple(reserved.values())
# Regular expression rules for simple tokens
t_VAR_TIPO_1 = r'var="[\w]+"'
t_MARK_1 = r'"'
t_MARK_2 = r"'"
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
# Aporte de Eddy
t_RESERVED = r'...'
t_DOT= r'.'
t_COMMA= r','
t_LPAREN= r'('
t_RPAREN= r')'
t_LSQUARE= r'['
t_RSQUARE= r']'
t_LCURL= r'{' 
t_RCURL= r'}'
t_INCR= r'++'
t_DECR= r'--'
t_CONJ= r'&&'
t_DISJ= r'||'
t_EXCL_WS= r'!'
t_EXCL_NO_WS= r'!'
t_COLON= r':'
t_SEMICOLON= ';'
t_ASSIGNMENT= '='
t_ADD_ASSIGNMENT= '+='
t_SUB_ASSIGNMENT= '-='
t_MULT_ASSIGNMENT= '*='
t_DIV_ASSIGNMENT= '/='
t_MOD_ASSIGNMENT= '%='
t_ARROW= '->'
t_DOUBLE_ARROW= '=>'
t_RANGE= '..'
t_COLONCOLON= '::'
t_DOUBLE_SEMICOLON= ';;'
t_HASH= '#'
t_AT_NO_WS= '@'
t_QUEST_WS= '?'
t_QUEST_NO_WS= '?'
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

# Regular expression rules for complex tokens
t_STRING_1 = r'"[\w]*"'
t_STRING_2 = r"'[\w]*'"


#t_VAL_TIPO_1 = r'(var' + t_EQUAL + r'(' + t_STRING_1 + r'|'+ t_STRING_2 + r')' + r')'



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
    r'-?[0-9]+\.[0-9]+'
    t.value = float(t.value[:-1])
    return t

# Regla de expresión regular para Long
def t_LONG(t):
    r'(-[1-9][0-9]*)|([0-9]+)'
    t.value = int(t.value[:-1])
    return t

# Regla de expresión regular para enteros
entero = r'(-[1-9][0-9]*)|(\d+)'
suma = r'(' + entero + t_PLUS + entero + r')'

@TOKEN(entero)
def t_INT(t):
    #r'(-[1-9][0-9]*)|(\d+)'
    t.value = int(t.value)
    return t

@TOKEN(suma)
def t_SUM(t):
    return t

def t_COMMENT(t):
    r'(\/\/\w*)|(\/\*\w*\*\/)'
    pass #ignora comentarios

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
