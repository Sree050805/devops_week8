from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        return redirect(url_for("success", name=name))

    return render_template("register.html")


@app.route("/success")
def success():
    name = request.args.get("name")
    return render_template("success.html", name=name)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5001)