import ply.lex as lex
import ply.yacc as yacc
import analizador_lexico

lexer = lex.lex(module=analizador_lexico)

cadena = ''' 
        println(numbers.slice(1..3))
    '''
lexer.input(cadena)

while True:
    tok = lexer.token()
    if tok!=None:
        print(tok)
        # print(tok.type, tok.value, tok.lineno, tok.lexpos)
    else:
        break
