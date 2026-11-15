import os
import uuid

from flask import request
from werkzeug.utils import secure_filename


def uploadFile(datos=None, campo="archivo", carpeta="static/uploads", extensiones_permitidas=None):
    """Guarda un archivo válido y completa el diccionario recibido."""
    if datos is None:
        datos = {}

    clave_error = "error_" + campo
    archivo = request.files.get(campo)
    archivo_valido = True

    if archivo is None or archivo.filename == "":
        archivo_valido = False

    if archivo_valido:
        nombre_seguro = secure_filename(archivo.filename)
        if nombre_seguro == "" or "." not in nombre_seguro:
            datos[clave_error] = "El archivo debe tener un nombre y una extensión válidos."
            archivo_valido = False

    if archivo_valido:
        extension = nombre_seguro.rsplit(".", 1)[1].lower()
        if extensiones_permitidas is not None and extension not in extensiones_permitidas:
            datos[clave_error] = "La extensión no está permitida."
            archivo_valido = False

    if archivo_valido:
        nombre_nuevo = uuid.uuid4().hex + "." + extension

        try:
            os.makedirs(carpeta, exist_ok=True)
            archivo.save(os.path.join(carpeta, nombre_nuevo))
            datos[campo] = nombre_nuevo
        except OSError as error:
            datos[clave_error] = "No se pudo guardar el archivo: " + str(error)

    return datos
