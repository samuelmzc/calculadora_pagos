import tkinter as tk

def dicts(
        param : str
) -> dict:
    colores = {
        "Fondo" : "#F2EED0",
        "Fondo Entry": "#FCFBEF",
        "Título" : "#374B4A",
        "Subtítulo" : "#526760",
        "Descripción" : "Black"
    }

    fuentes = {
        "Título" : ("ATC Elm Normal", 24, "bold"),
        "Subtítulo" : ("ATC Elm Normal", 12, "normal")
    }

    dictionaries = {
        "Colores" : colores,
        "Fuentes" : fuentes
    }
    return dictionaries[str(param)]

def ajustar_texto(event):
    """
    Función para ajustar texto de tkinter a la ventana.
    """
    event.widget.config(wraplength = event.width)

def extraer(
    entrada_raiz,
    entrada_sal,
    entrada_salext,
    resultados,
    window
):
    """
    Comando que ejecuta el botón
    """
    resultados["Raíz"] = entrada_raiz.get()
    resultados["Salario"] = entrada_sal.get()
    resultados["Salario Extra"] = entrada_salext.get()
    window.destroy()

def window_obtener(
        colores = dicts("Colores"),
        fuentes = dicts("Fuentes")
):
    """
    Se crea ventana usando tkinter
    """
    # Creación de ventana
    window = tk.Tk()
    window.title("Cálculo de pago")
    window.geometry("1000x500")
    window.minsize(500, 250)
    window.configure(bg = colores["Fondo"])

    # Título
    titulo = tk.Label(window, text = "Cálculo de pagos")
    titulo.config(fg = colores["Título"], bg = colores["Fondo"], font = fuentes["Título"])
    titulo.pack(pady = (30, 10))

    # Descripción
    subtitulo = tk.Label(window, text = "Este programa calcula el pago que se te va a realizar en función de las horas que trabajes en un rango de tiempo específico. Se tienen en cuenta horas preventorias, extras, nocturnidades, etc...")
    subtitulo.config(fg = colores["Subtítulo"], bg = colores["Fondo"], font = fuentes["Subtítulo"], justify = "left")
    subtitulo.pack(fill = "both", pady = (0, 20))
    subtitulo.bind("<Configure>", ajustar_texto)

    # Insertar raiz
    label_raiz = tk.Label(window, text = "Inserte la ubicación del archivo csv")
    label_raiz.config(fg = colores["Subtítulo"], bg = colores["Fondo"], font = fuentes["Subtítulo"], justify = "center")
    label_raiz.pack()
    entrada_raiz = tk.Entry(window)
    entrada_raiz.config(bg = colores["Fondo Entry"])
    entrada_raiz.pack(pady = (0, 20))

    # Insertar salario por hora
    label_sal = tk.Label(window, text = "Inserte su salario por hora")
    label_sal.config(fg = colores["Subtítulo"], bg = colores["Fondo"], font = fuentes["Subtítulo"], justify = "center")
    label_sal.pack()
    entrada_sal = tk.Entry(window)
    entrada_sal.config(bg = colores["Fondo Entry"])
    entrada_sal.pack(pady = (0, 20))

    # Insertar salario por hora extra
    label_salext = tk.Label(window, text = "Inserte su salario por hora extra")
    label_salext.config(fg = colores["Subtítulo"], bg = colores["Fondo"], font = fuentes["Subtítulo"], justify = "center")
    label_salext.pack()
    entrada_salext = tk.Entry(window)
    entrada_salext.config(bg = colores["Fondo Entry"])
    entrada_salext.pack(pady = (0, 20))

    # Botón para obtener los valores de las entradas
    resultados_boton = {}
    boton = tk.Button(
        window,
        text = "Enviar",
        command = lambda : extraer(entrada_raiz, entrada_sal, entrada_salext, resultados_boton, window)
    ).pack()

    window.mainloop()
    return (resultados_boton)

