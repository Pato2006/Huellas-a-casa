from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/catalogo')
def catalogo():
    return render_template('catalogo.html')

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

if __name__ == "__main__":
    app.run(debug=True)
