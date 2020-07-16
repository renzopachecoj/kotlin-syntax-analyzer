import tkinter as tk

window = tk.Tk()


label = tk.Label(text="Código en lenguaje Kotlin")
label2 = tk.Label(text="Resultados de análisis")

textFld = tk.Text()     #input
textFld2 = tk.Text()    #salida
textFld2.configure(state="disabled")

btn = tk.Button(text="Analizador Léxico")
btn2 = tk.Button(text="Analizador Sintáctico")

label.grid(row=0,column=0)
textFld.grid(row=1,column=0)
btn.grid(row=2,column=0)
btn2.grid(row=2,column=1)
label2.grid(row=3,column=0)
textFld2.grid(row=4,column=0)
window.mainloop()