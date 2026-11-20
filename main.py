from flask import Flask, render_template, request

# Crear la aplicación web.
app = Flask(__name__)


# Mostrar el menú principal.
@app.route("/")
def inicio():
    return render_template("index.html")


# Mostrar el formulario de notas y procesar los datos enviados.
@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    if request.method == "POST":
        # Convertir los datos del formulario a números enteros.
        nota1 = int(request.form["nota1"])
        nota2 = int(request.form["nota2"])
        nota3 = int(request.form["nota3"])
        asistencia = int(request.form["asistencia"])

        # Calcular el promedio de las tres notas.
        promedio = (nota1 + nota2 + nota3) / 3

        # Para aprobar deben cumplirse ambos requisitos.
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

    # Al ingresar mediante GET, mostrar el formulario sin resultados.
    return render_template("ejercicio1.html")


# Mostrar el formulario de nombres y procesar los datos enviados.
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

        # Actualizar el candidato cuando otro nombre sea más largo.
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


# Iniciar el servidor al ejecutar directamente este archivo.
if __name__ == "__main__":
    app.run()