from tkinter import*

ventana = Tk()
ventana.title("Calculadora")

e_texto = Entry(ventana, font= ("ComicsSans 20"))
e_texto.grid(row= 0, column= 0, columnspan= 4, padx= 10, pady= 10)

boton1 = Button(ventana, text="1", width=9, height=2)
boton2 = Button(ventana, text="2", width=9, height=2)
boton3 = Button(ventana, text="3", width=9, height=2)
boton4 = Button(ventana, text="4", width=9, height=2)
boton1.grid(row= 1, column= 0, padx=5, pady=5)
boton2.grid(row= 1, column= 1, padx=5, pady=5)
boton3.grid(row= 1, column= 2, padx=5, pady=5)
boton4.grid(row= 1, column= 3, padx=5, pady=5)

ventana.mainloop()