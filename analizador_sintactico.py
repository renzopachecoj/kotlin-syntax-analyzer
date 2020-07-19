import ply.lex as lex
import ply.yacc as yacc
import analizador_lexico

lexer = lex.lex(module=analizador_lexico)
tokens = analizador_lexico.tokens

def p_sentencia(p):
    '''sentencia : asignacion
                | expresion
                | metodo
                | control
                | condicion
                | atributo
    '''


def p_asignacion(p):
    '''asignacion : VAL ID tipoAsignacion
                  | VAR ID tipoAsignacion
    '''
    print("asignacion")

def p_tipoAsignacion(p):
    '''tipoAsignacion : declaracion
                      | inicializacion
                      | declaracion inicializacion'''

def p_declaracion(p):
    'declaracion : DOSPUNTOS tipoDato'

def p_inicializacion(p):
    'inicializacion : IGUAL valor'

def p_tipoDato(p):
    '''tipoDato : INT
                | FLOAT
                | BOOLEAN
                | STRING
                | LIST MENOR tipoDato MAYOR
                | SET MENOR tipoDato MAYOR
                | PAIR MENOR tipoDato COMA tipoDato MAYOR
                | TRIPLE MENOR tipoDato COMA tipoDato COMA tipoDato MAYOR '''

def p_valor(p):
    '''valor : ENTEROEXPRESION
             | FLOTANTEEXPRESION
             | BOOLEANOEXPRESION
             | CADENAEXPRESION
             | list
             | set
             | pair
             | triple'''

def p_list(p):
    'list : ACOR contenido CCOR'

def p_set(p):
    'set : APAR contenido CPAR'

def p_pair(p):
    'pair : APAR tipoFactor COMA tipoFactor CPAR'

def p_triple(p):
    'triple : APAR tipoFactor COMA tipoFactor COMA tipoFactor CPAR'

def p_contenido(p):
    '''contenido : elementos factor
                 | elementos factorEspecial'''

def p_elementos_col(p):
    'elementos : elementos COMA'

def p_elementos_ter(p):
    '''elementos : factor
                 | factorEspecial'''

def p_tipoFactor(p):
    '''tipoFactor : factor
                | factorEspecial'''

def p_expresion_suma(p):
    'expresion : expresion SUMA termino'
    p[0] = p[1] + p[3]

def p_expresion_resta(p):
    'expresion : expresion RESTA termino'
    p[0] = p[1] - p[3]

def p_expresion_division(p):
    'expresion : expresion DIVISION termino'
    p[0] = p[1] / p[3]

def p_expresion_mult(p):
    'expresion : expresion MULT termino'
    p[0] = p[1] * p[3]

def p_expresion_modulo(p):
    'expresion : expresion MODULO termino'
    p[0] = p[1] % p[3]

def p_expresion_termino(p):
    'expresion : termino'
    p[0] = p[1]

def p_termino_suma(p):
    'termino : termino SUMA factorEspecial'
    p[0] = p[1] + p[3]

def p_termino_resta(p):
    'termino : termino RESTA factor'
    p[0] = p[1] - p[3]

def p_termino_mult(p):
    'termino : termino MULT factor'
    p[0] = p[1] * p[3]

def p_termino_division(p):
    'termino : termino DIVISION factor'
    p[0] = p[1] / p[3]

def p_termino_modulo(p):
    'termino : termino MODULO factor'
    p[0] = p[1] % p[3]

def p_termino_factor(p):
    'termino : factor'
    p[0] = p[1]

def p_termino_factorEspecial(p):
    '''termino : ENTEROEXPRESION
               | FLOTANTEEXPRESION
               | CADENAEXPRESION
               | list
               | set'''

def p_factor_num(p):
    'factor : ENTEROEXPRESION'
    p[0] = p[1]

def p_factor_float(p):
    'factor : FLOTANTEEXPRESION'
    p[0] = p[1]

def p_factorEspecial(p):
    '''factorEspecial : ENTEROEXPRESION
               | FLOTANTEEXPRESION
               | CADENAEXPRESION
               | list
               | set'''

# def p_factorEspecial_string(p):
#     'factorEspecial : CADENAEXPRESION'
#     p[0] = p[1]

# def p_factorEspecial_list(p):
#     'factorEspecial : list'
#     p[0] = p[1]
#
# def p_factorEspecial_set(p):
#     'factorEspecial : set'
#     p[0] = p[1]

def p_factor_expr(p):
    'factor : APAR expresion CPAR'
    p[0] = p[2]

def p_funcion(p):
    '''funcion : WITHINDEX
                | GET
                | SLICE
                | COMPARETO
                | GETINDEX
                | HASHCODE
                | CONTAINS
                | SIZE
                | ISEMPTY
                | TOSTRING
                | TOLIST
                | PRINT
                | PRINTLN
                | INDICES
    '''


def p_metodo(p):
    '''metodo : ID PUNTO ID APAR CPAR
            | ID PUNTO ID APAR ID CPAR
            | atributo PUNTO ID APAR CPAR
            | atributo PUNTO ID APAR ID CPAR
            | ID PUNTO funcion APAR CPAR
            | ID PUNTO funcion APAR ID CPAR
            | atributo PUNTO funcion APAR CPAR
            | atributo PUNTO funcion APAR ID CPAR
    '''
    print("metodo")


def p_atributo(p):
    '''atributo : ID PUNTO ID'''
    print("atributo")


def p_comparador(p):
    '''comparador : IGUALIGUAL 
                | TRIPLEIGUAL 
                | NOIGUAL 
                | MAYOR 
                | MENOR 
                | MAYORIGUAL 
                | MENORIGUAL
    '''

def p_conector(p):
    '''conector : AND 
                | OR
    '''

def p_compmiembro(p):
    '''compmiembro : ID
                    | ENTEROEXPRESION
                    | metodo
                    | atributo
                    | asignacion
    '''

def p_condicion(p):
    '''condicion : compmiembro comparador compmiembro
                | compmiembro comparador compmiembro conector compmiembro comparador compmiembro
    '''
    print("condicion")

def p_control(p):
    '''control : if
                | for
                | while
    '''


def p_cuerpo(p):
    '''cuerpo : sentencia
                | ALLAVE sentencia CLLAVE
    '''


def p_if(p):
    '''if : IF APAR condicion CPAR cuerpo
        | IF APAR condicion CPAR cuerpo ELSE cuerpo
    '''
    print("if")


def p_for(p):
    '''for : FOR APAR ID IN ID CPAR cuerpo
        | FOR APAR ID DOSPUNTOS INT IN ID CPAR cuerpo
        | FOR APAR ID IN ENTEROEXPRESION PUNTOPUNTO ENTEROEXPRESION CPAR cuerpo
        | FOR APAR ID IN ENTEROEXPRESION UNTIL ENTEROEXPRESION CPAR cuerpo
        | FOR APAR ID IN ENTEROEXPRESION UNTIL ENTEROEXPRESION STEP ENTEROEXPRESION CPAR cuerpo
        | FOR APAR ID IN ENTEROEXPRESION DOWNTO ENTEROEXPRESION STEP ENTEROEXPRESION CPAR cuerpo
        | FOR APAR ID IN ID PUNTO INDICES CPAR cuerpo
        | FOR APAR ID IN ID PUNTO ID CPAR cuerpo
        | FOR APAR APAR ID COMA ID CPAR IN ID PUNTO WITHINDEX APAR CPAR CPAR cuerpo
        | FOR APAR APAR ID COMA ID CPAR IN ID CPAR cuerpo
    '''
    print("for")


def p_while(p):
    '''while : WHILE APAR condicion CPAR cuerpo
    '''
    print("while")


def p_error(p):
    print("Error de sintaxis en: ", p.value)


parser = yacc.yacc()
while True:
    try:
        s = input('<kotlin> ')
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    print(result)
