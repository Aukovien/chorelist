from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="templates")

chores = [{"task":"Simple Chore", "done": False}]

@app.route("/")
def index():
    return render_template("index.html", chores=chores)

@app.route("/add", methods=["POST"])
def add():
    chore = request.form["chore"]
    chores.append({"task": chore, "done": False})
    return redirect(url_for("index"))

@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    chore = chores[index]
    if request.method == "POST":
        chore['task'] = request.form["chore"]
        return redirect(url_for("index"))
    else:
        return render_template("edit.html", chore=chore, index=index)

@app.route("/check/<int:index>")
def check(index):
    chores[index]['done'] = not chores[index]['done']
    return redirect(url_for("index"))

@app.route("/delete/<int:index>")
def delete(index):
    del chores[index]
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)


