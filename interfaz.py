import tkinter as tk
import ply.lex as lex
import ply.yacc as yacc
import analizador_lexico
import analizador_sintactico

window = tk.Tk()
window.geometry("600x500")
window.title("Analizador léxico y sintáctico de kotlin")

label = tk.Label(text="Código en lenguaje Kotlin")
label2 = tk.Label(text="Resultados de análisis")

textFld = tk.Text()     #input
textFld2 = tk.Text()    #salida
textFld2.configure(state="disabled")


def presentErrors(errors, messageOK):
    textFld2.config(state="normal")
    textFld2.delete('1.0', "end")

    if len(errors) == 0:
        textFld2.insert("1.0", messageOK)
    else:
        for i in range(0, len(errors)):
            textFld2.insert("1.0", errors[len(errors) - 1- i] + "\n")
    errors.clear()
    textFld2.config(state="disabled")

def lexer():
    data = textFld.get("1.0", 'end-1c')

    if len(data) == 0:
        presentErrors(analizador_lexico.errors, "Please enter code before validating.")
    else:
        lexer = lex.lex(module=analizador_lexico)
        tokens = analizador_lexico.tokens
        tok = lexer.input(data)
        while True:
            tok = lexer.token()
            if not tok:
                break
            print(tok.value, tok.type, tok.lineno)
        presentErrors(analizador_lexico.errors, "Lexical Errors not found. OK!")

def parser():
    data = textFld.get("1.0", 'end-1c')

    if len(data) == 0:
        presentErrors(analizador_lexico.errors, "Please enter code before validating.")
    else:
        lexer = lex.lex(module=analizador_lexico)
        tokens = analizador_lexico.tokens
        parser = yacc.yacc(module=analizador_sintactico)
        data = textFld.get("1.0", 'end-1c')
        parser.parse(data)
        presentErrors(analizador_sintactico.errors, "Syntax Errors not found. OK!")


btn = tk.Button(text="Analizador Léxico", command=lexer)
btn2 = tk.Button(text="Analizador Sintáctico", command=parser)

label.grid(row=0, column=0, columnspan=2)
textFld.grid(row=1, column=0, columnspan=2)
btn.grid(row=2, column=0)
btn2.grid(row=2, column=1)
label2.grid(row=3, column=0, columnspan=2)
textFld2.grid(row=4, column=0, columnspan=2)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

window.grid_rowconfigure(0, weight=0)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=0)
window.grid_rowconfigure(3, weight=0)
window.grid_rowconfigure(4, weight=1)
window.mainloop()
