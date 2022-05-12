
from flask import Flask, render_template
# import the class from friend.py
from friends_model import Friend
app = Flask(__name__)
@app.route("/")
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", friends = friends)

@app.route("/addfriend", methods=['Post'])
def addfriend():
    data={
        'first_name' : request.form['first_name_from_form'],
        'last_name' : request.form['last_name_from_form'],
        'occupation' : request.form['occupation_from_form'],
    }

Friend.addfriend(data)

if __name__ == "__main__":
    app.run(debug=True)