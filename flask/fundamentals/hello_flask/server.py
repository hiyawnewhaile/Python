from flask import Flask  # Import Flask to allow us to create our app


app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response


@app.route('/anotherone')
def dift_route():
    return 'another one!!'

@app.route('/test/<route_data>')
def test_data(route_data):
    return f"the route data that was passed in was {route_data}"

@app.route('/multiply/<int:x>/<int:y>')
def mutiply_two_numbers(x,y):
    return f"the result of {x} x {y} is {x*y}"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

