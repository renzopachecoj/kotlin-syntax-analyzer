import ply.lex as lex
import analizador_lexico

lexer = lex.lex(module=analizador_lexico)

cadena = "true === 45"

lexer.input(cadena)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok.type, tok.value, tok.lineno, tok.lexpos)