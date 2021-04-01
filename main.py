
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def mainPage():

    return render_template("index.html")

@app.route("/login", methods = ["get", "post"])
def loginPage():
    
    data = {}
    loginRedirect = {
        "usuarioCliente": "/reservarCupos",
        "usuarioSecretaria": "/boletos",
        "usuarioAdministrador": "/registrarCupo",
        "usuarioSupervisor": "/"
    }
    
    if( request.form ):
        
        usuario = request.form['username']
        contrasena = request.form["password"]

        if(usuario not in loginRedirect.keys() or contrasena != "1234"):
            data['loginError'] = True
        else:
            return redirect(loginRedirect[usuario])
        
    return render_template("login.html", **data)


@app.route("/registro", methods = ["get", "post"])
def registerPage():

    data = {}
    if( request.form ):

        email = request.form["email"]
        
        if(email == ""):
            data['registerError'] = True

    return render_template("registro.html", **data)

@app.route("/dashboard")
def dashboardPage():

    return render_template("dashboard/index.html")

@app.route("/reservarCupos")
def cuposPage():
    
    data = {"admin": False}

    return render_template("dashboard/reservarCupos.html", **data)

@app.route("/loginPaypal")
def loginPaypalPage():
    
    return render_template("dashboard/loginPaypal.html")

@app.route("/registrarCupo", methods = ["get", "post"])
def registerTicketPage():

    data = {"admin": True}
    
    if(request.form):
        
        data["nuevo"] = [request.form["cantidad"], request.form["destino"]]
        print(data["nuevo"])
    
    return render_template("dashboard/registrarCupo.html", **data)

@app.route("/registerCalendar")
def calendarFrame():

    return render_template("dashboard/calendar.html")

@app.route("/empleados")
def empleadosPage():
    
    data = {"admin": True}

    return render_template("dashboard/empleados.html", **data)

@app.route("/agregarTicket")
def ticketFrame():
    
    data = {"admin": True}
    
    return render_template("dashboard/ingresarCupo.html", **data)

@app.route("/recibo")
def receiptFrame():
    
    return render_template("dashboard/recibo.html")

@app.route("/clientes")
def usersPage():

    data = {"admin": True}

    return render_template("dashboard/usuarios.html", **data)

@app.route("/reportes")
def reportsPage():

    data = {"admin": True}

    return render_template("dashboard/reportes.html", **data)

@app.route("/perfil")
def profilePage():

    data = {"admin": True}

    return render_template("dashboard/perfil.html", **data)
