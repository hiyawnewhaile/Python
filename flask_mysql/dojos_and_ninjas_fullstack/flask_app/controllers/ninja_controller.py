from flask_app  import app
from flask import render_template, redirect, session, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import   Dojo
@app.route('/ninjas')
def ninjas():
    dojos=Dojo.show_all_dojos()

    return render_template("addninja.html", dojos=dojos)

@app.route("/ninjas", methods=["POST"])
def add_ninja():
    data={
        "dojo_id" : request.form["dojo_id"],
        "first_name" : request.form["f_name"],
        "last_name" : request.form["l_name"],
        "age" : request.form["age"],
    }

    Ninja.create_ninja(data)
    return redirect("/dojos")