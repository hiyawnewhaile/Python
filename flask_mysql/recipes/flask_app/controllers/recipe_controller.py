from flask_app import app
from flask import render_template, redirect, request, flash, session 
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

@app.route('/addrecipe')
def add_recipe():
    if 'user_id' not in session:
        flash('login to view page')
        return redirect('/')
    return render_template("addrecipe.html")

@app.route('/addrecipeprocess', methods=["POST"])
def add_recipe_process():
    if Recipe.validate_recipe(request.form):
        data = {
            "name" : request.form["name"],
            "description" : request.form["description"],
            "instructions" : request.form["instructions"],
            "created_at" : request.form["created_at"],
            "under_30_mins" : request.form["under_30_mins"],
            "user_id" : session['user_id']
        }

        Recipe.add_recipe(data)
        return redirect("/dashboard")


    else:
        print("is not valid")
    return redirect('/addrecipe')
        


