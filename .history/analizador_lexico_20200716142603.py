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
    #'outer': 'OUTER',
    #'continue': 'CONTINUE',
    'in': 'IN',
    'until': 'UNTIL',
    'step': 'STEP',
    'downTo': 'DOWNTO',
    'index': 'INDEX',
    'fun' : 'FUN'
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
    'println': 'PRINTLN',
    'indices': 'INDICES'
}

variables = {
    'Int' : 'INT',
    'Float' : 'FLOAT',
    'Boolean' : 'BOOLEAN',
    'String' : 'STRING',
    'List' : 'LIST',
    'Set' : 'SET',
    'Pair' : 'PAIR',
    'Triple' : 'TRIPLE',
    'Array': 'ARRAY'
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
    'COMDOBLE',
    'SIGNODOLAR',
    'INICIOCOMENTARIO',
    'PREGUNTA'
]

tokens = ["NUMEROS", "ID"] + list(reservados.values()) + list(simbolos)\
         + list(funciones.values()) + list(variables.values())

t_NUMEROS = r'[0-9]+'

t_IGUAL = r'='
t_IGUALIGUAL = r'=='
t_TRIPLEIGUAL = r'==='
t_NOIGUAL = r'!='
t_NEGACION = r'!'
t_MAYOR = r'>'
t_MENOR = r'<'
t_MAYORIGUAL = r'>='
t_MENORIGUAL = r'<='

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
t_SIGNODOLAR = r'\$'
t_INICIOCOMENTARIO = r'//'
t_PREGUNTA = r'\?'

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
