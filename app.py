from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="templates")

chores = [{"chore": "Sample Task", "done": False}]

@app.route("/")
def index():
    return render_template("index.html", chores=chores)


if __name__ == '__main__':
    app.run(debug=True)


