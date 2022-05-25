from flask_app import app
from flask import render_template, redirect, request, flash, session
# from flask_app.models.user import User
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)

import requests
import json


@app.route('/innerspirit')
def page_face():
    return render_template('inner_spirit.html')

@app.route('/search_cocktail')
def seach_cocktail():
    search = request.form['search']
    r = requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={search}")
    j=r.json()
    print(j['drinks'][0]['strInstructions'])
    return redirect('/results', data = j)
