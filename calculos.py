import datetime as dt

def intervalo_horas(
        inicial : str,
        final : str
) -> float:
    """
    Esta función calcula el intervalo de horas entre dos horas exactas

    :param inicial: Hora inicial del intervalo en formato HH:MM
    :param final: Hora final del intervalo en formato HH:MM
    :return Intervalo: Número de horas
    """
    inicial = dt.datetime.strptime(inicial, "%H:%M")
    final = dt.datetime.strptime(final, "%H:%M")
    delta = final - inicial
    seconds = delta.total_seconds()
    hours = seconds / (60*60)
    hours = hours if hours >= 0 else 24 + hours
    return hours

def calculo_horas(
        entrada : str,
        salida : str,
        salida_real : str
) -> tuple:
    """
    Calcula el número de horas trabajadas. Esta función devuelve las horas trabajadas,
    y además, el número de horas que han sido preventorias (extras). Esta función tiene 
    en cuenta los turnos partidos

    :param entrada: Hora de entrada. En el caso de turno sin partir: HH:MM, en el caso de turno partido: HH:MM,HH:MM. La hora antes de la coma es la entrada al turno, y la que va después de la misma, la hora de entrada después del partido
    :param salida: Hora de salida, mismo formato que hora entrada.
    :param salida_real: Hora de salida real al final de TODO el turno
    :return Horas: Devuelve tupla, cuyo primer valor es las horas trabajadas correspondientes, y el segundo, las horas extras que se han realizado
    """
    if "," not in entrada:
        horas = intervalo_horas(entrada, salida)
        horas_extra = intervalo_horas(salida, salida_real)
        return (horas, horas_extra)
    hora_entrada1, hora_entrada2 = entrada.replace(" ", "").split(",")
    hora_salida1, hora_salida2 = salida.replace(" ", "").split(",")
    horas = intervalo_horas(hora_entrada1, hora_salida1) + intervalo_horas(hora_entrada2, hora_salida2)
    horas_extra = intervalo_horas(hora_salida2, salida_real)
    return (horas, horas_extra)

def calculo_pago(
        tupla_horas : tuple,
        salario : float,
        salario_extra : float
) -> float:
    """
    Cálculo de pago bruto

    :param tupla_horas: Tupla con la forma (horas, horas extra)
    :param salario: salario por hora
    :param salario_extra: salario por hora extra
    :return pago: Pago total
    """
    pago, pago_extra = tupla_horas[0] * salario, tupla_horas[1] * salario_extra
    return pago + pago_extra