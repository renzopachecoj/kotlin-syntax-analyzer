import tkinter as tk

window = tk.Tk()


label = tk.Label(text="Código en lenguaje Kotlin")
label2 = tk.Label(text="Resultados de análisis")

textFld = tk.Text()     #input
textFld2 = tk.Text()    #salida
textFld2.configure(state="disabled")

btn = tk.Button(text="Analizador Léxico")
btn2 = tk.Button(text="Analizador Sintáctico")

label.pack()
textFld.pack()
btn.pack(side="LEFT")
btn2.pack(side="RIGHT")
textFld2.pack()
window.mainloop()