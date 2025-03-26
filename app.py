from flask import Flask, render_template
from route import livro_bp

app = Flask(__name__)

# Registro do Blueprint de livros
app.register_blueprint(livro_bp)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/view/livro")
def view_biblioteca():
    return render_template("biblioteca.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=85)
