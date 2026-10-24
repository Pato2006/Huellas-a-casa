from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/catalogo')
def catalogo():
    return render_template('catalogo.html')

@app.route('/catalogo/detalle')
def detalle():
    return render_template('detalle.html')

@app.route('/catalogo/detalle/formulario_adopcion')
def formulario_adopcion():
    return render_template('formulario_adopcion.html')

@app.route('/login')
def login():
    return render_template('login.html')

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

@app.route('/registro')
def registro():
    return render_template('registro.html')

if __name__ == "__main__":
    app.run(debug=True)
