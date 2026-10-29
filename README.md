 # 🖩 **Calculadora de pagos** 🖩

El objetivo de este repositorio reside en obtener el pago que se realizará según el número  de horas trabajadas. Se tienen en cuenta las horas extra, y los turnos partidos.

## 🛠️ *Cómo funciona* 🛠️

Es necesario tener un archivo (preferiblemente un .csv) que contenga columnas *ENTRADA*, *SALIDA*, *SALIDA REAL*, y en las filas se tengan las distintas horas de los turnos realizados en formato HH:MM.

**Nota**: En el caso de los turnos partidos, en el campo *ENTRADA*, se ha de poner a hora de entrada original, y la entrada tras partir el turno. Lo mismo aplica al campo *SALIDA*

Hay dos modos en el que funciona este script, insertando los valores necesarios mediante terminal, o a través de una ventana de Tkinter. Esto se realiza con el argumento -t (más información con -h o --help). Los resultados son mostrados también en una ventana de Tkinter, se muestra el pago en euros, las horas totales trabajadas, y cuáles de ellas son horas extra. Próximamente aparecerán las horas realizadas los domingos, festivos, nocturnidades, etc...

