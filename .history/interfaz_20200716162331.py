import tkinter as tk
import analizador_sintactico

window = tk.Tk()


label = tk.Label("Código en lenguaje Kotlin")
label2 = tk.Label("Resultados de análisis")

textFld = tk.Text()     #input
textFld2 = tk.Text()    #salida
textFld2.configure(state="disabled")

btn = tk.Button("Analizador Léxico")
btn2 = tk.Button("Analizador Sintáctico")

label.pack()
textFld.pack()
btn.pack()
btn2.pack()
textFld2.pack()
window.mainloop()