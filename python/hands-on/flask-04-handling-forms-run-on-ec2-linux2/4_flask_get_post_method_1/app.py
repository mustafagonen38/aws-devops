from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["get", "post"])
def index() :
    return render_template("index.html")
@app.route("/total", methods=["post", "get"])
def total() :
    if request.method == "POST" :
        num1 = request.form.get('value1')
        num2 = request.form.get('value2')
        num3 = request.form.get('value3')
        return render_template("number.html", total= int(num1)+int(num2)+int(num3))      
    else :
        return render_template("number.html", message="Since this is GET request, Total hasn't been calculated")
        
if __name__ == '__main__' :
    app.run(debug=True)