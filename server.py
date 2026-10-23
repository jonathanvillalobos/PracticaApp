from flask import Flask, render_template

app = Flask(__name__)

# Ruta 1: Inicio
@app.route('/')
def index():
    return render_template(
        'index.html',
        titulo='Inicio',
        mensaje='Bienvenido a la Biblioteca Universitaria Central'
    )

# Ruta 2: Catálogo
@app.route('/catalogo')
def catalogo():
    return render_template(
        'catalogo.html',
        titulo='Catálogo de Materiales',
        mensaje='Explora nuestra amplia colección de recursos físicos y digitales.'
    )

# Ruta 3: Servicios
@app.route('/servicios')
def servicios():
    return render_template(
        'servicios.html',
        titulo='Nuestros Servicios',
        mensaje='Conoce los servicios e instalaciones que ponemos a tu disposición.'
    )

# Ruta 4: Contacto
@app.route('/contacto')
def contacto():
    return render_template(
        'contacto.html',
        titulo='Contacto y Ubicación',
        mensaje='Estamos aquí para resolver tus dudas y atender tus solicitudes.'
    )

if __name__ == '__main__':
    app.run(debug=True)