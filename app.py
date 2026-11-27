import os
from flask import Flask, redirect, render_template, request, session, url_for
import mysql.connector

from config import CONFIG_DB
from utilidades._mysql_db import selectDB, insertDB, updateDB, deleteDB
from utilidades.file_utils import uploadFile
from utilidades.request_utils import getRequest

from modulos.catalogo import (listas_animales, ver_animal, borrar_animal, cargar_animal_nuevo, filtros_mascotas)

from modulos.ver_adopciones import (lista_adopciones, ver_formulario, cambiar_estado, lista_adopciones_usuario, ver_formulario_usuario)

from modulos.usuarios import (buscar_usuario_por_email, crear_usuario, modificar_usuario)

from modulos.ver_donaciones import(lista_donaciones, ver_donacion, cambiar_estado_donaciones, lista_donaciones_usuario, ver_donacion_usuario)


app = Flask(__name__)
app.config["SECRET_KEY"] = "clave-solo-para-desarrollo"

CARPETA_IMG = os.path.join(app.root_path, "static", "img")
EXTENSIONES_AVATAR = {"png", "jpg", "jpeg"}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/catalogo')
def catalogo():
    consultas = listas_animales()
    respuesta = None
    if consultas is None:
        respuesta = "No se pudieron consultar las especialidades.", 500
    else:
        respuesta = render_template('catalogo.html', consultas=consultas, error="")
    return respuesta

@app.route('/catalogo/filtros', methods=['GET', 'POST'])
def filtros():
    datos = getRequest()
    consultas = filtros_mascotas(datos)
    if consultas is None:
        return "No se pudieron consultar los animales.", 500
    return render_template('catalogo.html', consultas=consultas)    

@app.route('/catalogo/<int:id>/detalle/')
def detalle(id):
    consultas = ver_animal(id)
    respuesta = None
    if consultas is None:
        respuesta = "No se pudieron consultar las especialidades.", 500
    else:
        respuesta = render_template('detalle.html', consultas=consultas[0], error="")
    return respuesta

@app.route('/catalogo/detalle/formulario_adopcion')
def formulario_adopcion():
    return render_template('formulario_adopcion.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ""
    respuesta = None

    if request.method == "POST":
        datos = getRequest()
        usuario = buscar_usuario_por_email(datos.get("correo", ""))
        credenciales_correctas = False

        if usuario:
            contrasena = datos.get("contrasena", "")
            credenciales_correctas = usuario["contrasena"] == contrasena

        if credenciales_correctas:
            session["usuario_id"] = usuario["id"]
            session["nombre"] = usuario["nombre"]
            session["apellido"] = usuario["apellido"]
            session["correo"] = usuario["correo"]
            session["telefono"] = usuario["telefono"]
            session["fecha_nacimiento"] = str(usuario["fecha_nacimiento"])
            session["tipo"] = usuario["tipo"]

            if usuario["tipo"] == "Admin":    
                respuesta = redirect(url_for("index_admin"))
            else:
                respuesta = redirect(url_for("index"))
        else:
            error = "Email o contraseña incorrectos."
    if "usuario_id" in session:
        respuesta = render_template("perfil.html", usuario=session, aviso="Ya tenés una sesión iniciada.")

    if respuesta is None:
        respuesta = render_template("login.html", error=error)

    return respuesta

@app.route('/registro', methods=['GET', 'POST'])
def registrar():
    datos = {}
    error = ""
    respuesta = None

    if request.method == "POST":
        datos = getRequest()

        exito, error = crear_usuario(datos)

        if exito:
            respuesta = redirect(url_for("login"))

    if respuesta is None:
        respuesta = render_template("registro.html", datos=datos, error=error)

    return respuesta

@app.route('/formulario_donar')
def formulario_donar():
    return render_template('formulario_donar.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/perfil')
def perfil():
    respuesta = None

    if "usuario_id" not in session:
        respuesta = redirect(url_for("login"))
    else:
        respuesta = render_template("perfil.html", usuario=session)

    return respuesta

@app.route('/perfil/modificar', methods=['GET', 'POST'])
def perfil_mod():
    error = ""
    respuesta = None

    if "usuario_id" not in session:
        respuesta = redirect(url_for("login"))
    else:
        datos = {
            "nombre": session["nombre"],
            "apellido": session["apellido"],
            "correo": session["correo"],
            "telefono": session["telefono"],
            "fecha_nacimiento": session["fecha_nacimiento"]
        }

        if request.method == "POST":
            datos = getRequest()
            error = modificar_usuario(session["usuario_id"], datos)

            if error == "":
                session["nombre"] = datos["nombre"]
                session["apellido"] = datos["apellido"]
                session["correo"] = datos["correo"]
                session["telefono"] = datos["telefono"]
                session["fecha_nacimiento"] = datos["fecha_nacimiento"]
                respuesta = redirect(url_for("perfil"))

        if respuesta is None:
            respuesta = render_template("perfil_mod.html", datos=datos, error=error, usuario=session)

    return respuesta

@app.route('/perfil/formulario_adopcion')
def perfil_form_adop():
    if "usuario_id" not in session:
        respuesta = redirect(url_for("login"))
    else:
        consultas = lista_adopciones_usuario(session["usuario_id"])
        if consultas is None:
            respuesta = "No se pudieron consultar las adopciones.", 500
        else:
            respuesta = render_template('perfil_form_adop.html', consultas=consultas)
    return respuesta

@app.route('/perfil/formulario_adopcion_respondido_usuario/<int:formulario_id>')
def formulario_adopcion_respondido_usuario(formulario_id):
    if "usuario_id" not in session:
        respuesta = redirect(url_for("login"))
    else:
        consultas = ver_formulario_usuario(formulario_id, session["usuario_id"])
        if not consultas:
            respuesta = "Formulario de adopcion no encontrado.", 404
        else:
            respuesta = render_template('formulario_adopcion_respondido_usuario.html', consultas=consultas[0])
    return respuesta

@app.route('/perfil/formulario_donacion')
def perfil_form_dona():
    if "usuario_id" not in session:
        respuesta = redirect(url_for("login"))
    else:
        consultas = lista_donaciones_usuario(session["usuario_id"])
        if consultas is None:
            respuesta = "No se pudieron consultar las donaciones.", 500
        else:
            respuesta = render_template('perfil_form_dona.html', consultas=consultas)
    return respuesta

@app.route('/perfil/formulario_donar_respondido_usuario/<int:donacion_id>')
def formulario_donar_respondido_usuario(donacion_id):
    if "usuario_id" not in session:
        respuesta = redirect(url_for("login"))
    else:
        consultas = ver_donacion_usuario(donacion_id, session["usuario_id"])
        if not consultas:
            respuesta = "Formulario de donacion no encontrado.", 404
        else:
            respuesta = render_template('formulario_donar_respondido_usuario.html', consultas=consultas[0])
    return respuesta

#ADMINISTRADOR

@app.route('/index_admin')
def index_admin():
    return render_template('index_admin.html')

@app.route('/catalogo_admin')
def catalogo_admin():
    consultas = listas_animales()
    respuesta = None
    if consultas is None:
        respuesta = "No se pudieron consultar las especialidades.", 500
    else:
        respuesta = render_template('catalogo_admin.html', consultas=consultas, error="")
    return respuesta

@app.route('/catalogo_admin/detalle_modificar_admin')
def detalle_modificar_admin():
    return render_template('detalle_modificar_admin.html')

@app.route('/catalogo_admin/borrar/<int:animal_id>', methods=['POST'])
def eliminar_animal(animal_id):
    consultas = borrar_animal(animal_id)
    retorno = ""
    if consultas is None:
        retorno = "No se pudo eliminar el animal.", 500
    else:
        retorno = redirect(url_for('catalogo_admin'))
    return retorno

@app.route('/cargar_animales')
def cargar_animales():
    return render_template('cargar_animales.html')

@app.route('/cargar_animales/nuevo', methods=['GET', 'POST'])
def subir_animales():
    error = ""
    datos = {}
    respuesta = None
    
    if request.method == "POST":
        datos = getRequest()
        datos = uploadFile(
            datos,
            campo="foto",
            carpeta=CARPETA_IMG,
            extensiones_permitidas=EXTENSIONES_AVATAR,
        )
        if "error_foto" in datos:
            error = datos["error_foto"]
        else:
            exito, error = cargar_animal_nuevo(datos)
            if exito:
                respuesta = redirect(url_for("catalogo_admin"))
    if respuesta is None:
        respuesta = render_template("cargar_animales.html", datos=datos, error=error)
    return respuesta

@app.route('/ver_formulario_adopcion_admin')
def ver_formulario_adopcion_admin():
    consultas = lista_adopciones()
    if consultas is None:
        respuesta = "No se pudieron consultar las adopciones.", 500
    else:
        respuesta = render_template('ver_formulario_adopcion_admin.html', consultas=consultas)
    return respuesta 

@app.route('/ver_formulario_adopcion_admin/formulario/<int:formulario_id>')
def formulario_adopcion_respondido_admin(formulario_id):
    consultas = ver_formulario(formulario_id)
    if consultas is None:
        respuesta = "Formulario no encontrado.", 404
    else:
        respuesta = render_template('formulario_adopcion_respondido_admin.html', consultas=consultas[0])
    return respuesta

@app.route('/ver_formulario_adopcion_admin/<int:formulario_id>/estado', methods=['POST'])
def cambiar_estado_adopcion(formulario_id):
    estado = request.form.get('estado')
    if estado in ('Aceptado', 'Rechazado'):
        cambiar_estado(formulario_id, estado)
    respuesta = redirect(url_for('ver_formulario_adopcion_admin'))
    return respuesta

@app.route('/formulario_donar_admin')
def formulario_donar_admin():
    consultas=lista_donaciones()
    if consultas is None:
        respuesta="No se pudieron consultar las donaciones", 500
    else:
        respuesta=render_template('formulario_donar_admin.html', consultas=consultas)
    return respuesta 

@app.route('/formulario_donar_admin/donacion/<int:donacion_id>')
def formulario_donar_respondido_admin(donacion_id):
    consultas=ver_donacion(donacion_id)
    if consultas is None:
        respuesta="Formulario de donacion no encontrado.", 404
    else:
        respuesta=render_template('formulario_donar_respondido_admin.html', consultas=consultas[0])
    return respuesta

@app.route('/formulario_donar_admin/estado/<int:donacion_id>', methods=['POST'])
def cambiar_estado_donacion(donacion_id):
    estado = request.form.get('estado')
    if estado not in ('Recibido', 'No recibido'):
        respuesta = "Estado invalido.", 400
    elif cambiar_estado_donaciones(donacion_id, estado) is None:
        respuesta = "No se pudo cambiar el estado de la donacion.", 500
    else:
        respuesta = redirect(url_for('formulario_donar_admin'))
    return respuesta


if __name__ == "__main__":
    app.run(debug=True)
