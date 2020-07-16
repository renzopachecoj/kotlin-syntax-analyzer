import tkinter as tk

window = tk.Tk()
window.geometry("600x500")

label = tk.Label(text="Código en lenguaje Kotlin")
label2 = tk.Label(text="Resultados de análisis")

textFld = tk.Text()     #input
textFld2 = tk.Text()    #salida
textFld2.configure(state="disabled")

btn = tk.Button(text="Analizador Léxico")
btn2 = tk.Button(text="Analizador Sintáctico")

label.grid(row=0,column=0, columnspan=2)
textFld.grid(row=1,column=0, columnspan=2)
btn.grid(row=2,column=0)
btn2.grid(row=2,column=1)
label2.grid(row=3,column=0, columnspan=2)
textFld2.grid(row=4,column=0, columnspan=2)
window.grid_columnConfigure(0, weight=1)
window.grid_columnConfigure(1, weight=1)
window.grid_rowConfigure(0, weight=1)
window.grid_rowConfigure(1, weight=1)
window.grid_rowConfigure(2, weight=1)
window.grid_rowConfigure(3, weight=1)
window.grid_rowConfigure(4, weight=1)
window.mainloop()