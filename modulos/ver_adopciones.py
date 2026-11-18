from config import CONFIG_DB
from utilidades._mysql_db import deleteDB, insertDB, selectDB, updateDB

def lista_adopciones():
    sql = """SELECT adopciones.id AS adopcion_id, adopciones.formulario_id, adopciones.estado,
                    mascotas.nombre, mascotas.edad, mascotas.peso, mascotas.personalidad,
                    mascotas.descripcion, mascotas.tipo, mascotas.genero, mascotas.ruta_img
             FROM adopciones
             INNER JOIN mascotas ON adopciones.mascota_id = mascotas.id
             ORDER BY adopciones.id DESC"""
    return selectDB(CONFIG_DB, sql, dictionary=True)

def ver_formulario(formulario_id):
    sql = """SELECT formularios.*, usuarios.nombre AS usuario_nombre, usuarios.apellido AS usuario_apellido
             FROM formularios
             INNER JOIN usuarios ON formularios.usuario_id = usuarios.id
             WHERE formularios.id = %s"""
    return selectDB(CONFIG_DB, sql, (formulario_id,), dictionary=True)

def cambiar_estado(adopcion_id, estado):
    sql = "UPDATE adopciones SET estado = %s WHERE id = %s"
    return updateDB(CONFIG_DB, sql, (estado, adopcion_id))
