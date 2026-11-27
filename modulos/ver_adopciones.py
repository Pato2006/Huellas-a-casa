from config import CONFIG_DB
from utilidades._mysql_db import deleteDB, insertDB, selectDB, updateDB

def lista_adopciones():
    sql = """SELECT formularios.id AS formulario_id, formularios.estado,
                    mascotas.nombre, mascotas.edad, mascotas.peso, mascotas.personalidad,
                    mascotas.descripcion, mascotas.tipo, mascotas.genero, mascotas.ruta_img
             FROM formularios
             INNER JOIN mascotas ON formularios.mascota_id = mascotas.id
             ORDER BY formularios.id DESC"""
    return selectDB(CONFIG_DB, sql, dictionary=True)

def ver_formulario(formulario_id):
    sql = """SELECT formularios.*, mascotas.nombre AS mascota_nombre
             FROM formularios
             INNER JOIN mascotas ON formularios.mascota_id = mascotas.id
             WHERE formularios.id = %s"""
    return selectDB(CONFIG_DB, sql, (formulario_id,), dictionary=True)

def cambiar_estado(formulario_id, estado):
    sql = "UPDATE formularios SET estado = %s WHERE id = %s"
    return updateDB(CONFIG_DB, sql, (estado, formulario_id))

def lista_adopciones_usuario(usuario_id):
    sql = """SELECT formularios.id AS formulario_id, formularios.estado,
                    mascotas.nombre AS mascota_nombre, mascotas.ruta_img
             FROM formularios
             INNER JOIN mascotas ON formularios.mascota_id = mascotas.id
             WHERE formularios.usuario_id = %s
             ORDER BY formularios.id DESC"""
    return selectDB(CONFIG_DB, sql, (usuario_id,), dictionary=True)

def ver_formulario_usuario(formulario_id, usuario_id):
    sql = """SELECT formularios.*, mascotas.nombre AS mascota_nombre,
                    usuarios.nombre AS usuario_nombre, usuarios.apellido AS usuario_apellido
             FROM formularios
             INNER JOIN mascotas ON formularios.mascota_id = mascotas.id
             INNER JOIN usuarios ON formularios.usuario_id = usuarios.id
             WHERE formularios.id = %s AND formularios.usuario_id = %s"""
    return selectDB(CONFIG_DB, sql, (formulario_id, usuario_id), dictionary=True)