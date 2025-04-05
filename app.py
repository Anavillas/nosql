from flask import Flask, render_template
from route import livro_bp
from routeUser import user_bp


app = Flask(__name__)

# Registro do Blueprint de livros
app.register_blueprint(livro_bp)
app.register_blueprint(user_bp)



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/view/livros")
def view_biblioteca():
    return render_template("biblioteca.html")

@app.route("/view/user")
def view_user():
    return render_template("user.html")

@app.route("/view/userlivro")
def view_userlivro():
    return render_template("userlivro.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=85)
