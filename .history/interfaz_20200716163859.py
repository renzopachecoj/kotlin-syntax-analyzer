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
label.pack()
textFld.grid(row=1,column=0)
textFld.pack()
btn.pack()
btn2.pack()
textFld2.pack()
window.mainloop()