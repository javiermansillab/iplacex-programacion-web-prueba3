from flask import Flask, render_template, request, redirect, url_for, abort

# Crear la aplicación web.
app = Flask(__name__)

# Mostrar el menú principal.
@app.route("/")
def inicio():
    return render_template("index.html")

# Dirigir al formulario solicitado mediante un número en la URL.
@app.route("/ejercicio/<int:numero>")
def seleccionar_ejercicio(numero):
    if numero == 1:
        return redirect(url_for("ejercicio1"))
    elif numero == 2:
        return redirect(url_for("ejercicio2"))

    # Rechazar la solicitud si el ejercicio no existe.
    abort(404)

# Mostrar el formulario de ejercicio 1 y procesar los datos enviados.
@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    if request.method == "POST":

        # Recibir los datos del formulario.
        # Convertir los datos y controlar valores no válidos.
        try:
            nota1 = int(request.form["nota1"])
            nota2 = int(request.form["nota2"])
            nota3 = int(request.form["nota3"])
            asistencia = int(request.form["asistencia"])
        except ValueError:
            return render_template(
                "ejercicio1.html",
                error="Debes ingresar números enteros.",
                nota1=request.form["nota1"],
                nota2=request.form["nota2"],
                nota3=request.form["nota3"],
                asistencia=request.form["asistencia"]
            )

        # Verificar los rangos antes de calcular el promedio.
        if (nota1 < 10 or nota1 > 70 or
                nota2 < 10 or nota2 > 70 or
                nota3 < 10 or nota3 > 70 or
                asistencia < 0 or asistencia > 100):
            return render_template(
                "ejercicio1.html",
                error="Las notas deben estar entre 10 y 70 y la asistencia entre 0 y 100.",
                nota1=nota1,
                nota2=nota2,
                nota3=nota3,
                asistencia=asistencia
            )
        
        # Calcular el promedio de las tres notas.
        promedio = (nota1 + nota2 + nota3) / 3

        # Requisitos para aprobar.
        if promedio >= 40 and asistencia >= 75:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"

        # Mostrar el resultado y conservar los datos en los campos.
        return render_template(
            "ejercicio1.html",
            promedio=promedio,
            estado=estado,
            nota1=nota1,
            nota2=nota2,
            nota3=nota3,
            asistencia=asistencia
        )

    return render_template("ejercicio1.html")


# Mostrar el formulario de ejercicio 2 y procesar los datos enviados.
@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    if request.method == "POST":

        # Recibir los tres nombres como texto.
        nombre1 = request.form["nombre1"]
        nombre2 = request.form["nombre2"]
        nombre3 = request.form["nombre3"]

        # Detener la comparación si hay nombres repetidos.
        if nombre1 == nombre2 or nombre1 == nombre3 or nombre2 == nombre3:
            return render_template(
                "ejercicio2.html",
                error="Debes ingresar tres nombres diferentes.",
                nombre1=nombre1,
                nombre2=nombre2,
                nombre3=nombre3
            )

        # Conservar el primer nombre en caso de empate de longitud.
        nombre_mayor = nombre1

        # Actualizar cuando otro nombre sea más largo.
        if len(nombre2) > len(nombre_mayor):
            nombre_mayor = nombre2
        if len(nombre3) > len(nombre_mayor):
            nombre_mayor = nombre3
        cantidad = len(nombre_mayor)

        # Mostrar el resultado y conservar los nombres ingresados.
        return render_template(
            "ejercicio2.html",
            nombre_mayor=nombre_mayor,
            cantidad=cantidad,
            nombre1=nombre1,
            nombre2=nombre2,
            nombre3=nombre3
        )

    return render_template("ejercicio2.html")


# Iniciar el servidor al ejecutar este archivo.
if __name__ == "__main__":
    app.run()