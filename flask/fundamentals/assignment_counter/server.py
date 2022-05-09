from flask import Flask, render_template, session, redirect
app=Flask(__name__)
app.secret_key="karamba"

@app.route('/')
def index():
    if "pullups" in session:
        session["pullups"]+=1
    else:
        session["pullups"]=1
    return render_template("index.html")

@app.route('/clear', methods=["post"])
def clear():
    session.clear()
    return redirect('/')

@app.route('/revisit', methods=["post"])
def revisit():
    session["pullups"]+=1
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)