# Aplicación Web - Biblioteca Universitaria

Este proyecto consiste en el desarrollo de un sitio web multipágina para una **Biblioteca Universitaria**, construido con el framework **Flask**, plantillas **Jinja2** y **Bootstrap 4** para el diseño visual responsivo.

---

## Estrategia e Implementación

### 1. Servidor y Rutas (`server.py`)
El archivo `server.py` funciona como el punto de entrada de la aplicación. Se crearon cuatro rutas dinámicas:
* `/` (`index`): Página principal del sitio.
* `/catalogo` (`catalogo`): Presenta las categorías de materiales.
* `/servicios` (`servicios`): Muestra la lista de servicios ofertados.
* `/contacto` (`contacto`): Proporciona la ubicación y datos institucionales.

Todas las rutas renderizan sus respectivas plantillas con `render_template()` y envían las variables `titulo` y `mensaje`.

### 2. Herencia de Plantillas (`layout.html`)
Se implementó una plantilla base en `templates/layout.html` que contiene:
* Estructura HTML5 y metadatos responsivos.
* Referencia a la librería **Bootstrap 4.6.2**.
* Menú de navegación horizontal con estilos oscuros (`navbar-dark bg-dark`).
* Redirección dinámica mediante la función `url_for()` de Flask.
* Bloque `{% block content %}` para la inserción de vistas hijas.

### 3. Vistas Hijas
Cada vista hereda de `layout.html` mediante la etiqueta `{% extends "layout.html" %}` y encapsula su contenido en contenedores con la clase `.container-fluid`.