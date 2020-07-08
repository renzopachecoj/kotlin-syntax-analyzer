import ply.lex as lex

reservados = {
    'for': 'FOR',
    'in': 'IN',
    'until': 'UNTIL',
    'step': 'STEP',
    'downTo': 'DOWNTO',
    'index': 'INDEX',
    'value': 'VALUE',
    'key': 'KEY',

    'while': 'WHILE',
    'break': 'BREAK',
    'outer': 'OUTER',
    'continue': 'CONTINUE',
    
    'if': 'IF', 
    'else': 'ELSE',
}

simbolos = {
    'apar': 'APAR',
    'cpar': 'CPAR',
    'allave': 'ALLAVE',
    'cllave': 'CLLAVE',
    'acor': 'ACOR',
    'ccor': 'CCOR',
    'punto': 'PUNTO',
    #considerar doble punto
    'puntocoma': 'PUNTOCOMA',
    'coma': 'COMA',
    'igual': 'IGUAL',
    'mayor': 'MAYOR',
    'menor': 'MENOR',
    'arroba': 'ARROBA',
    'comsimple': "COMSIMP",
    'comdoble': "COMDOBLE"
}

funciones = {
    'withIndex': 'WITHINDEX',
    'get': 'GET',
    'set': 'SET',
    'slice': 'SLICE',
    'compareTo': 'COMPARETO',
    'getIndex': 'GETINDEX',
    'hashCode': 'HASHCODE',
    'contains': 'CONTAINS',
    'size': 'SIZE',
    'isEmpty': 'ISEMPTY',
    'toString': 'TOSTRING',
    'toList': 'TOLIST'
}

atributos = {
    #'key': 'KEY',
    #'value': 'VALUE',
    'keys': 'KEYS',
    'values': 'VALUES'
}

tokens = ["NUMEROS", "ID"] + list(reservados.values()) + list(simbolos.values()) + list(funciones.values()) +list(atributos.values())

t_NUMEROS = r'[0-9]+'
t_FOR = r'for'
t_IN = r'int'
t_UNTIL = r'until'
t_STEP = r'step'
t_DOWNTO = r'downto'
t_INDEX = r'index'
t_VALUE = r'value'
t_KEY = r'key'
t_WHILE = r'while'
t_BREAK = r'break'
t_OUTER = r'outer'
t_CONTINUE = r'continue'
t_IF = r'if'
t_ELSE = r'else'

t_APAR = r'\('
t_CPAR = r'\)'
t_ALLAVE = r'{'
t_CLLAVE = r'}'
t_ACOR = r'\['
t_CCOR = r'\]'
t_PUNTO = r'\.'
t_PUNTOCOMA = r';'
t_COMA = r','
t_IGUAL = r'='
t_MAYOR = r'>'
t_MENOR = r'<'
t_ARROBA = r'@'
t_COMSIMP = r'\''
t_COMDOBLE = r'\"'

t_WITHINDEX = r'withIndex'
t_GET = r'get'
t_SET = r'set'
t_SLICE = r'slice'
t_COMPARETO = r'compareTo'
t_GETINDEX = r'getIndex'
t_HASHCODE = r'hashCode'
t_CONTAINS = r'contains'
t_SIZE = r'size'
t_ISEMPTY = r'isEmpty'
t_TOSTRING = r'toString'
t_TOLIST = r'toList'

t_KEYS = r'keys'
t_VALUES = r'values'

t_ignore = r'   '

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in reservados:
        t.type = reservados.get(t.value, 'RESERVADOS')  # Verifica palabras reservadas
    if t.value in simbolos:
        t.type = simbolos.get(t.value, 'SIMBOLOS')
    if t.value in funciones:
        t.type = funciones.get(t.value, 'FUNCIONES')
    if t.value in atributos:
        t.type = atributos.get(t.value, 'ATRIBUTOS')
    return t

def t_error(t):
    print("No se ha reconocido '%s'"%t.value[0])
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

cadena = "for (item in items) {}"

analizadorL = lex.lex()
analizadorL.input(cadena)

while True:
    tokenRec = analizadorL.token()
    if tokenRec!=None:
        print(tokenRec)
    else:
        break
