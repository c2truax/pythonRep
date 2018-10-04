from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def checkerboard():
    return render_template("index.html", xtimes = 9, ytimes = 8)
@app.route('/<x>/<y>')
def checkerboardflex(x,y):
    x = int(x) + 1
    y = int(y)
    return render_template("index.html", xtimes = x, ytimes = y)


if __name__=="__main__":
    app.run(debug=True)