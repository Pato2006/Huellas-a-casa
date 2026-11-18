import os
from flask import Flask, redirect, render_template, request, session, url_for
import mysql.connector

from config import CONFIG_DB
from utilidades._mysql_db import selectDB, insertDB, updateDB, deleteDB
from utilidades.file_utils import uploadFile
from utilidades.request_utils import getRequest

from modulos.catalogo import (
    listas_animales,
    ver_animal,
    borrar_animal,
    cargar_animal_nuevo
)

from modulos.ver_adopciones import (lista_adopciones, ver_formulario, cambiar_estado)

app = Flask(__name__)

CARPETA_UPLOADS = os.path.join(app.root_path, "static", "img")
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

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/formulario_donar')
def formulario_donar():
    return render_template('formulario_donar.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

@app.route('/perfil/modificar')
def perfil_mod():
    return render_template('perfil_mod.html')

@app.route('/perfil/formulario_adopcion')
def perfil_form_adop():
    return render_template('perfil_form_adop.html')

@app.route('/perfil/formulario_adopcion_respondido_usuario')
def formulario_adopcion_respondido_usuario():
    return render_template('formulario_adopcion_respondido_usuario.html')

@app.route('/perfil/formulario_donacion')
def perfil_form_dona():
    return render_template('perfil_form_dona.html')

@app.route('/perfil/formulario_donar_respondido_usuario')
def formulario_donar_respondido_usuario():
    return render_template('formulario_donar_respondido_usuario.html')

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
            carpeta=CARPETA_UPLOADS,
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
        return "No se pudieron consultar las adopciones.", 500
    return render_template('ver_formulario_adopcion_admin.html', consultas=consultas)

@app.route('/ver_formulario_adopcion_admin/formulario/<int:formulario_id>')
def formulario_adopcion_respondido_admin(formulario_id):
    consultas = ver_formulario(formulario_id)
    if not consultas:
        return "Formulario no encontrado.", 404
    return render_template('formulario_adopcion_respondido_admin.html', f=consultas[0])

@app.route('/ver_formulario_adopcion_admin/<int:formulario_id>/estado', methods=['POST'])
def cambiar_estado_adopcion(formulario_id):
    estado = request.form.get('estado')
    if estado in ('Aceptado', 'Rechazado'):
        cambiar_estado(formulario_id, estado)
    return redirect(url_for('ver_formulario_adopcion_admin'))

@app.route('/formulario_donar_admin')
def formulario_donar_admin():
    return render_template('formulario_donar_admin.html')

@app.route('/formulario_donar_admin/formulario_donar_respondido_admin')
def formulario_donar_respondido_admin():
    return render_template('formulario_donar_respondido_admin.html')
    
if __name__ == "__main__":
    app.run(debug=True)
