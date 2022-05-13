from flask import render_template, request, redirect
# import the class from friend.py
from flask_app.models.user import User
from flask_app import app
@app.route("/")
def index():
    # call the get all classmethod to get all friends
    users = User.get_all()
    print(users)
    return render_template("allusers.html", users=users)
            

@app.route("/adduser", methods=["POST"])
def add_user():
    data = {
        'first_name' : request.form["first_name"],
        'last_name' : request.form["last_name"],
        'email' : request.form["email"],
    }
    User.add_user(data)
    return redirect("/")

@app.route("/renderadduser")
def create_user():
    return render_template("adduser.html")

@app.route("/updateuser", methods=["POST"])
def update():
    data={
        'id': request.form["id"],
        'first_name' : request.form["first_name"],
        'last_name' : request.form["last_name"],
        'email' : request.form["email"],
    }
    User.update_user(data)
    return redirect("/")

@app.route("/renderupdateuser/<int:id>")
def render_update(id):
    return render_template("update.html", id=id)

@app.route("/delete/<int:id>")
def delete_user(id):
    data={
        "id" : id
    }
    User.delete_user(data)
    return redirect("/")

@app.route("/<int:id>")
def show_user(id):
    data={
        "id" : id
    }
    users=User.show_user(data)
    print(users)
    return render_template("showuser.html", users=users)


if __name__ == "__main__":
    app.run(debug=True)