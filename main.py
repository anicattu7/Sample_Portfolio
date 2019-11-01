from flask import Flask, render_template

app = Flask(__name__, template_folder="./static/templates")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


@app.route("/portfolio/fakebook")
def fakebook():
    return render_template("fakebook.html")


@app.route("/portfolio/boogle")
def boogle():
    return render_template("Boogle.html")


@app.route("/portfolio/hair-salon")
def hair_salon():
    return render_template("hair-salon.html")


def next1():
    return "Next page"


if __name__ == '__main__':
    app.run(port="4000")
