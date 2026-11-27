from config import CONFIG_DB
from utilidades._mysql_db import deleteDB,updateDB,insertDB,selectDB

def lista_donaciones():
    sql="""SELECT donaciones.id AS donacion_id, donaciones.monto AS monto, donaciones.estado AS estado, 
        donaciones.ruta_comp AS comprobante, usuarios.nombre, usuarios.apellido, usuarios.ruta_img
        FROM donaciones
        INNER JOIN usuarios ON donaciones.usuario_id=usuarios.id
        ORDER BY donaciones.id DESC"""
    return selectDB(CONFIG_DB,sql,dictionary=True)

def ver_donacion(donacion_id):
    sql="""SELECT donaciones.id, donaciones.mensaje AS mensaje, donaciones.ruta_comp AS comprobante, 
        usuarios.nombre, usuarios.apellido 
        FROM donaciones
        INNER JOIN usuarios ON donaciones.usuario_id=usuarios.id
        WHERE donaciones.id=%s"""
    return selectDB(CONFIG_DB,sql,(donacion_id,), dictionary=True)

def cambiar_estado_donaciones(donacion_id, estado):
    sql = "UPDATE donaciones SET estado = %s WHERE id = %s"
    return updateDB(CONFIG_DB, sql, (estado, donacion_id))