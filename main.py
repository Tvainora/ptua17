from flask import Flask, template_rendered

app = Flask(__name__)

@app.route("/greet/<name>/<age>")
def home():
    return template_rendered("home.html")

@app.route("/greet/<name>/<age>")
def user(name, age):
    return f"Labas, {name} , {age}"

if __name__ == "__main__":
    app.run()