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
    '''asignacion : VAL ID IGUAL NUMEROS
                | VAR ID IGUAL NUMEROS
    '''
    print("asignacion")


def p_expresion(p):
    '''expresion : NUMEROS SUMA NUMEROS
                | PRINTLN APAR COMDOBLE ID COMDOBLE CPAR
                | PRINTLN APAR ID CPAR
    '''
    print("expresion")


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
                    | NUMEROS
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
        | FOR APAR ID IN NUMEROS PUNTOPUNTO NUMEROS CPAR cuerpo
        | FOR APAR ID IN NUMEROS UNTIL NUMEROS CPAR cuerpo
        | FOR APAR ID IN NUMEROS UNTIL NUMEROS STEP NUMEROS CPAR cuerpo
        | FOR APAR ID IN NUMEROS DOWNTO NUMEROS STEP NUMEROS CPAR cuerpo
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
