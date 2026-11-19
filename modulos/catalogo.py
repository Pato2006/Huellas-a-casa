from flask import redirect

from config import CONFIG_DB
from utilidades._mysql_db import deleteDB, insertDB, selectDB, updateDB
from utilidades.file_utils import uploadFile

def listas_animales():
    sql = "SELECT id,nombre,ruta_img FROM mascotas"
    consultas = selectDB(
        CONFIG_DB,
        sql,
        dictionary=True,
    )
    return consultas

def ver_animal(id):
    sql = "SELECT * FROM mascotas WHERE id = %s"

    consultas = selectDB(
        CONFIG_DB,
        sql,
        (id,),
        dictionary=True,
    )
    return consultas

def borrar_animal(id):
    sql = "DELETE FROM mascotas WHERE id = %s"
    valores = (id,)
    consultas = deleteDB(
        CONFIG_DB,
        sql,
        valores    
    )
    if consultas == 1:
        retorno = True
    else:
        retorno = "No se pudo eliminar el animal solicitado."
    return retorno

def cargar_animal_nuevo(datos):
    resultado = False
    mensaje = ""
    sql = """
        INSERT INTO mascotas (
            nombre, edad, peso, personalidad, descripcion,
            castrado, tipo, genero, ruta_img
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    if datos["castrado"] == "si":
        castrado = 1
    else:
        castrado = 0
        
    valores = (
        datos["nombre"],
        datos["edad"],
        datos["peso"],
        datos["personalidad"],
        datos["descripcion"],
        castrado,
        datos["tipo"],
        datos["genero"],
        datos["foto"]
    )

    consultas = insertDB(CONFIG_DB, sql, valores)

    if consultas == 1:
        resultado = True
    else:
        mensaje = "No se pudo cargar el animal satisfactoriamente"
    return resultado, mensaje