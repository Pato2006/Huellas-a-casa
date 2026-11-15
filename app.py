import os
from flask import Flask, redirect, render_template, request, session, url_for
import mysql.connector

from config import CONFIG_DB
from utilidades._mysql_db import selectDB, insertDB, updateDB, deleteDB
from utilidades.file_utils import uploadFile
from utilidades.request_utils import getRequest


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/catalogo')
def catalogo():
    consultas = selectDB(
        CONFIG_DB,
        "SELECT id,nombre,ruta_img FROM mascotas",
        dictionary=True,
    )
    respuesta = None
    if consultas is None:
        respuesta = "No se pudieron consultar las especialidades.", 500
    else:
        respuesta = render_template('catalogo.html', consultas=consultas, error="")
    return respuesta

@app.route('/catalogo/<int:id>/detalle/')
def detalle(id):
    consultas = selectDB(
        CONFIG_DB,
        "SELECT * FROM mascotas WHERE id = %s",(id,),
        dictionary=True,
    )
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
    return render_template('catalogo_admin.html')

@app.route('/catalogo_admin/detalle_modificar_admin')
def detalle_modificar_admin():
    return render_template('detalle_modificar_admin.html')

@app.route('/cargar_animales')
def cargar_animales():
    return render_template('cargar_animales.html')

@app.route('/ver_formulario_adopcion_admin')
def ver_formulario_adopcion_admin():
    return render_template('ver_formulario_adopcion_admin.html')

@app.route('/ver_formulario_adopcion_admin/formulario_adopcion_respondido_admin')
def formulario_adopcion_respondido_admin():
    return render_template('formulario_adopcion_respondido_admin.html')

@app.route('/formulario_donar_admin')
def formulario_donar_admin():
    return render_template('formulario_donar_admin.html')

@app.route('/formulario_donar_admin/formulario_donar_respondido_admin')
def formulario_donar_respondido_admin():
    return render_template('formulario_donar_respondido_admin.html')
    
if __name__ == "__main__":
    app.run(debug=True)
