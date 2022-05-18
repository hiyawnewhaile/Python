from flask_app import app
from flask import render_template, redirect, request, flash, session
from flask_app.models.user import User
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)

@app.route('/')
def reg_n_login():
    return render_template("reg_n_login.html")

@app.route('/register', methods=['POST'])
def register_user():

    if User.validate_user(request.form):
        data = {
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'email' : request.form['email'],
            'password' : bcrypt.generate_password_hash(request.form['password']),
        }
        User.create_user(data)

        users = User.get_user_by_email(request.form)
        user = users[0]
        session['user_id'] = user.id
        session['first_name'] = user.first_name
        return redirect('/dashboard')


    else:
        print("is not valid")

    return redirect('/')

@app.route('/login', methods=['POST'])
def login_user():

    users = User.get_user_by_email(request.form)

    if len(users) != 1:
        flash("Incorrect *Email or Password")
        return redirect('/')

    user = users[0]

    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Incorrect Email or *Password")
        return redirect('/') 

    session['user_id'] = user.id
    session['first_name'] = user.first_name
    return redirect('/dashboard')

@app.route('/dashboard')
def home_page():
    if 'user_id' not in session:
        flash('login to view page')
        return redirect('/')

    return render_template("homepage.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')