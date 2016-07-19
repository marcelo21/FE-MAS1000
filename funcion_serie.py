import serial
import time


def envio_dato(direccion, dato):
    """
    ESTA FUNCION ENVIA UN PARAMETRO Y
    UNA POSICION DE MEMORIA POR PUERTO
    SERIE.
    """

    ser = serial.Serial('COM4')
    print(ser.name)

    ser.write(bytes(direccion.encode()))
    ser.write(b'*')  # ESTO ES UNA POSICION DE MEMORIA.

    ser.write(bytes(dato.encode()))
    ser.write(b'_')  # ESTO ES UN PARAMETRO.

    ser.write(b';')
    ser.close()


def envio_dato_calibracion(dato):
    """
    ESTA FUNCION ENVIA LOS DATOS NECESARIOS
    PARA LA FUNCION DE CALIBRACION
    """

    ser = serial.Serial('COM4')
    print(ser.name)

    ser.write(bytes(dato.encode()))
    time.sleep(1)
    ser.write(bytes(dato.encode()))
    time.sleep(1)
    ser.write(bytes(dato.encode()))
    time.sleep(1)

    ser.close()


def leo_dato_eeprom(tipo, direccion):
    """
    ESTA FUNCION LEE UNA POSICION
    DE MEMORIA DESDE LA EEPROM
    """

    ser = serial.Serial('COM4', timeout=0.001)
    print(ser.name)

    ser.write(bytes(direccion.encode()))
    ser.write(b'*')  # ESTO ES UNA POSICION DE MEMORIA.
    ser.write(bytes(tipo.encode()))

    valor = ser.readline()

    if direccion == str(0x07):
        valor = int(valor) / 10

    elif direccion == str(0x08):
        valor = int(valor) / 10

    else:
        valor = valor

    ser.close()

    return(valor)