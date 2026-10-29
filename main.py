import argparse
import calculos as c
import tk_settings as tks
import tkinter as tk
import pandas as pd

# Se crea el parser del programa
parser = argparse.ArgumentParser(
    prog = "Calculadora de pagos",
    description = open("./media/descripcion.txt").read()
)

# Argumentos del parser
parser.add_argument("-v", "--verbosity", help = "Incrementa el texto al ejecutar códigos", type = bool)
parser.add_argument("-r", "--root", help = "Ruta del archivo con las horas", type = str)
parser.add_argument("-s", "--salario", help = "Pago por hora", type = float, default = 10)
parser.add_argument("-e", "--salarioext", help = "Pago por hora extra", type = float, default = 12)
parser.add_argument("-t", "--terminal", help = "Usar parseo por terminal o por Tkinter", action = "store_true")
args = parser.parse_args()

# Hacemos funcionar la ventana del Tkinter
resultados_boton = tks.window_obtener() if not args.terminal else 0

# Definimos los parámetros según si se usa tkinter o no
root = args.root if args.terminal else resultados_boton["Raíz"]
salario = args.salario if args.terminal else resultados_boton["Salario"]
salarioext = args.salarioext if args.terminal else resultados_boton["Salario Extra"]
if __name__ == "__main__":
    # Se convierte el csv en DataFrame
    df = pd.read_csv(root)
    df["HORAS"] = df.apply(lambda fila: c.calculo_horas(fila["ENTRADA"], fila["SALIDA"], fila["SALIDA REAL"])[0], axis = 1)
    df["HORAS EXTRA"] = df.apply(lambda fila: c.calculo_horas(fila["ENTRADA"], fila["SALIDA"], fila["SALIDA REAL"])[1], axis = 1)
    df["HORAS TUPLA"] = df.apply(lambda fila: c.calculo_horas(fila["ENTRADA"], fila["SALIDA"], fila["SALIDA REAL"]), axis = 1)
    df["PAGO"] = df.apply(lambda fila: c.calculo_pago(fila["HORAS TUPLA"], args.salario, args.salarioext), axis = 1)

    # Hacemos la suma de las distintas columnas
    horas_total = df["HORAS"].sum()
    horasext_total = df["HORAS EXTRA"].sum()
    pago_total = df["PAGO"].sum()

    # Solución estética para que no aparezca .0 si el número al final es entero
    pago_total = int(pago_total) if pago_total - int(pago_total) == 0 else pago_total

    # Print final
    print(f"Este mes va a cobrar {pago_total}€ brutos, con un total de {horas_total + horasext_total} horas trabajadas, de las cuales {horasext_total} fueron preventorias.")

