from flask_app  import app
from flask import render_template, redirect, session, request
from flask_app.models.dojo import Dojo

@app.route('/dojos')
def dojos():

    dojos = Dojo.show_all_dojos()
    print(dojos)

    return render_template("dojos.html", dojos=dojos)



@app.route("/dojos/process", methods=["POST"])
def add_dojo():
    data={
        "name" : request.form["name"],
    }

    Dojo.create_dojo(data)
    return redirect("/dojos")

@app.route("/dojos/<int:id>")
def ninjas_in_dojo(id):
    data={
        "id" : id
    }
    dojos=Dojo.ninjas_in_dojo(data)
    return render_template("ninjas_in_dojo.html", dojos=dojos)