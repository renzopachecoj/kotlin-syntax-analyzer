errors = []

reservados = {
    'val': 'VAL',
    'var': 'VAR',
    'true': 'TRUE',
    'false': 'FALSE',
    'for': 'FOR',
    'while': 'WHILE',
    'if': 'IF',
    'else': 'ELSE',
    'in': 'IN',
    'until': 'UNTIL',
    'step': 'STEP',
    'downTo': 'DOWNTO',
    'f': 'F'
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
    'indices': 'INDICES',
    'indexOf': 'INDEXOF',
    'listOf': 'LISTOF',
    'setOf': 'SETOF'
}

variables = {
    'Int': 'INT',
    'Float': 'FLOAT',
    'Boolean': 'BOOLEAN',
    'String': 'STRING',
    'List': 'LIST',
    'Set': 'SET',
    'Pair': 'PAIR',
    'Triple': 'TRIPLE'
}

simbolos = [
    'IGUAL',
    'IGUALIGUAL',
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
    'PUNTO',
    'DOSPUNTOS',
    'PUNTOPUNTO',
    'PUNTOCOMA',
    'COMA',
    "SIGNODOLAR",
    "COMDOBLE"
]

valores = ["ENTEROEXPRESION"]


tokens = ["ID"] + list(valores)\
         + list(reservados.values()) + list(simbolos)  \
         + list(funciones.values()) + list(variables.values()) \

t_IGUAL = r'='
t_IGUALIGUAL = r'=='
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
t_PUNTO = r'\.'
t_PUNTOPUNTO = r'\.\.'
t_DOSPUNTOS = r':'
t_PUNTOCOMA = r';'
t_COMA = r','
t_SIGNODOLAR = r"\$"
t_COMDOBLE = r'"'
# t_FLOTANTEEXPRESION = r'\d+(\.\d+)?f'

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

def t_ENTEROEXPRESION(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# def t_FLOTANTEEXPRESION(t):
#     r'\d+(\.\d+)?f'
#     try:
#         t.value = float(t.value[:-2])
#     except ValueError:
#         print("Float value too large %d", t.value)
#         t.value = 0
#     return t

def t_error(t):
    message = "Lexical Error. Unknown token '" + t.value[0] + "'" + " at line " + str(t.lineno) + "."
    #print("No se ha reconocido '%s'"%t.value[0])
    errors.append(message)
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
