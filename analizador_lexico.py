
reservados = {
    'val': 'VAL',
    'var': 'VAR',
    'true': 'TRUE',
    'false': 'FALSE',
    'for': 'FOR',
    'while': 'WHILE',
    'if': 'IF',
    'else': 'ELSE',
    'break': 'BREAK',
    'outer': 'OUTER',
    'continue': 'CONTINUE',
    'in': 'IN',
    'until': 'UNTIL',
    'step': 'STEP',
    'downTo': 'DOWNTO',
    'index': 'INDEX'
}

funciones = {
    'withIndex': 'WITHINDEX',
    'get': 'GET',
    'slice': 'SLICE',
    'compareTo': 'COMPARETO',
    'getIndex': 'GETINDEX',
    'hashCode': 'HASHCODE',
    'contains': 'CONTAINS',
    'size': 'SIZE',
    'isEmpty': 'ISEMPTY',
    'toString': 'TOSTRING',
    'toList': 'TOLIST',
    'print': 'PRINT',
    'println': 'PRINTLN'
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

simbolos = [
    'IGUAL',
    'IGUALIGUAL',
    'TRIPLEIGUAL',
    'NOIGUAL',
    'NEGACION',
    'MAYOR',
    'MENOR',
    'MAYORIGUAL',
    'MENORIGUAL',
    'SUMA',
    'RESTA',
    'DIVISION',
    'MULT',
    'MODULO',
    'AND',
    'OR',
    'APAR',
    'CPAR',
    'ALLAVE',
    'CLLAVE',
    'ACOR',
    'CCOR',
    'PUNTO',
    'DOSPUNTOS',
    'PUNTOPUNTO',
    'PUNTOCOMA',
    'COMA',
    'ARROBA',
    'COMSIMPLE',
    'COMDOBLE'
]

tokens = ["NUMEROS", "ID"] + list(reservados.values()) + list(simbolos)\
         + list(funciones.values()) + list(variables.values())

t_NUMEROS = r'[0-9]+'

t_IGUAL = r'='
t_IGUALIGUAL = '=='
t_TRIPLEIGUAL = '==='
t_NOIGUAL = '!='
t_NEGACION = '!'
t_MAYOR = r'>'
t_MENOR = r'<'
t_MAYORIGUAL = '>='
t_MENORIGUAL = '<='

t_SUMA = r'\+'
t_RESTA = r'\-'
t_DIVISION = r'/'
t_MULT = r'\*'
t_MODULO = r'%'

t_AND = r'&&'
t_OR = r'\|\|'

t_APAR = r'\('
t_CPAR = r'\)'
t_ALLAVE = r'{'
t_CLLAVE = r'}'
t_ACOR = r'\['
t_CCOR = r'\]'
t_PUNTO = r'\.'
t_PUNTOPUNTO = r'\.\.'
t_DOSPUNTOS = r':'
t_PUNTOCOMA = r';'
t_COMA = r','
t_ARROBA = r'@'

t_COMSIMPLE = r'\''
t_COMDOBLE = r'\"'

t_ignore = ' \t'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in reservados:
        t.type = reservados.get(t.value, 'RESERVADOS')  # Verifica palabras reservadas
    if t.value in funciones:
        t.type = funciones.get(t.value, 'FUNCIONES')
    if t.value in variables:
        t.type = variables.get(t.value, 'VARIABLES')    
    return t

def t_error(t):
    print("No se ha reconocido '%s'"%t.value[0])
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
