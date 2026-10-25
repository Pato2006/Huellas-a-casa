"""Funciones simples para acceder a MySQL desde los ejemplos de PWM."""

import mysql.connector

# Marcadores: %s usa tuplas/listas y %(nombre)s 
# usa diccionarios; no usar %d ni %f.

def _conectar(configDB):
    return mysql.connector.connect(
                host=configDB["host"],
                user=configDB["user"],
                password=configDB["password"],
                database=configDB["database"]
            )

def selectDB(configDB, sql, valores=None, title=False, dictionary=False):
    """Ejecuta un SELECT y retorna tuplas o diccionarios.

    Si title es True, el primer elemento del resultado contiene los títulos.
    """
    conexion = None
    cursor = None
    registros = None
    try:
        conexion = _conectar(configDB)
        cursor = conexion.cursor(dictionary=dictionary)
        cursor.execute(sql, valores)
        registros = cursor.fetchall()

        if title:
            titulos = cursor.column_names
            if dictionary:
                titulos = {titulo: titulo for titulo in titulos}
            else:
                titulos = tuple(titulos)
            registros.insert(0, titulos)
    except mysql.connector.Error as error:
        print("No se pudo realizar el SELECT:", error)
    finally:
        if cursor is not None:
            cursor.close()
        if conexion is not None and conexion.is_connected():
            conexion.close()

    return registros


def _ejecutar_escritura(configDB, sql, valores=None):
    conexion = None
    cursor = None
    filas_afectadas = None
    try:
        conexion = _conectar(configDB)
        cursor = conexion.cursor()
        cursor.execute(sql, valores)
        conexion.commit()
        filas_afectadas = cursor.rowcount
    except mysql.connector.Error as error:
        if conexion is not None:
            conexion.rollback()
        print("No se pudo modificar la base:", error)
    finally:
        if cursor is not None:
            cursor.close()
        if conexion is not None and conexion.is_connected():
            conexion.close()

    return filas_afectadas


def insertDB(configDB, sql, valores=None):
    return _ejecutar_escritura(configDB, sql, valores)


def updateDB(configDB, sql, valores=None):
    return _ejecutar_escritura(configDB, sql, valores)


def deleteDB(configDB, sql, valores=None):
    return _ejecutar_escritura(configDB, sql, valores)
