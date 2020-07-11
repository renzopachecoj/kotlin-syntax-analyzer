import ply.lex as lex

reserved = {
    'if' : 'IF',
    'elif' : 'ELIF',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'for' : 'FOR',
    'echo' : 'ECHO',

    'val' : 'VAL',
    'var' : 'VAR'
}

variables = {
    'int' : 'INT',
    'float' : 'FLOAT',
    'boolean' : 'BOOLEAN',
    'string' : 'STRING',
    'list' : 'LIST',
    'set' : 'SET',
    'pair' : 'PAIR',
    'triple' : 'TRIPLE'
}

tokens = ["MENOS", "MAS", "PRODUCTO", "DIVISION",
          "NUMEROS", "LPAREN", "RPAREN", "IGUAL", "POTENCIA",
          "ID", "COMPARA", "PUNTOS"] + list(reserved.values()) + list(variables.values()) + list(simbolos.values())

t_MENOS = r'-'
t_MAS = r'\+'
t_PRODUCTO = r'\*'
t_DIVISION = r'/'
t_NUMEROS = r'[0-9]+'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_IGUAL = r'='
t_POTENCIA = r'\\'
t_COMPARA = r'[<>!=]='
t_PUNTOS = r':'
t_IF = r'if'
t_ECHO = r'echo'
t_WHILE = r'while'
t_FOR = r'for'
t_ELIF = r'elif'
t_ignore = r'   '

t_VAL = r'val'
t_VAR = r'var'

t_INT = r'Int'
t_FLOAT = r'Float'
t_BOOLEAN = r'Boolean'

t_STRING = r'String'
t_PAIR = r'Pair'
t_TRIPLE = r'Triple'
t_SET = r'Set'
t_LIST = r'List'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    if t.value in variables:
        t.type = variables.get(t.value, 'VARIABLES')    
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print("No se ha reconocido '%s'"%t.value[0])
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

cadena = "for while"

analizadorL = lex.lex()
analizadorL.input(cadena)

while True:
    tokenRec = analizadorL.token()
    if tokenRec!=None:
        print(tokenRec)
    else:
        break

lex.lex()