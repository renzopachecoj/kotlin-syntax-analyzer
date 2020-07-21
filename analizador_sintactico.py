import ply.lex as lex
import analizador_lexico

errors = []

lexer = lex.lex(module=analizador_lexico)
tokens = analizador_lexico.tokens

def p_todos(p):
    '''todos : sentencia PUNTOCOMA
    | sentencia
    | todos sentencia
    | todos sentencia PUNTOCOMA'''

def p_sentencia(p):
    '''sentencia : asignacion
                | valor
                | funcion
                | control
                | condicion
                | print
    '''


def p_print(p):
    '''print : printType APAR CADENAEXPRESION CPAR
             | printType APAR CPAR
             | printType APAR ID CPAR
             | printType APAR funcion CPAR'''

def p_print_error(p):
    'print : printType APAR error CPAR'
    message = "\tBad expression '" + str(p[3].value) + "' in function print. The content can be a string" \
                "\n\tbetween \" print(\"hello Word!\") or a function call."
    errors.append(message)


def p_printType(p):
    '''printType : PRINT
                 | PRINTLN'''

def p_funcion_string_compare(p):
    'funcion : CADENAEXPRESION PUNTO COMPARETO APAR CADENAEXPRESION CPAR'

def p_funcion_string_getindex(p):
    'funcion : CADENAEXPRESION PUNTO GETINDEX APAR ENTEROEXPRESION CPAR'

def p_funcion_string_hash(p):
    'funcion : CADENAEXPRESION PUNTO HASHCODE APAR CPAR'

def p_funcion_contains(p):
    '''funcion : ID PUNTO CONTAINS APAR factorEspecial CPAR
               | ID PUNTO CONTAINS APAR ID CPAR'''

def p_funcion_Getindex(p):
    'funcion : ID PUNTO GETINDEX APAR ENTEROEXPRESION CPAR'

def p_funcion_list_set(p):
    '''funcion : ID PUNTO SIZE APAR CPAR
               | ID PUNTO GET APAR CPAR
               | ID PUNTO SET APAR factorEspecial CPAR'''

def p_funcion_set(p):
    'funcion : ID PUNTO ISEMPTY APAR CPAR'

def p_funcion_tuple(p):
    '''funcion : ID PUNTO TOLIST APAR CPAR
               | ID PUNTO TOSTRING APAR  CPAR'''

def p_funcion_access_slice(p):
    'funcion : ID PUNTO SLICE APAR contentSlice CPAR'

def p_contentSlice(p):
    '''contentSlice : ENTEROEXPRESION PUNTOPUNTO ENTEROEXPRESION
                    | ENTEROEXPRESION PUNTOPUNTO ENTEROEXPRESION STEP ENTEROEXPRESION'''

def p_funcion_access_slice_error(p):
    'funcion : ID PUNTO SLICE APAR error CPAR'
    print("\tBad expression '%s' in function slice. Call function \n [variable].slice(NUM .. NUM step NUM)" % (p[5].value))


def p_funcion_access_indexOf(p):
    'funcion : ID PUNTO INDEXOF APAR factorEspecial CPAR'


def p_asignacion(p):
    '''asignacion : VAL ID tipoAsignacion
                  | VAR ID tipoAsignacion
                  | ID inicializacion
    '''

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
             | flotante
             | expresionBooleano
             | CADENAEXPRESION
             | list
             | set
             | pair
             | triple
             | expresion
             | ID
             | if'''

def p_expresionBooleano(p):
    '''expresionBooleano : TRUE
                        | FALSE'''

def p_flotante(p):
    '''flotante : ENTEROEXPRESION F
                | ENTEROEXPRESION PUNTO ENTEROEXPRESION F'''

def p_list(p):
    'list : LISTOF APAR contenido CPAR'

def p_set(p):
    'set : SETOF APAR contenido CPAR'

def p_pair(p):
    'pair : PAIR APAR factorEspecial COMA factorEspecial CPAR'

def p_triple(p):
    'triple : TRIPLE APAR factorEspecial COMA factorEspecial COMA factorEspecial CPAR'

def p_contenido(p):
    '''contenido : factorEspecial
                 | factorEspecial COMA contenido'''

def p_expresion_suma(p):
    'expresion : expresion SUMA termino'

def p_expresion_resta(p):
    'expresion : expresion RESTA termino'

def p_expresion_division(p):
    'expresion : expresion DIVISION termino'

def p_expresion_mult(p):
    'expresion : expresion MULT termino'

def p_expresion_modulo(p):
    'expresion : expresion MODULO termino'

def p_expresion_termino(p):
    'expresion : termino'

def p_termino_suma(p):
    'termino : termino SUMA factorEspecial'

def p_termino_resta(p):
    'termino : termino RESTA factor'

def p_termino_mult(p):
    'termino : termino MULT factor'

def p_termino_division(p):
    'termino : termino DIVISION factor'

def p_termino_modulo(p):
    'termino : termino MODULO factor'

def p_termino_factor(p):
    'termino : factor'

def p_termino_factorEspecial(p):
    '''termino : ENTEROEXPRESION
               | flotante
               | CADENAEXPRESION
               | list
               | set
               | ID'''

def p_factor_num(p):
    'factor : ENTEROEXPRESION'

def p_factor_float(p):
    'factor : flotante'

def p_factor_id(p):
    'factor : ID'

def p_factorEspecial(p):
    '''factorEspecial : factor
               | CADENAEXPRESION
               | list
               | set'''

def p_factor_expr(p):
    'factor : APAR expresion CPAR'


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
                    | funcion
                    | asignacion
    '''

def p_condicion(p):
    '''condicion : compmiembro comparador compmiembro
                | NEGACION compmiembro comparador compmiembro
                | condicion conector condicion
    '''

def p_control(p):
    '''control : if
                | for
                | while
    '''

def p_cuerpo(p):
    '''cuerpo : sentencia
                | ALLAVE todos CLLAVE
    '''

def p_if(p):
    '''if : IF APAR condicion CPAR cuerpo
        | IF APAR condicion CPAR cuerpo ELSE cuerpo
    '''

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

def p_while(p):
    '''while : WHILE APAR condicion CPAR cuerpo
    '''


def p_error(p):
    message = ""
    try:
        message = "Syntax Error at line " + str(p.lineno) + "."
    except:
        message = "Syntax Error"
    errors.append(message)
