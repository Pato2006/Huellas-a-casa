from config import CONFIG_DB
from utilidades._mysql_db import deleteDB, insertDB, selectDB, updateDB

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