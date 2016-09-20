import funcion_serie as fs
import numpy as np

# fs.envio_dato(str(0x20 + (20)*(programa - 1) ), Acercamiento_1)


def grabo_calibracion(y):
    ALTO = int(y[0][0]) >> 8
    BAJO = int(y[0][0]) & 0xFF
    fs.envio_dato(0x00, ALTO)
    fs.envio_dato(0x01, BAJO)

    ALTO = int(y[0][1]) >> 8
    BAJO = int(y[0][1]) & 0xFF
    fs.envio_dato(0x02, ALTO)
    fs.envio_dato(0x03, BAJO)
    #Acercamiento y Apriete se separan en 2 valores de 8bit

    fs.envio_dato(0x04, y[0][2])
    fs.envio_dato(0x05, y[0][3])
    fs.envio_dato(0x06, y[0][4])

    fs.envio_dato(0x07, y[0][5])  # Tension Fuerza 1
    fs.envio_dato(0x08, y[0][6])  # Tension Fuerza 2

    fs.envio_dato(0x09, y[0][7])  # Duty Corriente 1
    fs.envio_dato(0x0A, y[0][8])  # Duty Corriente 2

    ALTO = int(y[0][9]) >> 8
    BAJO = int(y[0][9]) & 0xFF
    fs.envio_dato(0x0B, ALTO)  # Valor Fuerza 1
    fs.envio_dato(0x0C, BAJO)  # Valor Fuerza 1

    ALTO = int(y[0][10]) >> 8
    BAJO = int(y[0][10]) & 0xFF
    fs.envio_dato(0x0D, ALTO)  # Valor Fuerza 2
    fs.envio_dato(0x0E, BAJO)  # Valor Fuerza 2

    ALTO = int(y[0][11]) >> 8
    BAJO = int(y[0][11]) & 0xFF
    fs.envio_dato(0x0F, ALTO)  # Valor Corriente 1
    fs.envio_dato(0x10, BAJO)  # Valor Corriente 1

    ALTO = int(y[0][12]) >> 8
    BAJO = int(y[0][12]) & 0xFF
    fs.envio_dato(0x11, ALTO)  # Valor Corriente 2
    fs.envio_dato(0x12, BAJO)  # Valor Corriente 2


def grabo_servicios(z):
    ALTO = int(z[0][0]) >> 8
    BAJO = int(z[0][0]) & 0xFF
    fs.envio_dato(0x20, ALTO)  # Puntos
    fs.envio_dato(0x21, BAJO)  # Puntos
    fs.envio_dato(0x22, z[0][1])  # Fresados

    fs.envio_dato(0x23, z[0][2])  # Alarma Punto
    fs.envio_dato(0x24, z[0][3])  # Alarma Fresado

    ALTO = int(z[0][4]) >> 8
    BAJO = int(z[0][4]) & 0xFF
    fs.envio_dato(0x25, ALTO)  # Contador Puntos 1
    fs.envio_dato(0x26, BAJO)  # Contador Puntos 1

    fs.envio_dato(0x27, z[0][5])  # Contador Fresado

    fs.envio_dato(0x28, z[0][6])  # Fuerza Fresado
    fs.envio_dato(0x29, z[0][7])  # Fuerza Cambio Electrodo

    fs.envio_dato(0x2A, z[0][8])  # Acercamiento
    fs.envio_dato(0x2B, z[0][9])  # Apriete

    ALTO = int(z[0][10]) >> 8
    BAJO = int(z[0][10]) & 0xFF
    fs.envio_dato(0x2C, ALTO)  # Puntos por Pieza
    fs.envio_dato(0x2D, BAJO)  # Puntos por Pieza

    fs.envio_dato(0x2E, z[0][11])  # Numero Curva
    fs.envio_dato(0x2F, z[0][12])  # Porcentaje Incremento

#def grabo_configuracion():


def grabo_parametros(x, Programa):
    """
    x: Matriz donde estan se almacenan los datos

    Cantidad_Programas: Numero TOTAL de Programas

    Programa: Programa Actual
    """

    Valor = ((0x10 * 0x02) * (Programa - 1))

    fs.envio_dato((0x40 + Valor), x[0][0])  # Acercamiento
    fs.envio_dato((0x41 + Valor), x[0][1])  # Apriete

    fs.envio_dato((0x42 + Valor), x[0][2])  # Tiempo Repeticion

    fs.envio_dato((0x43 + Valor), x[0][3])  # Pre Soldadura
    fs.envio_dato((0x44 + Valor), x[0][4])  # Intensidad 1 en %
    fs.envio_dato((0x45 + Valor), x[0][5])  # Tiempo Frio 1

    fs.envio_dato((0x46 + Valor), x[0][6])  # Soldadura
    fs.envio_dato((0x47 + Valor), x[0][7])  # Intensidad 2 en %
    fs.envio_dato((0x48 + Valor), x[0][8])  # Tiempo Frio 2
    fs.envio_dato((0x49 + Valor), x[0][9])  # Impulsos

    fs.envio_dato((0x4A + Valor), x[0][10])  # Post Soldadura
    fs.envio_dato((0x4B + Valor), x[0][11])  # Intensidad 3 en %
    fs.envio_dato((0x4C + Valor), x[0][12])  # Tiempo Frio 3

    fs.envio_dato((0x4D + Valor), x[0][13])  # Fuerza
    fs.envio_dato((0x4E + Valor), x[0][14])  # Tiempo Forja

    fs.envio_dato((0x4F + Valor), x[0][15])  # Ascenso
    fs.envio_dato((0x50 + Valor), x[0][16])  # Descenso
    fs.envio_dato((0x51 + Valor), x[0][17])  # Potencia Inicial en %
    fs.envio_dato((0x52 + Valor), x[0][18])  # Potencia Final en %

    fs.envio_dato((0x53 + Valor), x[0][19])  # Tolerancia Sup
    fs.envio_dato((0x54 + Valor), x[0][20])  # Tolerancia Inf


def grabo_dato_calibracion(Modo):
    if(Modo == 1):
        fs.envio_dato_calibracion('A')
    elif(Modo == 2):
        fs.envio_dato_calibracion('B')
    elif(Modo == 3):
        fs.envio_dato_calibracion('C')
    elif(Modo == 4):
        fs.envio_dato_calibracion('D')


def pido_dato_eeprom_calibracion():
    """
    """

    print("calibracion////////////")

    y = np.zeros((1, 13))

    y[0][0] = fs.leo_dato_eeprom('E', 0x00)  # Acercamiento
    y[0][1] = fs.leo_dato_eeprom('E', 0x02)  # Aprite
    y[0][2] = fs.leo_dato_eeprom('E', 0x04)  # Presion
    y[0][3] = fs.leo_dato_eeprom('E', 0x05)  # Soldadura
    y[0][4] = fs.leo_dato_eeprom('E', 0x06)  # Mantenido

    y[0][5] = fs.leo_dato_eeprom('E', 0x07)  # Duty Fuerza 1
    y[0][6] = fs.leo_dato_eeprom('E', 0x08)  # Duty Fuerza 2

    y[0][7] = fs.leo_dato_eeprom('E', 0x09)  # Duty Intensidad 1
    y[0][8] = fs.leo_dato_eeprom('E', 0x0A)  # Duty Intensidad 2

    y[0][9] = fs.leo_dato_eeprom('E', 0x0B)  # Valor Fuerza 1
    y[0][10] = fs.leo_dato_eeprom('E', 0x0D)  # Valor Fuerza 2

    y[0][11] = fs.leo_dato_eeprom('E', 0x0F)  # Valor Intensidad 1
    y[0][12] = fs.leo_dato_eeprom('E', 0x11)  # Valor Intensidad 2

    return(y)


def pido_dato_eeprom_servicios():
    """
    """

    print("servicios////////////")

    z = np.zeros((1, 13))

    z[0][0] = fs.leo_dato_eeprom('E', 0x20)  # Puntos
    z[0][1] = fs.leo_dato_eeprom('E', 0x22)  # Fresados

    z[0][2] = fs.leo_dato_eeprom('E', 0x23)  # Alarma Punto
    z[0][3] = fs.leo_dato_eeprom('E', 0x24)  # Alarma Fresado

    z[0][4] = fs.leo_dato_eeprom('E', 0x25)  # Contador Puntos 1
    z[0][5] = fs.leo_dato_eeprom('E', 0x27)  # Contador Fresado

    z[0][6] = fs.leo_dato_eeprom('E', 0x28)  # Fuerza Fresado
    z[0][7] = fs.leo_dato_eeprom('E', 0x29)  # Fuerza Cambio Electrodo

    z[0][8] = fs.leo_dato_eeprom('E', 0x2A)  # Acercamiento
    z[0][9] = fs.leo_dato_eeprom('E', 0x2B)  # Apriete

    z[0][10] = fs.leo_dato_eeprom('E', 0x2C)  # Puntos por Pieza

    z[0][11] = fs.leo_dato_eeprom('E', 0x2E)  # Numero Curva
    z[0][12] = fs.leo_dato_eeprom('E', 0x2F)  # Porcentaje Incremento

    return(z)


def pido_dato_eeprom_parametros(Cantidad_Programas, Programa):
    """
    """

    print("soldadura////////////")

    x = np.zeros((Cantidad_Programas, 21))

    VALOR = ((0x10 * 0x02) * (Programa - 1))

    x[0][0] = fs.leo_dato_eeprom('E', (0x40 + VALOR))  # Acercamiento
    x[0][1] = fs.leo_dato_eeprom('E', (0x41 + VALOR))  # Apriete

    x[0][2] = fs.leo_dato_eeprom('E', (0x42 + VALOR))  # Tiempo Repeticion

    x[0][3] = fs.leo_dato_eeprom('E', (0x43 + VALOR))  # Pre Soldadura
    x[0][4] = fs.leo_dato_eeprom('E', (0x44 + VALOR))  # Intensidad 1
    x[0][5] = fs.leo_dato_eeprom('E', (0x45 + VALOR))  # Tiempo Frio 1

    x[0][6] = fs.leo_dato_eeprom('E', (0x46 + VALOR))  # Soldadura
    x[0][7] = fs.leo_dato_eeprom('E', (0x47 + VALOR))  # Intensidad 2
    x[0][8] = fs.leo_dato_eeprom('E', (0x48 + VALOR))  # Tiempo Frio 2
    x[0][9] = fs.leo_dato_eeprom('E', (0x49 + VALOR))  # Impulsos

    x[0][10] = fs.leo_dato_eeprom('E', (0x4A + VALOR))  # Post Soldadura
    x[0][11] = fs.leo_dato_eeprom('E', (0x4B + VALOR))  # Intensidad 3
    x[0][12] = fs.leo_dato_eeprom('E', (0x4C + VALOR))  # Tiempo Frio 3

    x[0][13] = fs.leo_dato_eeprom('E', (0x4D + VALOR))  # Fuerza
    x[0][14] = fs.leo_dato_eeprom('E', (0x4E + VALOR))  # Tiempo Forja

    x[0][15] = fs.leo_dato_eeprom('E', (0x4F + VALOR))  # Ascenso
    x[0][16] = fs.leo_dato_eeprom('E', (0x50 + VALOR))  # Descenso
    x[0][17] = fs.leo_dato_eeprom('E', (0x51 + VALOR))  # Potencia Inicial
    x[0][18] = fs.leo_dato_eeprom('E', (0x52 + VALOR))  # Potencia Final

    x[0][19] = fs.leo_dato_eeprom('E', (0x53 + VALOR))  # Tolerancia Sup
    x[0][20] = fs.leo_dato_eeprom('E', (0x54 + VALOR))  # Tolerancia Inf

    return(x)