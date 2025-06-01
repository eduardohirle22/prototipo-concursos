from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return redirect(url_for("index"))
    return render_template("login.html")

@app.route("/cadastro-concurso", methods=["GET", "POST"])
def cadastro_concurso():
    if request.method == "POST":
        return redirect(url_for("index"))
    return render_template("cadastro_concurso.html")

@app.route("/inscricao", methods=["GET", "POST"])
def inscricao():
    if request.method == "POST":
        return redirect(url_for("index"))
    return render_template("inscricao.html")

@app.route("/alocacao", methods=["GET", "POST"])
def alocacao():
    if request.method == "POST":
        return redirect(url_for("index"))
    return render_template("alocacao.html")

@app.route("/correcao", methods=["GET", "POST"])
def correcao():
    if request.method == "POST":
        return redirect(url_for("index"))
    return render_template("correcao.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))