from flask import Flask, redirect, url_for, render_template, url_for

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route("/<name>")
def user(name):
    return f"Hello {name}"

@app.route("/admin")
def admin():
    return redirect(url_for("/"))


if __name__ == "__main__":
    app.run(debug=True)