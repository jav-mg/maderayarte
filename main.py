from config import *
from mail import *

# ~~~ rutas ~~~
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contacto", methods=["POST"])
def contact():
    personaNombre = request.form['nombre']
    personaTelefono = request.form['telefono']
    personaCorreo = request.form['correo']
    personaMsg = request.form['mensaje']

    destinatario = CONFIG_DESTINATARIO
    asunto = "Contacto desde :: maderarte ::"
    cuerpo = f"Esta persona de nombre: {personaNombre}\n correo: {personaCorreo}\n telefono: {personaTelefono}\n escribio:\n{personaMsg}"
    enviarCorreo(asunto, cuerpo, destinatario)
    print(destinatario)

    return redirect(url_for('home'))

#inicia servidor
if __name__ == "__main__":
    app.run(debug = False)