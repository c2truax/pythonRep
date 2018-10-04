from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play')
def index():
    return render_template("index.html", times = 3, color = "LightBlue")
@app.route('/play/<times>')
def indextwo(times):
    times = int(times)
    return render_template("index.html", times = times, color = "LightBlue")
@app.route('/play/<times>/<color>')
def indexthree(times,color):
    times = int(times)
    return render_template("index.html", times = times, color = color)


if __name__=="__main__":
    app.run(debug=True)
