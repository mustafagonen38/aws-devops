from flask import Flask, render_template, request

app = Flask(__name__)

def lcm(num1, num2) :
    list = []
    for i in range(max(num1, num2), num1*num2+1) :
        if i%num1==0 and i%num2==0 :
            list.append(i)
    return min(list)

@app.route("/")
def open() :
    return render_template("index.html")

@app.route("/result", methods=["GET", "POST"])
def result() :
    if request.method == "POST" :
        num1 = request.form["value1"]
        num2 = request.form["value2"]
        return render_template("result.html", LCM = lcm(int(num1), int(num2)), say1=num1, say2=num2)
    else :
        return render_template("result.html")

if __name__  == "__main__" :
    app.run(debug=True)