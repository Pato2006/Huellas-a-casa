from config import CONFIG_DB
from utilidades._mysql_db import insertDB, selectDB, updateDB


def crear_usuario(datos):
    campos_obligatorios = ["dni", "nombre", "apellido", "correo", "contrasena", "fecha_nacimiento", "telefono"]
    datos_completos = True
    resultado = False
    mensaje = ""

    for campo in campos_obligatorios:
        valor = datos.get(campo, "")
        valor_limpio = valor.strip()

        if valor_limpio == "":
            datos_completos = False

    if not datos_completos:
        mensaje = "Complete todos los campos obligatorios."
    else:
        sql = """
            INSERT INTO usuarios (nombre, apellido, correo ,contrasena,telefono, dni, fecha_nacimiento)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        valores = (
            datos["nombre"],
            datos["apellido"],
            datos["correo"],
            datos["contrasena"],
            datos["telefono"],
            datos["dni"],
            datos["fecha_nacimiento"]
)

        filas_insertadas = insertDB(CONFIG_DB, sql, valores)

        if filas_insertadas is None:
            mensaje = "No se pudo registrar el usuario. Verifique DNI y email."
        else:
            resultado = True

    return resultado, mensaje


def buscar_usuario_por_email(correo):
    sql = """
        SELECT id, nombre, apellido, correo, contrasena, telefono, fecha_nacimiento, tipo
        FROM usuarios
        WHERE correo = %s
    """

    usuarios = selectDB(CONFIG_DB, sql, (correo,), dictionary=True)
    usuario = None

    if usuarios:
        usuario = usuarios[0]

    return usuario

def modificar_usuario(usuario_id, datos):
    mensaje = ""

    for campo in ["nombre", "apellido", "correo", "telefono", "fecha_nacimiento"]:
        if datos.get(campo, "").strip() == "":
            mensaje = "Complete todos los campos obligatorios."

    if mensaje == "":
        sql = """
            UPDATE usuarios
            SET nombre = %s, apellido = %s, correo = %s, telefono = %s, fecha_nacimiento = %s
            WHERE id = %s
        """
        valores = (datos["nombre"], datos["apellido"], datos["correo"],
                   datos["telefono"], datos["fecha_nacimiento"], usuario_id)

        filas = updateDB(CONFIG_DB, sql, valores)

        if filas is None:
            mensaje = "No se pudo modificar el perfil."

    return mensaje