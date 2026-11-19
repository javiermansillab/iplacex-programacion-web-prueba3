from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    if request.method == "POST":
        nota1 = int(request.form["nota1"])
        nota2 = int(request.form["nota2"])
        nota3 = int(request.form["nota3"])
        asistencia = int(request.form["asistencia"])
        promedio = (nota1 + nota2 + nota3) / 3
        if promedio >= 40 and asistencia >= 75:
            estado = "Aprobado"
        else:
            estado = "Reprobado"
        return render_template("ejercicio1.html", promedio=promedio, estado=estado)
    return render_template("ejercicio1.html")

@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    if request.method == "POST":
        nombre1 = request.form["nombre1"]
        nombre2 = request.form["nombre2"]
        nombre3 = request.form["nombre3"]
        nombre_mayor = nombre1
        
        if len(nombre2) > len(nombre_mayor):
            nombre_mayor = nombre2
        if len(nombre3) > len(nombre_mayor):
            nombre_mayor = nombre3

        cantidad = len(nombre_mayor)
        return render_template("ejercicio2.html", nombre_mayor=nombre_mayor, cantidad=cantidad)

    return render_template("ejercicio2.html")


if __name__ == "__main__":
    app.run()