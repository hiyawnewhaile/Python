from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')
def hi(name):
    return f'Hi {name}!'

@app.route('/repeat/<string:word>/<int:repeat>')
def repeat(word,repeat):
    return f'{word} '*repeat

@app.route('/<random>')
def none(random):
    return f'Sorry! No response. Try again.'
if __name__ == "__main__":
    app.run(debug=True)