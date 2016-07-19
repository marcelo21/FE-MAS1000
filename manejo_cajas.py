import funcion_serie as fs
import numpy as np

# fs.envio_dato(str(0x20 + (20)*(programa - 1) ), Acercamiento_1)


def grabo_dato_parametro(Programa, Acercamiento_1, Acercamiento_2, Tiempo_Repe):
    Valor = (20 * (Programa - 1))

    fs.envio_dato(str(0x20 + Valor), Acercamiento_1)
    fs.envio_dato(str(0x21 + Valor), Acercamiento_2)

    fs.envio_dato(str(0x22 + Valor), Tiempo_Repe)


def grabo_dato_parametro_pre_sold(Programa, Pre_Sold, Intensidad_1, Tiempo_Frio_1):
    Valor = (20 * (Programa - 1))

    fs.envio_dato(str(0x23 + Valor), Pre_Sold)
    fs.envio_dato(str(0x24 + Valor), Intensidad_1)
    fs.envio_dato(str(0x25 + Valor), Tiempo_Frio_1)


def grabo_dato_parametro_sold(Programa, Soldadura, Intensidad_2, Tiempo_Frio_2, Impulsos):
    Valor = (20 * (Programa - 1))

    fs.envio_dato(str(0x26 + Valor), Soldadura)
    fs.envio_dato(str(0x27 + Valor), Intensidad_2)
    fs.envio_dato(str(0x28 + Valor), Tiempo_Frio_2)
    fs.envio_dato(str(0x29 + Valor), Impulsos)


def grabo_dato_parametro_post_sold(Programa, Post_Sold, Intensidad_3, Tiempo_Frio_3):
    Valor = (20 * (Programa - 1))

    fs.envio_dato(str(0x2A + Valor), Post_Sold)
    fs.envio_dato(str(0x2B + Valor), Intensidad_3)
    fs.envio_dato(str(0x2C + Valor), Tiempo_Frio_3)


def grabo_dato_parametro_forja(Programa, Tiempo_Forja, Fuerza):
    Valor = (20 * (Programa - 1))

    fs.envio_dato(str(0x2D + Valor), Fuerza)
    fs.envio_dato(str(0x2E + Valor), Tiempo_Forja)


def grabo_dato_parametro_incremento_decenso(Programa, Incremento, Decenso, Incremento_Potencia, Decenso_Potencia):
    Valor = (20 * (Programa - 1))

    fs.envio_dato(str(0x2F + Valor), Incremento)
    fs.envio_dato(str(0x30 + Valor), Decenso)
    fs.envio_dato(str(0x31 + Valor), Incremento_Potencia)
    fs.envio_dato(str(0x32 + Valor), Decenso_Potencia)


def grabo_dato_parametro_tolerancia(Programa, Tolerancia_Sup, Tolerancia_Inf):
    Valor = (20 * (Programa - 1))

    fs.envio_dato(str(0x33 + Valor), Tolerancia_Sup)
    fs.envio_dato(str(0x34 + Valor), Tolerancia_Inf)


def grabo_dato_calibracion(Modo):
    if(Modo == 1):
        fs.envio_dato_calibracion('A')
    elif(Modo == 2):
        fs.envio_dato_calibracion('B')
    elif(Modo == 3):
        fs.envio_dato_calibracion('C')
    elif(Modo == 4):
        fs.envio_dato_calibracion('D')


def grabo_dato_calibracion_parametros(Acercamiento, Apriete, Presion, Soldadura, Mantenido, Fuerza_1, Fuerza_2, Corriente_1, Corriente_2):
    ALTO = Acercamiento >> 8
    BAJO = Acercamiento & 0xFF
    fs.envio_dato(str(0x00), str(ALTO))
    fs.envio_dato(str(0x01), str(BAJO))

    ALTO = Apriete >> 8
    BAJO = Apriete & 0xFF
    fs.envio_dato(str(0x02), str(ALTO))
    fs.envio_dato(str(0x03), str(BAJO))
    #Acercamiento y Apriete se separan en 2 valores de 8bit

    fs.envio_dato(str(0x04), Presion)
    fs.envio_dato(str(0x05), Soldadura)
    fs.envio_dato(str(0x06), Mantenido)

    fs.envio_dato(str(0x07), Fuerza_1)
    fs.envio_dato(str(0x08), Fuerza_2)
    fs.envio_dato(str(0x09), Corriente_1)
    fs.envio_dato(str(0x0A), Corriente_2)


def grabo_dato_servicios_puntos(Puntos, Alarm_Puntos, Fresados, Alarm_Fresados):
    ALTO = Puntos >> 8
    BAJO = Puntos & 0xFF
    fs.envio_dato(str(0x11), str(ALTO))
    fs.envio_dato(str(0x12), str(BAJO))

    #fs.envio_dato(str(0x11), str(Puntos))
    #fs.envio_dato(str(0x12), str(Puntos))
    #Divido "Puntos" en dos

    fs.envio_dato(str(0x13), Fresados)
    fs.envio_dato(str(0x14), Alarm_Puntos)
    fs.envio_dato(str(0x15), Alarm_Fresados)


def grabo_dato_servicios_fuerza(Fresado, Cambio_Electrodo):
    fs.envio_dato(str(0x16), Fresado)
    fs.envio_dato(str(0x17), Cambio_Electrodo)


def grabo_dato_servicios_tiempo(Acercamiento, Apriete):
    fs.envio_dato(str(0x18), Acercamiento)
    fs.envio_dato(str(0x19), Apriete)


def grabo_dato_servicios_Punto_Piezas(Puntos_Pieza):
    ALTO = Puntos_Pieza >> 8
    BAJO = Puntos_Pieza & 0xFF
    fs.envio_dato(str(0x1A), str(ALTO))
    fs.envio_dato(str(0x1B), str(BAJO))


def grabo_dato_servicios_Ley_Incremental(Numero_Curva, Porcentaje):
    fs.envio_dato(str(0x1C), Numero_Curva)
    fs.envio_dato(str(0x1D), Porcentaje)


def pido_dato_eeprom_calibracion():
    """
    """

    print("calibracion////////////")

    y = np.zeros((1, 9))

    y[0][0] = fs.leo_dato_eeprom('E', str(0x00))  # Acercamiento
    y[0][1] = fs.leo_dato_eeprom('E', str(0x02))  # Aprite
    y[0][2] = fs.leo_dato_eeprom('E', str(0x04))  # Presion
    y[0][3] = fs.leo_dato_eeprom('E', str(0x05))  # Soldadura
    y[0][4] = fs.leo_dato_eeprom('E', str(0x06))  # Mantenido

    y[0][5] = fs.leo_dato_eeprom('E', str(0x07))  # Fuerza 1
    y[0][6] = fs.leo_dato_eeprom('E', str(0x08))  # Fuerza 2

    y[0][9] = fs.leo_dato_eeprom('E', str(0x09))  # Intensidad 1
    y[0][10] = fs.leo_dato_eeprom('E', str(0x0A))  # Intensidad 2

    return(y)


def pido_dato_eeprom_servicios():
    """
    """

    print("servicios////////////")

    z = np.zeros((1, 11))

    z[0][0] = fs.leo_dato_eeprom('E', str(0x11))  # Puntos
    z[0][1] = fs.leo_dato_eeprom('E', str(0x13))  # Fresados

    z[0][2] = fs.leo_dato_eeprom('E', str(0x14))  # Alarma Punto
    z[0][3] = fs.leo_dato_eeprom('E', str(0x15))  # Alarma Fresado

    z[0][4] = fs.leo_dato_eeprom('E', str(0x16))  # Fuerza Fresado
    z[0][5] = fs.leo_dato_eeprom('E', str(0x17))  # Fuerza Cambio Electrodo

    z[0][6] = fs.leo_dato_eeprom('E', str(0x18))  # Acercamiento
    z[0][7] = fs.leo_dato_eeprom('E', str(0x19))  # Apriete

    z[0][8] = fs.leo_dato_eeprom('E', str(0x1A))  # Puntos por Pieza

    z[0][9] = fs.leo_dato_eeprom('E', str(0x1C))  # Numero Curva
    z[0][10] = fs.leo_dato_eeprom('E', str(0x1D))  # Porcentaje Incremento

    return(z)


def pido_dato_eeprom_parametros(Cantidad_Programas):
    """
    """

    print("soldadura////////////")

    x = np.zeros((Cantidad_Programas, 21))

    x[0][0] = fs.leo_dato_eeprom('E', str(0x20))  # Acercamiento
    x[0][1] = fs.leo_dato_eeprom('E', str(0x21))  # Apriete

    x[0][2] = fs.leo_dato_eeprom('E', str(0x22))  # Tiempo Repeticion

    x[0][3] = fs.leo_dato_eeprom('E', str(0x23))  # Pre Soldadura
    x[0][4] = fs.leo_dato_eeprom('E', str(0x24))  # Intensidad 1
    x[0][5] = fs.leo_dato_eeprom('E', str(0x25))  # Tiempo Frio 1

    x[0][6] = fs.leo_dato_eeprom('E', str(0x26))  # Soldadura
    x[0][7] = fs.leo_dato_eeprom('E', str(0x27))  # Intensidad 2
    x[0][8] = fs.leo_dato_eeprom('E', str(0x28))  # Tiempo Frio 2
    x[0][9] = fs.leo_dato_eeprom('E', str(0x29))  # Impulsos

    x[0][10] = fs.leo_dato_eeprom('E', str(0x2F))  # Ascenso
    x[0][11] = fs.leo_dato_eeprom('E', str(0x30))  # Potencia Inicial
    x[0][12] = fs.leo_dato_eeprom('E', str(0x31))  # Descenso
    x[0][13] = fs.leo_dato_eeprom('E', str(0x32))  # Potencia Final

    x[0][14] = fs.leo_dato_eeprom('E', str(0x33))  # Tolerancia Sup
    x[0][15] = fs.leo_dato_eeprom('E', str(0x34))  # Tolerancia Inf

    x[0][16] = fs.leo_dato_eeprom('E', str(0x2A))  # Post Soldadura
    x[0][17] = fs.leo_dato_eeprom('E', str(0x2B))  # Intensidad 3
    x[0][18] = fs.leo_dato_eeprom('E', str(0x2C))  # Tiempo Frio 3

    x[0][19] = fs.leo_dato_eeprom('E', str(0x2E))  # Tiempo Forja
    x[0][20] = fs.leo_dato_eeprom('E', str(0x2D))  # Fuerza

    return(x)