import serial
import time


def envio_dato(direccion, dato):
    """
    ESTA FUNCION ENVIA UN PARAMETRO Y
    UNA POSICION DE MEMORIA POR PUERTO
    SERIE.
    """

    direccion = str(direccion)
    dato = str(int(dato))

    try:
        ser = serial.Serial('COM5', baudrate=9600, timeout=0.1)
        print("PUERTO =", ser.name, "DATO =", dato)
        time.sleep(0.1)

        ser.write(bytes(direccion.encode()))
        ser.write(b'*')  # ESTO ES UNA POSICION DE MEMORIA.

        ser.write(bytes(dato.encode()))
        ser.write(b'_')  # ESTO ES UN PARAMETRO.

        ser.write(b';')
        ser.close()

    except:
        ser.close()


def envio_dato_calibracion(dato):
    """
    ESTA FUNCION ENVIA LOS DATOS NECESARIOS
    PARA LA FUNCION DE CALIBRACION
    """

    try:
        ser = serial.Serial('COM5', baudrate=9600, timeout=1)
        print("PUERTO =", ser.name, "DATO =", dato)
        time.sleep(0.1)

        ser.write(bytes(dato.encode()))
        time.sleep(1)
        ser.write(bytes(dato.encode()))
        time.sleep(1)
        ser.write(bytes(dato.encode()))
        time.sleep(1)

        ser.close()

    except:
        ser.close()


def leo_dato_eeprom(tipo, direccion):
    """
    ESTA FUNCION LEE UNA POSICION
    DE MEMORIA DESDE LA EEPROM
    """

    direccion = str(direccion)

    try:
        ser = serial.Serial('COM5', baudrate=9600, timeout=0.1)
        time.sleep(0.1)

        ser.write(bytes(direccion.encode()))
        ser.write(b'*')  # ESTO ES UNA POSICION DE MEMORIA.
        ser.write(bytes(tipo.encode()))

        valor = ser.readline()

        if direccion == str(0x07):
            valor = int(valor) / 1  # Tension Fuerza 1

        elif direccion == str(0x08):
            valor = int(valor) / 1  # Tension Fuerza 2

        elif direccion == str(0x0F):
            valor = int(valor) / 100  # Valor Corriente 1

        elif direccion == str(0x11):
            valor = int(valor) / 100  # Valor Corriente 2

        else:
            valor = int(valor)

        ser.close()

        print("PUERTO =", ser.name, "DATO =", valor)

        return(valor)

    except:
        ser.close()