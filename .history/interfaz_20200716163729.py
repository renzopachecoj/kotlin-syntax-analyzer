import tkinter as tk

window = tk.Tk()


label = tk.Label(text="Código en lenguaje Kotlin").grid(row=0,column=0)
label2 = tk.Label(text="Resultados de análisis").grid(row=3,column=0)

textFld = tk.Text().grid(row=1,column=0)     #input
textFld2 = tk.Text().grid(row=4,column=0)    #salida


btn = tk.Button(text="Analizador Léxico").grid(row=2,column=0)
btn2 = tk.Button(text="Analizador Sintáctico").grid(row=2,column=1)

label.pack()
textFld.pack()
btn.pack()
btn2.pack()
textFld2.pack()
window.mainloop()