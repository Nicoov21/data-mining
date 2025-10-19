# env -> python -m venv nombre
# .\nombre\Scripts\activate  -> Windows
# source nombre/bin/activate -> Linux/Mac
# deactivate -> para salir del env
#pip install flask
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.before_request
def before_request():
    print("Antes de cada solicitud")

@app.after_request
def after_request(response):
    print("despues")
    return response

@app.route("/")
def index():
    #return "<h1>Hola mundo desde Flask!</h1>"
    cursos = ["Python", "Flask", "Django", "FastAPI"]
    data={
        'titulo':'Index123', 
        'bienvenida':'saludos', 
        'cursos': cursos, 
        'numero_cursos':len(cursos)
    }
    return render_template("index.html", data=data)  #retorna el archivo HTML

@app.route("/contacto/<nombre>/<int:edad>")
def contacto(nombre, edad):
    data = {
        'titulo':'Contacto123', 
        'nombre':nombre,
        'edad':edad
    }
    return render_template("contacto.html", data=data)

def query_string():
    print(request)
    print(request.args)
    print(request.args.get("param1"))
    print(request.args.get("param2"))
    return "ok"

def PaginaError(error):
    # return render_template('error.html'), 404
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.register_error_handler(404, PaginaError)
    app.add_url_rule("/query_string", view_func=query_string)
    app.run(debug=True)  # Ejecuta la aplicación Flask, debug permite ejecutar cambios en tiempo real

