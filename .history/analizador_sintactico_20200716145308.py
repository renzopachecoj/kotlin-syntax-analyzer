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
    | atributo'''

def p_asignacion(p):
    '''asignacion : VAL ID IGUAL NUMEROS
                | VAR ID IGUAL NUMEROS
    '''
def p_expresion(p):
    '''expresion : NUMEROS SUMA NUMEROS
                | PRINTLN APAR COMDOBLE ID CPAR
                | PRINTLN APAR ID CPAR
    '''

def p_metodo(p):
    '''metodo : ID PUNTO ID APAR CPAR
            | ID PUNTO ID CPAR ID CPAR
            | ID PUNTO ID APAR CPAR
            | ID PUNTO ID APAR ID CPAR
    '''
def p_atributo(p):
    '''atributo : ID PUNTO ID'''

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
#condicion : NEGACION* (expresion | metodo) comparador NEGACION* (expresion | metodo) (CONECTOR NEGACION* (expresion | metodo) comparador NEGACION* (expresion | metodo))*
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

def p_while(p):
    '''while : WHILE condicion cuerpo
    '''
cadena = ''' 
        println(numbers.slice(1..3))
    '''
def p_error(p):
    print("Error de sintaxis:")

parser = yacc.yacc()
while True:
    try:
        s = input('<kotlin> ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)