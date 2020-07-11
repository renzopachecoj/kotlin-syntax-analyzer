import ply.lex as lex
import ply.yacc as yacc
import analizador_lexico

lexer = lex.lex(module=analizador_lexico)

cadena = ''' for( elements in arreglo ){
        var x: Int = 1;
        print("hola")
        println(numbers.slice(0..4 step 2))
    }
    '''

analizadorL = lex.lex()
analizadorL.input(cadena)

while True:
    tokenRec = analizadorL.token()
    if tokenRec!=None:
        print(tokenRec)
    else:
        break


lexer.input(cadena)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok.type, tok.value, tok.lineno, tok.lexpos)