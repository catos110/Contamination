from flask import Flask, render_template
import random
app = Flask(__name__)

lado = ["cara", "cruz"]


@app.route("/")
def hello_world():
    return render_template("cont.html")


@app.route("/hija")
def hija():
    return "<h1>Esta es la pagina hija</h1>"


@app.route("/moneda")
def moneda():
    ranmoneda = random.choice(lado)
    return f"<p>{ranmoneda}</p>"


@app.route("/tech")
def tecnologia():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
