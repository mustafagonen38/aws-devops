#Import Flask modules
from flask import Flask, render_template, redirect, url_for

#Create an object named app 
app = Flask(__name__)

# Create a function named home which returns a string 'This is home page for no path, <h1> Welcome Home</h1>' 
# and assign route of no path ('/')
@app.route('/')
def home() :
    return 'This is home page for no path, <h1> Welcome Home</h1>'

# Create a function named about which returns a formatted string '<h1>This is my about page </h1>' 
# and assign to the static route of ('about')
@app.route('/about')
def about() :
    return '<h1>This is my about page </h1>'

# Create a function named error which returns a formatted string '<h1>Either you encountered an error or you are not authorized.</h1>' 
# and assign to the static route of ('error')
@app.route('/error')
def error() :
    return '<h1>Either you encountered an error or you are not authorized.</h1>'

# Create a function named hello which returns a string of '<h1>Hello, World! </h1>' 
# and assign to the static route of ('/hello')
@app.route('/hello')
def hello() :
    return '<h1>Hello, World! </h1>'

# Create a function named admin which redirect the request to the error path 
# and assign to the route of ('/admin')
@app.route('/admin')
def admin() :
    return redirect(url_for('error'))

# Create a function named greet which return formatted inline html string 
# and assign to the dynamic route of ('/<name>')
# @app.route('/<string:name>')
# def greet(name) :
#     greet_format = f"""
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Greeting Page</title>
# </head>
# <body>
#     <h1> Hello, {name}! </h1>
#     <h2> Welcome to my greeting page.</h2>
# </body>
# </html>
#     """
#     return greet_format

# Create a function named greet_admin which redirect the request to the greet-admin path with param of 'Master Admin!!!!' 
# and assign to the route of ('/greet-admin')
@app.route('/greet-admin')
def greet_admin() :
    return redirect(url_for('greet', isim = 'Master Admin!!!!'))

# Rewrite a function named greet which which uses template file named `greet.html` under `templates` folder 
# and assign to the dynamic route of ('/<name>')
@app.route('/<string:isim>')
def greet(isim) :
    ad = isim
    return render_template('greet.html', name = ad)

# Create a function named list10 which creates a list counting from 1 to 10 within `list10.html` 
# and assign to the route of ('/list10')
@app.route('/list10')
def list10() :
    liste = range(1,11)
    return render_template('list10.html', list=liste)

# Create a function named evens which show the even numbers from 1 to 10 within `evens.html` 
# and assign to the route of ('/evens')
@app.route('/evens')
def evens() :
    return render_template('evens.html')

# Add a statement to run the Flask application which can be reached from any host on port 80.
@app.route('/mytext.txt')

if __name__=='__main__':
    app.run(debug = True)
    #app.run(host='0.0.0.0', port=80)
    