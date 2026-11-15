from flask import request


def getRequest():
    """Retorna un diccionario con los datos recibidos por GET o POST."""
    datos = {}

    if request.method == "GET":
        origen = request.args
    else:
        origen = request.form

    for campo in origen.keys():
        valores = origen.getlist(campo)
        if len(valores) == 1:
            datos[campo] = valores[0]
        else:
            datos[campo] = valores

    return datos
